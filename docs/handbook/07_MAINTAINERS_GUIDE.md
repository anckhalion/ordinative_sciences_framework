# Maintainers' guide

How the repository is organised, what is generated from what, and the procedure for a release. Written for whoever changes a file here.

## Principles

1. **`FRAMEWORKS/` is canonical and byte-exact.** The framework corpus is maintained in the author's canonical corpus and published here as one synchronised release. The files are stored with `-text` (no line-ending conversion), hashed in `MANIFEST_SHA256.txt`, and pinned by the runtimes. Updates flow from the canonical corpus to the repository, never the reverse (`TE_SYMBOL_CANON` header, master-copy rule).
2. **Everything else is derived or supporting.** `dist/`, `llms.txt`, the manifest and the lock are generated; the handbook explains; the tools build and check. None of it restates the doctrine.
3. **A change is complete when `make check` is green.** The check fails on any drift between the canonical files and what depends on them.

## Layout and provenance

| Path | Kind | Produced by | Consumed by |
|---|---|---|---|
| `FRAMEWORKS/TE_*.md`, `LEXX/`, `CASEWORK/`, `ARCHIVE/` | canonical | the author's corpus | models, humans, the runtimes (by hash) |
| `FRAMEWORKS/README.md` | repository documentation | maintainers | humans |
| `FRAMEWORKS/MANIFEST_SHA256.txt` | generated | `make manifest` (`tools/build_dist.py --write-manifest`) | `shasum -c`, `make check` |
| `FRAMEWORKS/te_frameworks.lock.json` | generated | `make lock` (`CASEWORK/runtime/make_lock.py`) | the CASEWORK runtime (`--lock`), `tools/build_dist.py` (versions), `make check` |
| `FRAMEWORKS/LEXX/v0_2_alpha3/compatibility.json`, `FRAMEWORKS/CASEWORK/compatibility.json` | canonical, hand-pinned | the runtime's compatibility review | the runtimes, `make check` |
| `FRAMEWORKS/LEXX/v0_2_alpha3/schemas/*.json`, `FRAMEWORKS/CASEWORK/schemas/*.json` | generated | `build_schema.py`, `casework_schema.py` | the runtimes; the tests compare them with the builders |
| `tools/loading_set.json` | configuration | maintainers | `tools/build_dist.py` |
| `dist/*` | generated | `make dist` (`tools/build_dist.py`) | downloads, models, `make check` |
| `llms.txt` | generated | `make dist` | LLM tools |
| `docs/` | supporting | maintainers | humans |
| `.github/workflows/ci.yml`, `release.yml` | automation | maintainers | GitHub Actions |

## Commands

```bash
make test       # the LEXX (40) and CASEWORK (42) test suites; needs pip install -r FRAMEWORKS/CASEWORK/requirements.txt
make check      # manifest, lock, compatibility profiles, derived files, handbook files, Markdown links
make dist       # rebuild dist/ and llms.txt
make manifest   # regenerate FRAMEWORKS/MANIFEST_SHA256.txt
make lock       # regenerate FRAMEWORKS/te_frameworks.lock.json
make package    # build dist/te-frameworks-<version>.zip (not committed)
```

Without `make`: the commands are the one-liners in the `Makefile`, all `python3 tools/…` or `python3 FRAMEWORKS/CASEWORK/runtime/make_lock.py …`.

`tools/check_repo.py` reports a broken relative link inside `FRAMEWORKS/` as a warning rather than a failure, because canonical files change only with a release; everywhere else a broken link fails the check.

## Release procedure

Follow the order; each step's output is the next step's input.

1. **Update the canonical files** in `FRAMEWORKS/` from the canonical corpus. New editions take their canonical file names; superseded editions move to `ARCHIVE/`. Update `FRAMEWORKS/README.md` (loading table, archive list, register patches).
2. **If a file in the lock changed, regenerate the lock**: `make lock`. Then **re-pin the compatibility profiles** by hand: the SHA-256 of each single-file dependency in `LEXX/v0_2_alpha3/compatibility.json`, and the `digest` of each family in `CASEWORK/compatibility.json` (single files: the file hash; `TE_MODULE_LEXX`: the `package_digest` of the LEXX runtime package from the lock). This is a compatibility review, not a mechanical step: the runtime's authors state that a newer dependency requires review before the pin moves. Note that `make_lock.py` reads the family versions from `CASEWORK/compatibility.json`, so a version bump goes into the profile first and into the lock second, and that the `TE_CASEWORK` package includes its own `compatibility.json`, so its family digest changes when the profile changes (the profile does not pin its own family, so nothing else moves).
3. **Regenerate the manifest**: `make manifest`.
4. **Update the static metadata if the loading set changed**: `tools/loading_set.json` (order, roles, triggers, profiles, reference resolution, handbook list) and `make_lock.py`'s `FAMILY_PATHS` for a new family.
5. **Rebuild the derived layer**: `make dist`. Inspect the diff of `dist/README.md` and `llms.txt`.
6. **Update the release metadata**: `CITATION.cff` (`version`, `date-released`; `tools/build_dist.py` reads them), `CHANGELOG.md` (move `[Unreleased]` to the version), `README.md` where it states the release.
7. **Run everything**: `make test && make check`.
8. **Update the handbook** where the change affects it: module guides, glossary, the smoke test's expected answers, the training path's section references.
9. **Commit, tag `vX.Y.Z`, push.** The release workflow rebuilds the package and attaches `te-frameworks-X.Y.Z.zip` to the GitHub release.

