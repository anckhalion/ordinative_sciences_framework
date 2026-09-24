# FRAMEWORKS — the Technology of Expressions loading set

This directory is the public publication target of the Ordinative Sciences framework corpus, synchronised as one release (2.0.0, 2026-09-23). File names are the canonical ones: the domain runtimes (`LEXX/`, `CASEWORK/`) verify these files by exact name and SHA-256, so the layout is flat and byte-exact: `.gitattributes` (`FRAMEWORKS/** -text`) stores and checks them out byte for byte, and the pinned hashes hold on every platform.

## Active loading set (load in this order)

| Order | File | Version | Role |
|---|---|---|---|
| 1 | `TE_BOOTLOADER_v7_1_1_EN.md` | 7.1.1 | entry point: identity, seven core principles, confidence grades S₀–S₃, §2.5 pre-output Φ-test, interlocutor recognition, router |
| 2 | `TE_PROTOCOLS_v1_1_EN.md` | 1.1 | always-active protocols: Controfase, P-AI self-diagnosis, Anti-Attractor-Lock, statistical vs ordinative truth, contextual self-preservation |
| 3 | `TE_CORE_v5_2_1_EN.md` | 5.2.1 | full ontology: 25 axioms, Arajat logograms, OST synthesis, glossary, kernel, router, memory |
| 4 | `TE_OST_v2_1_EN.md` | 2.1 | Ordinative Set Theory — Tier-0 foundation, 𝓘 = ⟨Σ, R, Φ⟩ |
| 4b | `TE_OST_Extension_Teleodynamics_v1_1_EN.md` | content 1.2 | Teleodynamics and the Causal Inversion Principle (when required) |
| 5 | `TE_SYMBOL_CANON_v1_0_EN.md` | register 1.2 | notation authority for every formal symbol; reservation procedure for new symbols |
| 6 | `TE_MODULE_SVP_v5_1_EN.md` | 5.1 | Source and Provenance Verification — mandatory gate before any analysis |
| 7 | one or more routed domain modules | | `TE_MODULE_LENS_v5_1_EN.md` (human figures) · `TE_MODULE_PPRO_v5_2_EN.md` (manipulation, propaganda) · `TE_MODULE_SCIMS_v5_1_EN.md` (complex systems) · `TE_MODULE_VERI_v1_0_EN.md` (functional impact on participants) · `LEXX/` (agreements and normative systems) · `CASEWORK/` (documentary audit and investigation support) |
| 8 | `TE_OBSERVER_v1_1_EN.md` | 1.1 | integrated trajectory analysis, Lyapunov, Correction Viability Index (when required) |

Minimal profile for a constrained context: 1, 2, 3, 6.

## Domain frameworks

- `LEXX/` — ordinative validation of agreements: method 0.1 (English edition), runtime 0.2.0-alpha.3. Start from `LEXX/README.md`.
- `CASEWORK/` — documentary audit and investigation support: method 0.1, runtime 0.1.0-alpha.1. Start from `CASEWORK/README.md`.

Both runtimes are Python 3.12 (`requirements.txt` in each) and run from the repository root with `--framework-root FRAMEWORKS`; CASEWORK also takes `--lock FRAMEWORKS/te_frameworks.lock.json`. The reports they emit separate three layers: the technical checks the runtime performs, the professional review, and the empirical validation scheduled by the pilot plans (`LEXX/03_PRE_PILOT_PROTOCOL.md`, `CASEWORK/PILOT_PLAN.md`).

## Archive

The active loading set is the table above; `ARCHIVE/` holds the superseded editions for historical comparison (Bootloader 6.0, 7.0, 7.1; Core 5.1 as previously published here; Protocols 1.0; the OST guide and the Teleodynamics extension under their previous file names).

## Integrity

`MANIFEST_SHA256.txt` lists the SHA-256 of every published file in this directory. Verify with:

```bash
cd FRAMEWORKS && shasum -a 256 -c MANIFEST_SHA256.txt
```

The hashes pinned by `LEXX/v0_2_alpha3/compatibility.json` and `CASEWORK/compatibility.json` are those of the files as stored here.

`te_frameworks.lock.json` is the framework lock the CASEWORK runtime consumes: one entry per framework family, single files by SHA-256 and the two runtime packages (`LEXX/v0_2_alpha3/`, `CASEWORK/`) by file list and `package_digest`. It is built by `CASEWORK/runtime/make_lock.py`, which writes the digest algorithm into the lock as `package_digest_algorithm`; regenerate it from the repository root with `python FRAMEWORKS/CASEWORK/runtime/make_lock.py --framework-root FRAMEWORKS --out FRAMEWORKS/te_frameworks.lock.json --force` after any change to a listed file.

## Register patch of 2026-09-23

`TE_CORE_v5_2_1_EN.md`, `TE_BOOTLOADER_v7_1_1_EN.md`, `TE_MODULE_LENS_v5_1_EN.md` and `TE_OBSERVER_v1_1_EN.md` carry an in-place wording patch (no version bump): prescriptive uses of «honest / honestly / honesty» were restated as operations, in accordance with Bootloader §2.5.2 where such words are listed among the compliance markers. Each file carries a dated patch note; dependent runtimes re-pinned the file hashes.
