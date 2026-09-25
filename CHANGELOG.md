# Changelog

All notable changes to this repository should be documented in this file.

The format is inspired by Keep a Changelog and semantic versioning principles for documentation releases.

> **Note**: This changelog was added on 2026-05-06. Entries before that date are reconstructed retrospectively from git history; full diff context lives in `git log`. Future entries are written at the time of the change.

## [Unreleased]

### Added
- `dist/` — derived single-file loading sets (`TE_LOADING_SET_FULL.md`: the twelve active documents in loading order; `TE_LOADING_SET_MINIMAL.md`: Bootloader, Protocols, Core, SVP), the LEXX and CASEWORK method bundles (`TE_LEXX_METHOD.md`, `TE_CASEWORK_METHOD.md`), a machine-readable `catalog.json` (documents, versions from the lock, roles, triggers, section outlines, hashes, token estimates, a table resolving references to earlier editions), `SHA256SUMS.txt` and a README. Every document is reproduced byte for byte between delimiters that carry its SHA-256.
- `llms.txt` — index of the repository for LLM tools.
- `tools/build_dist.py` (builds `dist/` and `llms.txt`, regenerates the manifest, builds the release archive), `tools/check_repo.py` (manifest, lock, compatibility profiles, derived files, handbook files, Markdown links), `tools/loading_set.json` (loading order, roles, triggers, profiles, reference resolution), `Makefile` (`test`, `check`, `dist`, `manifest`, `lock`, `package`).
- `docs/handbook/` — documentation for people who use the framework: start here, core concepts, setup for LLMs with a loading smoke test, running an analysis, a four-level training path, glossary, FAQ and troubleshooting, maintainers' guide, and one guide per framework document and domain framework (`modules/`). `docs/README.md` indexes it.
- `.github/workflows/ci.yml` (tests and checks on every push and pull request) and `release.yml` (builds and attaches `te-frameworks-<version>.zip` on a `v*` tag).
- `LICENSE` (MIT), referenced by the README and previously absent; `.gitignore`.

### Fixed
- `FRAMEWORKS/MANIFEST_SHA256.txt` — the entry for `CASEWORK/README.md` still carried the hash from before the "acquisition authority is verified by the case owner" revision; regenerated. The lock and the compatibility profiles were unaffected (Markdown is excluded from package digests).

### Updated
- `README.md` — "Download and load" section, the handbook, the repository tree, the license statement; `FRAMEWORKS/README.md` — derived files and checks; `CONTRIBUTING.md` — the checks to run before a pull request; `.gitattributes` — `dist/**` and `llms.txt` stored byte-exact.

### Notes
- No framework document changed: `FRAMEWORKS/` is byte-identical to release 2.0.0 apart from the regenerated manifest and the added section in its README. Observations on the canonical files (stale section references, historical profile paths, platform-specific wording, the weight of version histories) are recorded in `docs/handbook/07_MAINTAINERS_GUIDE.md` for the canonical corpus.

## [2.0.0] - 2026-09-23

### Added
- `FRAMEWORKS/` — flat, byte-exact publication target of the canonical framework corpus, with canonical file names.
- `FRAMEWORKS/TE_BOOTLOADER_v7_1_1_EN.md`, `FRAMEWORKS/TE_PROTOCOLS_v1_1_EN.md`, `FRAMEWORKS/TE_CORE_v5_2_1_EN.md` — current core set (Protocols published here for the first time; Bootloader and Core register the LEXX and CASEWORK routing).
- `FRAMEWORKS/TE_OST_v2_1_EN.md`, `FRAMEWORKS/TE_OST_Extension_Teleodynamics_v1_1_EN.md` (content 1.2), `FRAMEWORKS/TE_SYMBOL_CANON_v1_0_EN.md` (register status 1.2) — OST foundation, extension and the notation authority, under their canonical names.
- `FRAMEWORKS/LEXX/` — `TE_MODULE_LEXX`, ordinative validation of agreements: method 0.1 (English edition: README, foundations, module, annotated example, compatibility profile, pre-pilot protocol) and runtime 0.2.0-alpha.3 (schema, validator, review request, runtime README, 40 tests). Revision of 2026-09-23 at first publication, runtime version unchanged: `runtime/prepare_run.py` resolves the methodology documents it freezes by edition (`00_FOUNDATIONS.md` or `00_FONDAMENTA.md`, `TE_MODULE_LEXX_v0_1_EN.md` or `TE_MODULE_LEXX_v0_1.md`), with one test added; the placeholder texts of the draft template are in English.
- `FRAMEWORKS/CASEWORK/` — `TE_CASEWORK`, `TE_AUDIT`, `TE_INVESTIGATION` 0.1 with runtime 0.1.0-alpha.1 (schemas, case preparation and validation, 42 tests), the English README and `PILOT_PLAN.md`, and `runtime/make_lock.py`, which builds the framework lock and records its `package_digest` algorithm (packages cover code, schemas, tests and configuration; Markdown excluded).
- `FRAMEWORKS/te_frameworks.lock.json` — the framework lock consumed by `casework.py prepare --lock`, generated against the published bytes.
- `FRAMEWORKS/README.md` — loading order, integrity check, archive policy.
- `FRAMEWORKS/MANIFEST_SHA256.txt` — hashes of every published framework file.
- `.gitattributes` — `FRAMEWORKS/** -text`: git stores and checks out these files byte for byte, so the pinned hashes hold on every platform.

