"""Compare Git operation records against a declared scope manifest."""

from __future__ import annotations

import argparse
from pathlib import Path

from .core import (
    GOVERNANCE_FAILURE,
    TOOL_ERROR,
    InputError,
    emit,
    evaluate_scope,
    load_json,
)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", default=".")
    parser.add_argument("--manifest", required=True)
    args = parser.parse_args(argv)
    try:
        result = evaluate_scope(Path(args.repo), load_json(args.manifest))
        return emit(result, 0 if result["overall"] == "PASS" else GOVERNANCE_FAILURE)
    except (InputError, OSError) as error:
        return emit(
            {"tool": "scope_checker", "overall": "TOOL_ERROR", "error": str(error)},
            TOOL_ERROR,
        )


if __name__ == "__main__":
    raise SystemExit(main())
