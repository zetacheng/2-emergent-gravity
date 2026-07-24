# Arm P decisive merge verification report

## Guard 0 — executor-local EOL configuration

Before checkout and merge, the executor-local configuration was:

```text
core.autocrlf=false
core.eol=lf
```

No repository file records these settings.

## Guard 1 — reviewed remote pins and ancestry

After `git fetch`:

```text
origin/main: 0f7961747abe2a18b436c0b1e5b928f425ea4d9a
origin/run/p2-betav-arm-p-decisive: 48c5cc59f81b148da66cb4366199b59987e53a2a
merge-base --is-ancestor base Arm-P: exit 0
rev-list --count base..Arm-P: 4
```

The reviewed branch structure was therefore current: the four Arm-P commits
descended from the exact pinned main base.

## Guard 2 — pinned merge

`main` equalled `origin/main` at the pinned base before merge. The exact reviewed
Arm-P SHA `48c5cc59f81b148da66cb4366199b59987e53a2a` was merged with `--no-ff` and
the authorized frozen merge message. The resulting merge commit (the
pre-report HEAD) is `8b64b895cac1e1c9b4e8f600449c15ce1ffc66c7`.

The Arm-P branch remains present and is not deleted by this merge.

## Guard 3 — merged-main verification

```text
python -m pytest tests -q
50 passed, 2 deselected

ruff check .
All checks passed!

git merge-base --is-ancestor 48c5cc59f81b148da66cb4366199b59987e53a2a HEAD
exit 0
```

`GATES.md` contains both decisive entries with `Status: RUN`, separate verdict
fields, and the full artifact-digest strings:

```text
918a9b87a8cac8fdff351d85bbfba66d09a80053926d370b634b76b3f11baa1f
29f937e467d0c3d6ed157f4dbd752af65084b621ee7f209badb3845524f26d7d
```

The raw Arm-P blob check returned:

```text
836cc1ab04cd153358d41e677280e058a652244196ba53a34369e373b56d7c4f
```

The working tree was clean before this report was written. The merge preserves
the campaign record without promoting `P2-C9`, releasing the `−3.2(5)`
quarantine, or changing the automatic-promotion prohibition.
