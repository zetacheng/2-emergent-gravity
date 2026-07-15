# Results

Raw outputs are immutable and must never be edited manually. Processed results
must contain complete provenance, including the producing script and raw input.

Every result directory must include:

- `README.md` describing the scientific question and gate;
- configuration;
- raw output;
- a processed table;
- a verdict;
- commit hash;
- branch;
- date;
- environment information.

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

Failed, inconclusive, suspended, and retired outputs remain part of the
scientific record and must be preserved.
