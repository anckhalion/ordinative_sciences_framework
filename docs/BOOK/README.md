# BOOK — Ordinative Sciences (long-form essay)

This folder contains the source of the **book** version of the work — the essay-form, narrative companion to the technical reference held in `docs/MANUAL/`.

Two distinct objects, two distinct destinations:

| | `docs/MANUAL/` | `docs/BOOK/` |
| --- | --- | --- |
| **Genre** | Reference manual — schematic, citable, lookup-friendly. | Long-form essay — continuous prose, designed to be read front to back. |
| **Voice** | Institutional, neutral, procedural. | Authorial: clear cadence, earned transitions, stakes named. |
| **Sectioning** | Numbered chapters with fixed sub-schema (*Statement · Definition · Positioning · …*). | Chapters with titles, not procedural labels. The schema is internal, never typographic. |
| **Audience** | Analysts looking up a definition, AI agents loading a passage, citations on Zenodo / OSF / HuggingFace, GitHub readers. | Readers — human or artificial — willing to spend several hours on the text. KDP buyers. |
| **Status of priority** | Maintained as parallel reference. | Primary writing investment. |
| **Relationship** | Stand-alone reference. | Cites the MANUAL where rigour is needed; never paraphrases it. |

Both are bilingual: `IT/` (authorial source) and `EN/` (parallel edition, not a calque). `shared/` is reserved for diagrams, bibliography, and assets used across editions.

## Editorial register (BOOK)

These rules govern *how* the book is written, not what it says. The substance comes from the framework documents (`docs/CORE/`, `docs/OST/`, `docs/MODULES/`); the manual condenses; the book *narrates*.

1. **Prose carries.** Numbered sub-sections and tabular fragments are admitted only when the content is genuinely tabular. Default form is a continuous paragraph that respects the reader's breath.
2. **Stakes named, not asserted.** Every chapter opens by making clear what is at risk if the reader does not understand what follows. No throat-clearing, no roll-call of citations.
3. **Rigour invisible, intact.** The technical apparatus is held in the MANUAL. The book references the MANUAL when needed (footnote or inline) but does not re-prove. Trust the reader to look up what they need.
4. **No academic pleading.** The book does not justify itself by listing predecessors. Comparisons appear only where they help position a concept the reader already half-recognises.
5. **The double reader is constant.** The book is written for human and artificial readers throughout — not in alternating chapters, not with separate sections. The grammar is the same; only the difficulty of apprenticeship differs.
6. **Cadence over coverage.** Better to leave a chapter shorter than to dilute its line. Length follows the logic, not a target.
7. **Italian is primary.** The Italian edition is composed first; the English edition is rewritten, not translated, where a literal calque would degrade the concept.

## Folder layout

The book layout is intentionally lighter than the manual's. No fixed Parts/Sub-folders are imposed up front: the architecture of the book emerges from the writing. Files are numbered for ordering only.

```
IT/
├── 00_nota_autore.md       # Nota dell'autore — opening address
├── 01_prologo.md           # Prologue
├── 02_*.md                 # Chapter 1 …
└── 99_chiusura.md          # Closing chapter, acknowledgements, references

EN/
├── 00_authors_note.md
├── 01_prologue.md
└── …
```

Once the book has matured enough to need Parts, we introduce them as named sub-folders (e.g. `IT/parte_prima_soglie/`) — never as numbered abstractions.

## KDP target

- Primary print title.
- Trim 6×9", `book` or `memoir` LaTeX class, KDP-conformant margins, embedded fonts.
- Pipeline: Markdown → Pandoc → LaTeX (template in `shared/build/`, to be added) → Overleaf → PDF/X → KDP.

## Relationship to the MANUAL

The MANUAL grows as a **subsequent condensation** of the book. Each chapter of the book that fixes an axiom, a definition, a module, will have a corresponding compact entry in the MANUAL — written *afterwards*, when the chapter has stabilised. The book is the writing; the manual is the index.

If a discrepancy ever arises between BOOK and MANUAL on a point of doctrine, the source-of-truth is the operative repository (`docs/CORE/`, `docs/OST/`, `docs/MODULES/`). Both BOOK and MANUAL are derivatives.
