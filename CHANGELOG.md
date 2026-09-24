# Changelog

All notable changes to this repository should be documented in this file.

The format is inspired by Keep a Changelog and semantic versioning principles for documentation releases.

> **Note**: This changelog was added on 2026-05-06. Entries before that date are reconstructed retrospectively from git history; full diff context lives in `git log`. Future entries are written at the time of the change.

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
- `docs/CORE/`, `docs/MODULES/`, `docs/OST/` → `FRAMEWORKS/` (current editions) and `FRAMEWORKS/ARCHIVE/` (superseded: Bootloader 6.0, 7.0, 7.1; Core 5.1; Protocols 1.0; the OST guide and Teleodynamics extension under their previous file names). `docs/` keeps `ArXiv_Abstract_TE.md`.

### Notes
- Major version: the repository layout changes (flat `FRAMEWORKS/` replaces `docs/CORE|MODULES|OST`) and two domain frameworks with runtimes are added.
- The division of work between each runtime and the signing professional is stated in `README.md` §Domain frameworks and in the compatibility profiles.
- On macOS the CASEWORK tests need a temporary directory that resolves to itself (a real directory; for example `mkdir -p tmp && TMPDIR=$PWD/tmp python -m unittest …`), because the runtime requires source paths that resolve to themselves; see `FRAMEWORKS/CASEWORK/README.md`.
- Both runtimes were exercised end to end from the repository root with the commands printed in their READMEs (`prepare` → `validate` on synthetic input) before this release.
- The OCT validation corpus is published in `te-oct-framework-en`; that mirror keeps its historical file-naming convention and points here for LEXX and CASEWORK.
- Register (2026-09-24): the published documents and the user-facing strings of both runtimes (help texts, messages, report `limits`, draft placeholders) state facts and assignments of function in the positive form; each limit is stated once, in its home (the README status lines, the compatibility profiles, the protocol sections), and the other files point to it.

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
