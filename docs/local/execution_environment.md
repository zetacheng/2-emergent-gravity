# Declared execution environment

## Configuration

| Item | Declared value |
|---|---|
| Execution identity | `zeta-3070\\codexsandboxoffline` |
| Interpreter | `C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python312\\python.exe` |
| Virtual environment | `C:\\p2-validator\\venv` |
| Required packages | `pytest`, `ruff`, `numpy`, `sympy` |

## Last validated snapshot

Validated on 2026-08-04 under the declared execution identity:

| Component | Observed version |
|---|---|
| Python | `3.12.10` |
| pytest | `9.1.1` |
| ruff | `0.16.1` |
| numpy | `2.5.1` |
| sympy | `1.14.0` |

**Version policy:** package names are the requirement; these versions are a
dated snapshot, not pins.

## Location rationale

`C:\\p2-validator` is outside `%TEMP%`, which Windows Storage Sense may clear,
and outside `C:\\Users\\User\\`, whose ACLs do not by default grant the declared
execution identity execute permission. The PI granted execute permission on the
interpreter directory and on `C:\\p2-validator` on 2026-08-04.

## If unusable

Follow rule 13's diagnostic order. Do not reinstall the interpreter or relocate
the virtual environment unless the declared interpreter is confirmed absent.
A permission failure is not absence. If absence is confirmed, restore the
declared interpreter at its declared path and report the action.
