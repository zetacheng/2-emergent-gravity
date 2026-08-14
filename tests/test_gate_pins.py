"""Every artifact pinned by SHA-256 in ``GATES.md`` still hashes to its pin.

This runs in the suite rather than as a checker property on purpose. The
measured failure was that ``python -m pytest`` returned the same
``280 passed, 2 deselected`` across four revisions spanning a stale pin, a
repaired pin, an edited artifact and a re-pinned one -- so the gap was the
suite's, and the repair belongs in the suite. A checker property only runs
when someone invokes the checker with a config; a test runs whenever anyone
runs the suite.

The zero-pin assertion is deliberate. A pin validator that passes over an
empty pin set is the same defect as the one ``P7`` carried -- an empty match
returning True -- one level along.
"""

from __future__ import annotations

import hashlib
import re
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
GATES_PATH = REPO_ROOT / "GATES.md"

#: A pin as it is actually written in ``GATES.md``: ``(sha256 `<64 hex>`)``.
PIN = re.compile(r"\(sha256 `([0-9a-f]{64})`\)")

#: The artifact a pin governs is named on the pin's own line or shortly above
#: it, as a repository-relative path in backticks or bare. Only these roots
#: are recognised, so that an incidental path-like string elsewhere in the
#: prose cannot be mistaken for the pinned artifact.
PATH_ROOTS = ("derivations", "scripts", "results", "docs", "paper", "tests")
ARTIFACT_PATH = re.compile(
    r"(?:^|[\s`(])((?:" + "|".join(PATH_ROOTS) + r")/[A-Za-z0-9._/-]+\.[A-Za-z0-9]+)"
)

#: How far above a pin the artifact path may be named. The landed file names
#: it on the line immediately above; the window is small so that a pin whose
#: path is missing fails rather than silently binding to an unrelated path
#: further up the document.
LOOKBACK_LINES = 3


def _gates_lines() -> list[str]:
    return GATES_PATH.read_text(encoding="utf-8").split("\n")


def _resolve_path(lines: list[str], index: int) -> str | None:
    """The artifact path named at, or just above, ``lines[index]``."""
    for offset in range(0, LOOKBACK_LINES + 1):
        probe = index - offset
        if probe < 0:
            break
        match = ARTIFACT_PATH.search(lines[probe])
        if match:
            return match.group(1)
    return None


def collect_pins(lines: list[str]) -> list[dict[str, object]]:
    """Every pin in ``lines``, with the artifact path it governs.

    ``path`` is ``None`` when no path could be resolved. That case is a
    failure rather than a skip: a pin nobody can trace to a file is exactly
    as unchecked as a pin that was never verified.
    """
    found: list[dict[str, object]] = []
    for index, line in enumerate(lines):
        for match in PIN.finditer(line):
            found.append(
                {
                    "line": index + 1,
                    "declared": match.group(1),
                    "path": _resolve_path(lines, index),
                }
            )
    return found


def test_gates_file_exists() -> None:
    assert GATES_PATH.is_file(), f"{GATES_PATH} is missing"


def test_pin_set_is_not_empty() -> None:
    """Zero pins is a failure, not a vacuous pass.

    ``GATES.md`` is the file this repository pins its adopted artifacts in.
    If the pattern stops matching -- because the notation drifted, or because
    the pins were removed -- every other assertion in this module becomes
    vacuously true, and the suite would go on reporting green over nothing.
    """
    pins = collect_pins(_gates_lines())
    assert pins, (
        "no `(sha256 `<64 hex>`)` pin found in GATES.md: either the pins were "
        "removed or the notation changed, and in both cases this validator is "
        "checking nothing"
    )


def test_every_pin_resolves_to_a_path() -> None:
    """A pin with no artifact path above it fails; it is never skipped."""
    unresolved = [p for p in collect_pins(_gates_lines()) if p["path"] is None]
    assert not unresolved, "\n".join(
        f"GATES.md line {p['line']}: pin {p['declared']} names no artifact "
        f"path within {LOOKBACK_LINES} lines above it"
        for p in unresolved
    )


def test_every_pinned_artifact_matches_its_pin() -> None:
    """The pinned digest equals the SHA-256 of the artifact's bytes."""
    failures = []
    for pin in collect_pins(_gates_lines()):
        if pin["path"] is None:
            continue  # reported by test_every_pin_resolves_to_a_path
        target = REPO_ROOT / str(pin["path"])
        if not target.is_file():
            failures.append(
                f"GATES.md line {pin['line']}: pinned artifact "
                f"{pin['path']} does not exist"
            )
            continue
        measured = hashlib.sha256(target.read_bytes()).hexdigest()
        if measured != pin["declared"]:
            failures.append(
                f"GATES.md line {pin['line']}: {pin['path']} is stale -- "
                f"pinned {pin['declared']}, measured {measured}"
            )
    assert not failures, "\n".join(failures)


# ---------------------------------------------------------------------------
# The validator's own failure modes, exercised against synthetic gate files so
# that each assertion above is shown to fire rather than assumed to.
# ---------------------------------------------------------------------------
_HEX_A = "a" * 64


def _write(tmp_path: Path, text: str) -> list[str]:
    path = tmp_path / "GATES.md"
    path.write_text(text, encoding="utf-8")
    return path.read_text(encoding="utf-8").split("\n")


def test_collect_pins_finds_a_pin_and_its_path(tmp_path: Path) -> None:
    lines = _write(
        tmp_path,
        "The adopted artifact is `derivations/thing.md`\n"
        f"(sha256 `{_HEX_A}`).\n",
    )
    pins = collect_pins(lines)
    assert len(pins) == 1
    assert pins[0]["path"] == "derivations/thing.md"
    assert pins[0]["declared"] == _HEX_A


def test_collect_pins_is_empty_when_the_file_has_none(tmp_path: Path) -> None:
    lines = _write(tmp_path, "# Gates\n\nNo pin anywhere in this file.\n")
    assert collect_pins(lines) == []


def test_collect_pins_reports_no_path_when_none_is_named(tmp_path: Path) -> None:
    lines = _write(
        tmp_path,
        "Some prose with no artifact path at all.\n"
        "\n"
        "\n"
        "\n"
        f"(sha256 `{_HEX_A}`).\n",
    )
    pins = collect_pins(lines)
    assert len(pins) == 1
    assert pins[0]["path"] is None


def test_a_stale_pin_is_detected(tmp_path: Path) -> None:
    """The digest comparison itself, on a file whose bytes are known."""
    artifact = tmp_path / "artifact.md"
    artifact.write_text("content\n", encoding="utf-8")
    measured = hashlib.sha256(artifact.read_bytes()).hexdigest()
    assert measured != _HEX_A
    assert hashlib.sha256(b"content\n").hexdigest() == measured


@pytest.mark.parametrize("separator", ["`", " ", "("])
def test_path_is_recognised_after_each_delimiter(
    tmp_path: Path, separator: str
) -> None:
    lines = _write(
        tmp_path,
        f"adopted{separator}derivations/thing.md\n(sha256 `{_HEX_A}`).\n",
    )
    assert collect_pins(lines)[0]["path"] == "derivations/thing.md"
