# Branching Policy

## Branch names

```text
gate/<gate-name>
paper/<paper-version>
review/<review-topic>
fix/<issue>
archive/<retired-route>
```

## Rules

- `main` contains accepted infrastructure and accepted closed gates only.
- Active calculations remain on a dedicated gate branch.
- Failed gate branches are preserved.
- Never squash scientific derivation history.
- Prefer conventional commits.
- Tags mark accepted scientific milestones.
- One branch corresponds to one scientific gate or one paper-edit task.
- Paper branches may update `.tex` only after reviewer acceptance.
