# Assumptions

**This directory holds physical assumptions and physical hypotheses** —
propositions that could in principle be established or refuted.

## What this directory does NOT hold

**It does not hold definitional conventions.** Those are the Convention
Registry's, `CONVENTIONS.md`.

**The separation is the point, and it is recent.** A definition is not a
falsifiable proposition: it cannot be refuted by a future calculation, and
filing one here would undo a distinction the repository made deliberately.
`A-EXT-01`, the definitional axis-TT observable, is therefore **canonical in
`CONVENTIONS.md` and has no entry or stub here.**

**A reader looking for the `A-EXT-01` / `H-EXT-01` pair finds both:**
`A-EXT-01` in `CONVENTIONS.md`'s definitional-conventions section, `H-EXT-01`
in this directory, and each names the other.

## The four-way separation

    CONVENTIONS.md    definitions and conventions
    assumptions/      falsifiable or unestablished scientific propositions
    decisions/        PI rulings
    reviews/          reviews of specifications

**A reader can tell what kind of epistemic object a statement is by where the
file sits.**

## One file per entry, in two parts

    PART 1 — THE ENTRY

             ID / Type / Status / Exact statement / Scope /
             What depends on it / What does NOT depend on it / Evidence /
             Falsifier or resolution condition / Review /
             Statement SHA / Review Artifact SHA / Date / Supersedes

    PART 2 — THE REVIEW

             the independent review of Part 1, carrying a `Function:` header,
             naming its author, and stating which parts of Part 1 it accepted,
             required to be changed, and did not address.

**`Type` distinguishes at minimum a physical assumption from a physical
hypothesis.** A definitional convention is not a `Type` this directory
accepts; see above.

## The pin rule

    Statement SHA          SHA-256 of the exact-statement bytes.
                           THIS IS THE BINDING PIN.
    Review Artifact SHA    SHA-256 identifying the review artifact.
                           Provenance, not a pin.

> **Editing the exact statement invalidates the attached review and requires
> re-review.** Editing Part 2, the field labels, or any other field does not.

**The pin is over the statement and not over the file.** With Part 1 and Part 2
in one file, a file digest would break on every review edit and survive nothing
that matters.

## Provenance of records that moved here

**An entry that was first landed elsewhere keeps its original record.** Where a
record is relocated, the original is not deleted and not rewritten; a note
records the relocation and names the new canonical location. **The repository
did not always have this taxonomy, and its history is not edited to pretend
otherwise.**