A change to the handbook, the tools or the workflows alone needs steps 5 (if the handbook list in `loading_set.json` changed), 7 and a `CHANGELOG.md` entry.

## Versioning conventions

- The **family version** (7.1.1, 1.1, 5.2.1, 2.1, 1.2, 1.2, 5.1, …) lives in the lock and in each file's header; it is the version quoted in the compatibility profiles.
- The **file-name version** is the version at which the file was named; it stays when an in-place patch advances the content, to avoid churning cross-references. Two files currently differ (Symbol Canon, Teleodynamics); `tools/loading_set.json` records the `version_note`, and the catalog prints both.
- A **register patch** is a wording-only change without a version bump, with a dated note in the file; hashes change and the profiles are re-pinned.
- The **repository release** (`CITATION.cff`, `CHANGELOG.md`) is semantic: major for a layout change or a new framework family, minor for additions, patch for fixes and documentation.

## Adding a document or a module

1. Add the file to `FRAMEWORKS/` under its canonical name; add the family to `make_lock.py` (`FAMILY_PATHS`) and to `CASEWORK/compatibility.json` if the runtime is to pin it (the lock takes its version from there); regenerate the lock and the manifest.
2. Add the document to `tools/loading_set.json` (`documents`, in loading order, with tier, load mode, role, triggers, prerequisites) and to the profiles that should carry it; rebuild `dist/`.
3. Register the routing in the canonical Bootloader and Core through the author's corpus (those are canonical files).
4. Add the row to `FRAMEWORKS/README.md`, a module guide under `docs/handbook/modules/`, the glossary entries, and the `CHANGELOG.md` entry.

## Continuous integration

`ci.yml` runs on every push and pull request: Python 3.12, the pinned requirements, `make test`, `make check`. `release.yml` runs on a `v*` tag: the same, then `make package` and the upload of the archive to the release (`gh release create` or `upload`). Both use only the repository's own scripts, so a failure in CI reproduces locally with the same commands.

## Open items found in the review of 2026-09-25

Recorded here so that they reach the canonical corpus; none of them was changed in the published framework files, which stay byte-identical to release 2.0.0.

1. **Manifest drift (fixed in the repository).** `FRAMEWORKS/MANIFEST_SHA256.txt` listed the pre-patch hash of `CASEWORK/README.md` (the commit "acquisition authority is verified by the case owner" changed the file without regenerating the manifest). The manifest was regenerated; the lock and the profiles were unaffected because Markdown is excluded from package digests.
2. **Missing `LICENSE` (fixed).** `README.md` referred to a `LICENSE` file that was not in the repository; an MIT license file was added, with the papers' CC BY 4.0 stated in the README.
3. **Stale section references inside canonical files.** `TE_CORE §6.0` cites "Bootloader v6.0, Section [6]" for interlocutor recognition (now `TE_BOOTLOADER §3`); `TE_CORE §0.2` and `TE_OBSERVER §1.4` say P-AI is "integrated in Bootloader v6.0" (now `TE_PROTOCOLS §2`, `TE_MODULE_PPRO §14`); `TE_MODULE_PPRO §3.4` cites "Bootloader v6.0, Section [5]" for confidence preservation (now `TE_BOOTLOADER §2`); `TE_CORE §8.2` lists P-AI as "Integrated in Bootloader v6.0". The Protocols' own policy is to resolve historical references by family through the lock; the bundle headers and `catalog.json` carry a resolution table, and the next edition of these files could update the section numbers.
4. **Historical profile paths.** `FRAMEWORKS/LEXX/lexx_compatibility_profile_v0_1.json` (`mandatory_stack`) and `02_COMPATIBILITY_PROFILE.md §2` name `../TE_BOOTLOADER_v7_1_EN.md`, `../TE_PROTOCOLS_v1_0_EN.md` and `../TE_CORE_v5_1_EN.md`, which are now in `ARCHIVE/`. Both documents are dated 2026-09-16 and point to `v0_2_alpha3/compatibility.json` as the current profile, so they are consistent as historical records; a reader may still take the paths literally.
5. **Platform-specific wording in the kernel.** The router in `TE_BOOTLOADER §6` and `TE_CORE §8.4` says "search project knowledge" / `project_knowledge_search(...)`, and `TE_BOOTLOADER §0` recognises the author by name as Hypervisor "in this project context". Both are correct for the author's sessions and need a resolution note for other deployments; the bundle headers provide it for the first, the handbook (`01_CORE_CONCEPTS §11`) for the second. An edition with a one-line "deployment context" clause would remove the need.
6. **Version-history weight in operational files.** Version notes and future-work sections occupy about a quarter of the Bootloader (`§8–§9`, lines 237–329 of 345) and sizeable tails of the Core, SVP, LENS, VERI, PPRO, SCIMS and OBSERVER. They are valuable as a record and cost tokens on every load. A future edition could move history to a changelog file in the corpus and keep a one-line pointer, or the build could offer a "lean" profile that omits those sections by an explicit list; the second was not done here because deciding what is operational is the author's call.
7. **Minor.** `CITATION.cff` cites *The Collapse Equation* as version 1.2-beta while the repository publishes v1.3 (the DOI is the v1.2 deposit, so this may be intended); `papers/collapse_equation/README.md` gives the APA citation as v1.2-beta under a v1.3 header; the archive file `ARCHIVE/OST_Extension_Teleodynamics_Causal_Inversion_v1_1.md` is byte-identical to the active `TE_OST_Extension_Teleodynamics_v1_1_EN.md` (same hash), so the archive entry documents a rename rather than a superseded edition.
