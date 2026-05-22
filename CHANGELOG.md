# Changelog

Version history of the Ordinative Sciences Framework (TE).

Document versions are recorded **here**, not embedded in filenames, so that
links, citations, and the Zenodo DOI remain stable across releases. Each
operative document also carries its own version in its front matter / header.

The format is loosely based on [Keep a Changelog](https://keepachangelog.com/).

## [Unreleased]

### Changed — repository reorganization

The `docs/` tree was reorganized for navigability. Operative documents are now
grouped under `docs/framework/`, version numbers and the `_EN` suffix were
removed from filenames (versions live in this changelog), and the manual/book
folders were lowercased. File **history is preserved** (`git mv`).

Path / filename migration map:

| Before | After | Version at move |
| --- | --- | --- |
| `docs/CORE/TE_CORE_v5_1_EN.md` | `docs/framework/core/TE_CORE.md` | v5.1 |
| `docs/CORE/TE_BOOTLOADER_v6_0_EN.md` | `docs/framework/core/TE_BOOTLOADER.md` | v6.0 |
| `docs/OST/Ordinative_Set_Theory_OST_A_Concise_Guide_For_AI_v2_1.md` | `docs/framework/ost/OST_Concise_Guide.md` | v2.1 |
| `docs/OST/OST_Extension_Teleodynamics_Causal_Inversion_v1_1.md` | `docs/framework/ost/OST_Teleodynamics_Causal_Inversion.md` | v1.1 |
| `docs/MODULES/TE_MODULE_SVP_v5_1_EN.md` | `docs/framework/modules/TE_MODULE_SVP.md` | v5.1 |
| `docs/MODULES/TE_MODULE_LENS_v5_1_EN.md` | `docs/framework/modules/TE_MODULE_LENS.md` | v5.1 |
| `docs/MODULES/TE_MODULE_VERI_v1_0_EN.md` | `docs/framework/modules/TE_MODULE_VERI.md` | v1.0 |
| `docs/MODULES/TE_MODULE_PPRO_v5_2_EN.md` | `docs/framework/modules/TE_MODULE_PPRO.md` | v5.2 |
| `docs/MODULES/TE_MODULE_SCIMS_v5_1_EN.md` | `docs/framework/modules/TE_MODULE_SCIMS.md` | v5.1 |
| `docs/MODULES/TE_OBSERVER_v1_1_EN.md` | `docs/framework/modules/TE_OBSERVER.md` | v1.1 |
| `docs/MANUAL/` | `docs/manual/` (subfolders `IT/EN` → `it/en`) | — |
| `docs/BOOK/` | `docs/book/` (subfolders `IT/EN` → `it/en`) | — |
| `docs/ArXiv_Abstract_TE.md` | `docs/papers/arxiv-abstract-te.md` | — |

### Added

- `LICENSE` (MIT) — previously referenced by `README.md` and `CITATION.cff` but missing.
- `CHANGELOG.md` — this file.
- `docs/README.md` — documentation map / navigation hub.

### Removed

- Empty placeholder sub-folders under the manual (`01-propaedeutics`, `03-ost`,
  `04-arajat`, `05-controphase`, `06-modules`, `07-practice`, `99-appendix` and
  Italian equivalents). The intended layout is documented in `docs/manual/README.md`;
  folders are created when their first chapter is written.

## Document versions (current)

| Document | Version |
| --- | --- |
| TE_CORE | 5.1 |
| TE_BOOTLOADER | 6.0 |
| OST Concise Guide | 2.1 |
| OST Teleodynamics / Causal Inversion | 1.1 |
| TE_MODULE_SVP | 5.1 |
| TE_MODULE_LENS | 5.1 |
| TE_MODULE_VERI | 1.0 |
| TE_MODULE_PPRO | 5.2 |
| TE_MODULE_SCIMS | 5.1 |
| TE_OBSERVER | 1.1 |
