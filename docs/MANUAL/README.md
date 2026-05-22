# MANUAL — Ordinative Sciences Framework

Theoretical and practical manual of the Technology of Expressions (TE) and the Ordinative Sciences.

This folder contains the source of a book-length work whose final destination is print publication via KDP (trim 6×9"), via the pipeline **Markdown → Pandoc → LaTeX → Overleaf → PDF/X → KDP**.

## Editions

| Folder | Edition | Status |
| --- | --- | --- |
| `IT/` | Edizione italiana (lingua di scrittura primaria dell'autore) | in progress |
| `EN/` | English edition (translated alongside IT) | in progress |
| `shared/` | Language-neutral assets: diagrams, figures, bibliography, build scripts | in progress |

The IT edition is the authorial source. The EN edition is maintained in sync but is not a word-for-word translation: concepts that would be "lost in translation" are re-expressed rather than calqued.

## Folder layout (per edition)

```
IT/
├── 00-front/          # Nota sull'intento, Prefazione, Indice generale
├── 01-propedeutica/   # Cosa sono le scienze ordinative, Come leggere, Arajat (intro)
├── 02-assiomi/        # Assiomi 0–24 (+ 9A, 9A1) — uno per capitolo salvo fusioni motivate
├── 03-ost/            # Ordinative Set Theory: fondamenti, triade ⟨Σ, R, Φ⟩, proprietà
├── 04-arajat/         # Arajat (introduzione; branch in sviluppo)
├── 05-controfase/     # Controfase e P-AI
├── 06-moduli/         # SVP, LENS, VERI, PPRO, SCIMS, OBSERVER
├── 07-pratica/        # Analisi guidate, errori comuni
└── 99-appendici/      # Glossario, tavola sinottica, bibliografia, indice analitico, changelog
```

EN/ mirrors this layout with English-language folder names.

## Editorial conventions

Every axiom chapter follows this fixed schema:

1. **Definizione / Definition** — enunciato esatto dell'assioma.
2. **Posizionamento / Positioning** — dove sta l'assioma nell'architettura (cosa presuppone, cosa rende possibile).
3. **Spiegazione / Explanation** — perché l'assioma è necessario e come va letto.
4. **Esempio / Example** — un caso concreto che rende visibile la struttura.
5. **Fonti / Sources** — rimandi al Core, OST, moduli, bibliografia esterna se pertinente.

Non-axiom chapters may adapt the schema but always separate **definition from explanation from example**.

## Editorial rule (inherited from the authorial intent)

1. Clarity before elegance. If a passage is clear but not elegant, it stays clear. If it is elegant but ambiguous, it is rewritten.
2. No rhetorical concessions to prestige. Citations only position, they do not signal.
3. The reader is assumed competent but new. No undefined jargon; no circular definitions.
4. Explicit audiences: human analysts + AIs seeking to operate outside statistical bias.
5. Academic recognition is a possible consequence, not a writing criterion.

## Build (planned)

A future `shared/build/` folder will contain the Pandoc + LaTeX templates (`book` or `memoir` class, KDP-conformant margins, embedded fonts) to assemble the PDF for print. Not yet implemented — we build the manual in Markdown first, then tool the pipeline.
