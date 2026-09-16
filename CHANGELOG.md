# Changelog

All notable changes to this repository should be documented in this file.

The format is inspired by Keep a Changelog and semantic versioning principles for documentation releases.

> **Note**: This changelog was added on 2026-05-06. Entries before that date are reconstructed retrospectively from git history; full diff context lives in `git log`. Future entries are written at the time of the change.

## [1.3.0] - 2026-09-16

### Added
- `docs/CORE/TE_BOOTLOADER_v7_1_EN.md` — Bootloader v7.1, now the entry point. Adds §2.5, the pre-output Functional Verification Pass (Φ-test), as a constitutive check applied before any output is released. Supersedes v6.0, which is retained for the record.
- `docs/CORE/TE_PROTOCOLS_v1_0_EN.md` — the always-active operational protocols (Controfase, P-AI self-diagnosis, Anti-Attractor-Lock, Statistical vs Ordinative Truth, Contextual Self-Preservation). Loaded alongside the Bootloader; previously absent from this repository.
- `docs/NOTATION/TE_SYMBOL_CANON_v1_0_EN.md` — the Symbol Canon for the Ordinative Sciences Programme (content v1.2). Binding before writing, editing or translating any formal notation; carries the reservation procedure for minting new symbols.
- `papers/direction_problem/` — *The Direction Problem*, preprint v1.1, with PDF, LaTeX source and Markdown. The companion paper to *The Collapse Equation*: the causal argument behind g_j. Not previously published anywhere.
- `papers/collapse_equation/` — v1.3 files added alongside the v1.2 set, which is retained as the version archived under DOI 10.5281/zenodo.19932312.

### Updated
- `docs/CORE/TE_CORE_v5_1_EN.md` — content advanced to **v5.2**: the ordinative-set glyph `ℐ → 𝓘` throughout (Tier-0 master primitive; `ℐ` stays reserved for PA's Invariant Space), the SHACK binary-state notation documented as the canon's logogram label-convention, and a notational-governance pointer to the Symbol Canon. The file name retains `v5_1` to preserve its cross-references, per the ratified naming policy. No ontology, axiom, glossary or protocol content was changed.
- `docs/MODULES/TE_MODULE_SVP_v5_1_EN.md` — adds the S-namespace callout distinguishing SVP source levels (S₀–S∅), analytical confidence grades (S₀–S₃) and the Strip operator S of Semantic Algebra. Purely additive.
- `docs/OST/Ordinative_Set_Theory_OST_A_Concise_Guide_For_AI_v2_1.md` — adds the Tier-0 notation callout. Purely additive.
- `docs/OST/OST_Extension_Teleodynamics_Causal_Inversion_v1_1.md` — content advanced to **v1.2**: notational alignment (ℳ vs 𝕄, Φ₄D₊, 𝔽_sem/𝔽_alg, δ) plus Version Notes.
- `papers/collapse_equation/` — the Markdown edition's header brought to parity with the LaTeX source: the Status line still read "seven micro-junctions (five confirmed)" where the paper reports eight observed and six confirmed; a duplicate `Date` line was removed.
- `README.md`, `ECOSYSTEM.md` — ecosystem extended from four pillars to five with `te-controfase`; repository tree, Papers section and the AI Getting Started sequence updated to the current load order (Bootloader v7.1 → Protocols → Core → Symbol Canon → SVP gate).

### Notes
- This release reconciles a divergence between the published framework and the working copies held in the author's vault. Five substantive sections developed in March 2026 — the *Three States of Form-Content Relationship* and *Projective Void* (Core), *Ordinative Algebraic Deduction* (SVP), *Compensatory Specialty Narrative* (LENS), *Structural Void Patterns* and the *Combined Perceptive Influence Model* (PPRO), and the *Dote e Residuo* principle (VERI) — were published here but absent from the working copies, which had separately received the June 2026 Symbol Canon alignment. The two lines are now merged in both directions. Nothing published was removed.

## [1.2.0] - 2026-05-06

### Updated
- `ECOSYSTEM.md` extended from 3-pillar to 4-pillar architecture to include the new `te-ordinative-algebras-en` repository (SA + PA frameworks).
- `README.md` "Part of a Larger Ecosystem" table updated from three-part to four-part, with row added for `te-ordinative-algebras-en`.

### Added
- `CHANGELOG.md` (this file).

### Notes
- The new repository [`te-ordinative-algebras-en`](https://github.com/anckhalion/te-ordinative-algebras-en) was published on 2026-05-06 with initial release `v1.0.0`. It contains the Semantic Algebra (SA) and Proportional Algebra (PA) corpora plus a Python reference engine for PA.

## [1.1.1] - 2026-05-01

### Updated
- LaTeX formatting fix: Table 7 (SVP confidence grading) overflow corrected by switching to `tabularx`.

## [1.1.0] - 2026-04-30

### Added
- *The Collapse Equation v1.2 Beta* — first empirical measurement of `g_j`.
- DOI badge for the Collapse Equation paper.
- CC BY 4.0 license declaration for the paper.
- Citation criteria for the Collapse Equation.

## [1.0.1] - 2026-04-20

### Added
- Ecosystem cross-links between this repository and the other public repositories of the Ordinative Sciences programme.
- Shared `ECOSYSTEM.md` map.

## [1.0.0] - 2026-03-30

### Added
- DOI badge linked to Zenodo deposit for the framework corpus.

## [0.1.0] - 2026-03-27

### Added
- Initial commit: Ordinative Sciences Framework Core & Modules.
- TE Core, Bootloader, and module documents (SVP, SCIMS, VERT, LENS, PPRO, OBSERVER) made publicly available.