### Updated
- `FRAMEWORKS/TE_MODULE_SVP_v5_1_EN.md`, `FRAMEWORKS/TE_MODULE_SCIMS_v5_1_EN.md`, `FRAMEWORKS/TE_OBSERVER_v1_1_EN.md` — refreshed to the canonical corpus (`LENS`, `PPRO`, `VERI` were already identical).
- Register patch, in place and without version bump: prescriptive uses of «honest / honestly / honesty» in Core (§1.3, §6.7), Bootloader (§4), LENS (two notes) and OBSERVER (§10.1, §10.2) restated as operations, per Bootloader §2.5.2. Wording only; dated patch notes in each file; runtime hashes re-pinned.
- `README.md`, `ECOSYSTEM.md`, `CITATION.cff` rewritten or updated for the new layout.

### Moved
- `docs/CORE/`, `docs/MODULES/`, `docs/OST/`, `docs/NOTATION/` → `FRAMEWORKS/` (current editions) and `FRAMEWORKS/ARCHIVE/` (superseded: Bootloader 6.0, 7.0, 7.1; Core 5.1 — content 5.2; Protocols 1.0; the OST guide and Teleodynamics extension under their previous file names; the archived Bootloader 7.1, Core 5.1 and Protocols 1.0 are the editions published in 1.3.0). `docs/` keeps `ArXiv_Abstract_TE.md`.

### Notes
- Major version: the repository layout changes (flat `FRAMEWORKS/` replaces `docs/CORE|MODULES|OST`) and two domain frameworks with runtimes are added.
- The division of work between each runtime and the signing professional is stated in `README.md` §Domain frameworks and in the compatibility profiles.
- On macOS the CASEWORK tests need a temporary directory that resolves to itself (a real directory; for example `mkdir -p tmp && TMPDIR=$PWD/tmp python -m unittest …`), because the runtime requires source paths that resolve to themselves; see `FRAMEWORKS/CASEWORK/README.md`.
- Both runtimes were exercised end to end from the repository root with the commands printed in their READMEs (`prepare` → `validate` on synthetic input) before this release.
- The OCT validation corpus is published in `te-oct-framework-en`; that mirror keeps its historical file-naming convention and points here for LEXX and CASEWORK.
- Register (2026-09-24): the published documents and the user-facing strings of both runtimes (help texts, messages, report `limits`, draft placeholders) state facts and assignments of function in the positive form; each limit is stated once, in its home (the README status lines, the compatibility profiles, the protocol sections), and the other files point to it.
- Merged from `main` (2026-09-24): release 1.3.0 — *The Collapse Equation* v1.3, *The Direction Problem* preprint v1.1, `te-controfase` in the ecosystem, and the five sections reconciled with the vault, which the canonical editions published here carry. The 1.3.0 editions of Bootloader 7.1, Protocols 1.0 and Core 5.1 (content 5.2) are in `FRAMEWORKS/ARCHIVE/`; the current editions are 7.1.1, 1.1 and 5.2.1; the Symbol Canon is `FRAMEWORKS/TE_SYMBOL_CANON_v1_0_EN.md`.

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
