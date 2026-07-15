# Result Schema

## Immutability and provenance

Raw outputs are immutable. Never modify a raw artifact manually or replace it
in place. If a run changes, create a new recorded run.

Processed results must identify the exact script and immutable raw input used.
They must also record the gate, configuration, commit hash, branch, date,
environment, regulator, cutoff, normalization, seeds, and operating point.

## Required contents

Every gate result directory must include:

- `README.md` — scientific question, gate, assumptions, and artifact map;
- configuration, normally `config.json`;
- raw output;
- processed table;
- `verdict.md`;
- commit hash;
- branch;
- date;
- environment information, normally `environment.txt`.

Recommended future layout:

```text
results/<gate-id>/
  README.md
  config.json
  raw/
  processed/
  figures/
  verdict.md
  environment.txt
```

The result `README.md` must link processed tables to their producing script and
raw inputs. Checksums are recommended for raw outputs. Failed and retired result
records remain immutable and discoverable.
