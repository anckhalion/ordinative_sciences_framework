# Endnote and Bibliography Policy

## Two-tier citation system

1. **Endnotes** — per chapter, numbered from 1, at the end of each chapter. Endnotes provide context, qualification, or compact reference to a source.
2. **Bibliography** — one consolidated list at the end of the book, alphabetical by author, full citations in a consistent format.

This is the Penrose / Deutsch / Tegmark model. Endnotes are never footnotes; they don't interrupt the page. Readers who want to check a source flip to the chapter's endnote block; readers who don't, never see them.

## Inline marker convention

Markdown footnote syntax, Pandoc-compatible:

```markdown
Bohr insisted that measurement apparatus is constitutive of the phenomenon observed.[^1]
```

With at end of chapter:

```markdown
## Notes

[^1]: Bohr, *Atomic Physics and Human Knowledge* (1958), pp. 32–66.
[^2]: See also Heisenberg, *Physics and Philosophy* (1958).
```

For LaTeX export, these convert to `\endnote{...}` or chapter-end footnote sections automatically.

## What gets cited

**Cite** when:
- You attribute a specific claim to a specific author ("Bohr argued that...")
- You use a term defined elsewhere (first use only per chapter)
- You make a historical claim that a reader might want to verify
- You take a position in a debate and want to acknowledge the other side
- You invoke a specific piece of data (Piri Reis map, Göbekli Tepe date)

**Do NOT cite** when:
- The claim is common knowledge within the field
- You are making an internal TE derivation (no external source)
- You repeat your own earlier argument
- You are being rhetorical rather than making a factual claim

## Citation format (short form in endnotes)

Author *Title* (Year) — first mention; shorter forms thereafter.

- First mention: *Bohr, Atomic Physics and Human Knowledge (1958), pp. 32–66.*
- Subsequent: *Bohr (1958), p. 45.*

For journal articles:
- First: *Chalmers, "Facing Up to the Problem of Consciousness", J. Conscious. Studies 2(3) (1995): 200–219.*
- Subsequent: *Chalmers (1995), p. 205.*

## Bibliography format (full)

Standard Chicago author-year, alphabetical. Example:

```
Bohr, Niels. 1958. Atomic Physics and Human Knowledge. New York: Wiley.
Chalmers, David J. 1995. "Facing Up to the Problem of Consciousness."
    Journal of Consciousness Studies 2, no. 3: 200–219.
Wheeler, John A. 1989. "Information, Physics, Quantum: The Search for Links."
    In Proceedings of the 3rd International Symposium on the Foundations
    of Quantum Mechanics, 354–368. Tokyo.
```

## Practical workflow

1. As a chapter is reviewed, flag claims that need citation with a placeholder: `[^CITE: Bohr on measurement]`
2. At the end of chapter review, convert placeholders to numbered endnotes `[^1]`, `[^2]`, ... and add the full short-form citation at the chapter's `## Notes` section
3. Each new source is added to `BIBLIOGRAPHY.md` with its full entry
4. The final LaTeX build uses the endnote blocks per chapter and the bibliography as a single consolidated list

## File organisation

- `WORKING/chapters/CH0N_*.md` — each chapter, with endnotes in its own `## Notes` section
- `WORKING/BIBLIOGRAPHY.md` — the consolidated bibliography
- `WORKING/ENDNOTE_POLICY.md` — this file
