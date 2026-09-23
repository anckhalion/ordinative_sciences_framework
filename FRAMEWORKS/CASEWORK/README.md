# TE CASEWORK — Analysis, Audit and Investigative Support

Method **0.1**, runtime **0.1.0-alpha.1**. A native package of the Technology of Expressions: it introduces no ontology, formal algebra or legal authority of its own.

## What is ready

- `TE_CASEWORK_v0_1_EN.md`: the shared discipline of evidence, coverage, sources, confidence and review.
- `TE_AUDIT_v0_1_EN.md`: organizational analysis with a mandatory audit pass; relevance is decided only after the first wave.
- `TE_INVESTIGATION_v0_1_EN.md`: investigative support, including the defensive profile, under a case-specific mandate.
- Strict JSON schemas and commands to prepare a dossier, check the registers and request a review bound to the hashes.

The runtime performs no automatic reading or interpretation of the pile of papers: it prepares copies and an inventory, and it checks the work that analyst and reviewer record. It contains no OCR, no Office/PDF extractors, no automatic accounting reconciliation, no fraud-discovery engine, no online collection and no investigative acts. Non-textual documents require verified extractions, with the originals preserved.

A passing test suite certifies none of the following: empirical effectiveness, truth of the facts, independence of the sources, lawfulness of the acquisitions, usability in proceedings. Investigations remain documentary support; the professional review of the penal profile and the field trials are still to be carried out (`release.json`: `empirical_runs_completed: 0`).

## Before use

Define mandate, access, purpose, owner, analyst and retention. Use only an explicitly authorized input folder and an environment appropriate to the confidentiality of the case. This prototype configures neither encryption nor permissions: a development folder is not automatically suitable for confidential case files. The example below is **synthetic only**.

**Environment.** The pilot environment uses Python 3.12; `requirements.txt` pins `jsonschema` 4.26.0 and its dependencies. From a clone of the repository:

```bash
git clone <repository-url> te-frameworks
cd te-frameworks
python3 -m venv .venv && source .venv/bin/activate    # Windows: .venv\Scripts\activate
pip install -r FRAMEWORKS/CASEWORK/requirements.txt
```

**Framework root and lock.** The `prepare` command takes `--framework-root`, the directory that holds the framework files, and `--lock`, the inventory `te_frameworks.lock.json` that binds every framework file to its SHA-256. `FRAMEWORKS/`, at the repository root, is the framework root. The code reads three paths at fixed positions under it — `CASEWORK/compatibility.json`, `CASEWORK/runtime/casework.py`, `CASEWORK/runtime/casework_schema.py` — and the two scripts must hash-match the lock; the script actually executing is compared with the lock as well (`Executing runtime differs from snapshot` otherwise). Every family pinned in `CASEWORK/compatibility.json` must be present at the exact version and digest:

- TE_BOOTLOADER 7.1.1 → `TE_BOOTLOADER_v7_1_1_EN.md`
- TE_PROTOCOLS 1.1 → `TE_PROTOCOLS_v1_1_EN.md`
- TE_CORE 5.2.1 → `TE_CORE_v5_2_1_EN.md`
- TE_OST 2.1 → `TE_OST_v2_1_EN.md`
- TE_OST_TELEODYNAMICS 1.2 → `TE_OST_Extension_Teleodynamics_v1_1_EN.md`
- TE_SYMBOL_CANON 1.2 → `TE_SYMBOL_CANON_v1_0_EN.md`
- TE_MODULE_SVP 5.1 → `TE_MODULE_SVP_v5_1_EN.md`
- TE_MODULE_LENS 5.1 → `TE_MODULE_LENS_v5_1_EN.md`
- TE_MODULE_PPRO 5.2 → `TE_MODULE_PPRO_v5_2_EN.md`
- TE_MODULE_SCIMS 5.1 → `TE_MODULE_SCIMS_v5_1_EN.md`
- TE_MODULE_VERI 1.0 → `TE_MODULE_VERI_v1_0_EN.md`
- TE_OBSERVER 1.1 → `TE_OBSERVER_v1_1_EN.md`
- TE_MODULE_LEXX 0.2.0-alpha.3 → the `LEXX/v0_2_alpha3/` package (code, schemas, tests and configuration), declared as a multi-file family

In addition, the lock carries a `TE_CASEWORK` package family (version 0.1.0-alpha.1: the `CASEWORK/` package itself — code, schemas, tests and configuration — so that the runtime is frozen with each run) whose `files` include `CASEWORK/runtime/casework.py` and `CASEWORK/runtime/casework_schema.py`; `verify_frameworks` looks those two paths up in the lock, and `compatibility.json` does not pin the family.

The lock has one entry per family. A single-file family carries `snapshot_path` and `sha256`; a package carries `files` (each with `relative_path` and `sha256`) and `package_digest`:

```json
{
  "families": {
    "TE_CORE": {"version": "5.2.1", "snapshot_path": "TE_CORE_v5_2_1_EN.md", "sha256": "<sha256 of the file>"},
    "TE_MODULE_LEXX": {"version": "0.2.0-alpha.3", "package_digest": "<digest pinned in CASEWORK/compatibility.json>",
                       "files": [{"relative_path": "LEXX/v0_2_alpha3/runtime/validate_lexx_output.py", "sha256": "<sha256 of the file>"}]},
    "TE_CASEWORK": {"version": "0.1.0-alpha.1",
                    "files": [{"relative_path": "CASEWORK/runtime/casework.py", "sha256": "<sha256 of the file>"}]}
  }
}
```

The runtime checks that every listed path exists under the framework root with the listed SHA-256 (`Framework hash mismatch`), that every dependency in `compatibility.json` has a lock family with the same `version` and with `sha256` or `package_digest` equal to its `digest` (`Unreviewed dependency version` / `Unreviewed dependency content`), and that no snapshot path is listed twice. A run freezes exactly the files the lock lists into `<run>/frameworks/`, together with the lock itself. `FRAMEWORKS/te_frameworks.lock.json` ships with the release, generated against the published bytes by `CASEWORK/runtime/make_lock.py`, which also declares the digest algorithm: `package_digest` is the SHA-256 of the UTF-8 text made of one line per file, `<relative_path>  <sha256>`, sorted by path in byte order. A package covers code, schemas, tests and configuration; Markdown documentation is excluded, so the digest is the same wherever the runtime bytes are the same. Regenerate the lock from the repository root with `python FRAMEWORKS/CASEWORK/runtime/make_lock.py --framework-root FRAMEWORKS --out FRAMEWORKS/te_frameworks.lock.json --force`; any change to a listed file requires a regenerated lock, an updated digest in `compatibility.json` where the family is pinned, and a compatibility review.

**Preparing a run.** From the repository root, with the environment active:

```bash
python FRAMEWORKS/CASEWORK/runtime/casework.py prepare \
  --source-dir path/to/authorized_input \
  --run-dir runs/case_01 \
  --framework-root FRAMEWORKS \
  --lock FRAMEWORKS/te_frameworks.lock.json \
  --case-id DEMO-AUDIT \
  --purpose "Synthetic technical test" \
  --scope "Synthetic documents in the named folder only" \
  --owner "Demo owner" \
  --analyst "Demo analyst" \
  --acquisition-authority-ref "Synthetic materials created for the test" \
  --mode audit \
  --jurisdiction IT \
  --synthetic
```

`--source-dir`, `--run-dir`, `--framework-root`, `--lock`, `--case-id`, `--purpose`, `--scope`, `--owner`, `--analyst`, `--acquisition-authority-ref`, `--jurisdiction` and `--mode` (`audit` or `investigation`) are all required. `--investigation-mandate-ref` and `--supervising-role` default to empty and are mandatory in investigation mode. `--synthetic` is a flag that records `synthetic: true` in the manifest. On Windows write the command on one line. Success prints `{"prepared": "runs/case_01", "analysis": "not_started"}`; every refusal prints `Casework blocked: <reason>` and exits with status 1.

The destination must be new and outside the source (`Destination exists; use a new run directory`, `Run directory cannot be inside source`). The command creates `originals/` (one `DOC-nnnnn.bin` per acquired file), `derived/`, the `frameworks/` snapshot, `te_frameworks.lock.json`, `manifest.json` and `case.json`. It records the Python and jsonschema versions and checks them at every later execution (`Recorded Python/jsonschema environment differs; reproduce it or prepare a reviewed new run`); hermetic isolation is outside its scope. The manifest appears only after every copy has succeeded and re-hashed. An interrupted preparation leaves an incomplete packet, to be treated as an unfinished acquisition: resolve the cause and use a new run. The enumeration raises on inaccessible subfolders and refuses links and reparse points, in the source tree and among the ancestors of both the source and the run directory. On macOS `/tmp` and `/var` are symlinks, so both source and run directory need a real path; for cloud-synced files carrying such attributes prepare a suitable local source. The check is a boundary, to be satisfied and never bypassed.

## Compilation and checking

1. Read the current protocols. Use `case.json` to record the state of every document (`reading`: `pending`, `read`, `unreadable`, `restricted`). Keep `wave1_complete=false` while any element is `pending`; no relevance can be decided before that boundary (`relevance` stays `deferred`).
2. At the end of the first wave, give reasons for provisional inclusions and exclusions (`include` or `exclude_provisional`, each with `relevance_reason`). An unreadable document is recorded as a limitation; the validator refuses `exclude_provisional` for any document whose reading is `unreadable` or `restricted`.
3. Record separate extractions (`derivatives`, stored under `derived/` with method, operator, time and hash), literal quotations (`evidence`: each `quote` must occur verbatim in the original or in the declared derivative), origin groups (`source_group`), gaps, chronology, relationships and analysis. Leave originals, snapshot and manifest untouched. The hash detects changes relative to the packet; who created the packet is outside what a hash can establish.
4. Complete the applicable audit areas (audit mode: `source_integrity`, `finance`, `procurement`, `authorizations`, `governance`, `people_internal_abuse`, `assets_resources`, `information_reporting`; investigation mode: `source_integrity`, `chronology`, `attribution`, `counterevidence`), giving reasons for tests, examined populations, results and limits. Findings require supporting evidence, at least one alternative explanation with a discriminating test, a counter-evidence search and next steps; a finding's confidence (S1–S3) never exceeds its weakest supporting premise, and S1 requires at least two declared origin groups. A `legal_question` criterion requires an entry in `legal_references`.
5. Run the validator and have the dossier reviewed by a distinct reviewer. To reopen or revise, keep a copy of the previous case revision and of its report; the software keeps no immutable historical register.

```bash
python runs/case_01/frameworks/CASEWORK/runtime/casework.py validate --run-dir runs/case_01
python runs/case_01/frameworks/CASEWORK/runtime/casework.py review-request --run-dir runs/case_01
```

The second command validates the run first, then writes `review_request.json` with `decision: pending` and every check `pending`; a positive review is the reviewer's separate act. The file is written once (`File exists` on a second call): move or delete the previous request to issue another. After the reviewer has actually filled it in (`reviewer`, `reviewer_role`, `decision`, `rationale`, `reviewed_at`, the five checks), pass it with `--review` to the validator. Any change to `case.json` or `manifest.json` invalidates the receipt (`Review invalidated by changed case/manifest`). An `accept` decision requires a completed audit pass and all five checks at `accept`; the reviewer must differ from the analyst named in the manifest. The reviewer's identity is recorded as declared; the runtime performs no authentication and cannot establish independence or professional qualification.

The report printed by `validate` carries these fields. Field identifiers are canonical and language-independent; they match the runtime schema.

- `technical_status`: `TECHNICALLY_CHECKED` — the technical checks passed on the declared records; a failed check prints `Casework blocked: <reason>` and no report.
- `phase`: `wave1` (elements still `pending`), `relevance_and_analysis` (wave closed, analysis open), `audit_required` (analysis complete, audit pass due), `independent_review_required` (audit complete, no accepted review bound to the current hashes), `documentary_pass_review_recorded` (an `accept` review bound to the current hashes).
- `coverage`: `declared_accessible_pass_only` when every document is `read`, no check is `pending`, `not_testable` or `inconclusive`, no limitation is declared and no gap is open; `limited_or_pending` otherwise.
- `review`: `not_recorded` (no `--review` passed), `pending`, `revise`, or `accept_recorded_identity_unverified`.
- `document_count`, `finding_count`, `case_sha256`, `manifest_sha256`: the counts and the hashes the review receipt binds to.
- `empirical_performance`: `not_assessed` in every report. `legal_use`: `not_authorized_by_runtime` in every report, with or without a recorded review.
- `limits`: three fixed sentences in every report — "Checks validate declared records, not truth, actual reading, independent origin or lawful authority", "No immutable custody log, trusted timestamp, encryption or access control is implemented", "No automated OCR, fraud detection, professional opinion or absence-of-wrongdoing verdict".

The `audit_required` phase is computed automatically once the analysis is complete. It means the audit pass is now due; no engine performs it. The routing in the prompt is an operating instruction; the mechanical check happens only when the command runs.

## Investigative mode

Use a new run with `--mode investigation`, `--investigation-mandate-ref` and `--supervising-role` stated explicitly (`Explicit investigative mandate and supervising role required` otherwise). Leave the manifest of an already acquired audit as it is; an investigative mandate needs its own run. The mode can be invoked directly, with no prior organizational audit. Closure requires competing hypotheses (`hypotheses`, at least two), including at least one of kind `non_criminal` or `exculpatory`, each with counter-evidence and discriminating checks (`Investigation requires competing and non-criminal/exculpatory hypotheses` otherwise).

No contact with witnesses, system access, filing, external communication or procedural act is executed or authorized by this mode. `legal_use` remains `not_authorized_by_runtime`, with a recorded review as well. The Italian jurisdiction profile in `TE_INVESTIGATION_v0_1_EN.md` §4 is a map of references to be re-examined by a qualified reviewer before any penal use.

## Tests

```bash
cd FRAMEWORKS/CASEWORK
python -m unittest discover -s tests -v
```

The suite has 42 tests. On macOS set `TMPDIR` to a directory whose path contains no symlink (for example `mkdir -p tmp && TMPDIR=$PWD/tmp python -m unittest discover -s tests -v`): the default temporary directory sits under `/var`, a symlink to `/private/var`, and the runtime refuses symlinked ancestors. The JSON schemas in `schemas/` are generated by `python runtime/casework_schema.py`; `test_schema_generation_reproducible` checks that the committed files match the code.

The tests are synthetic and verify software constraints. The correct and suspicious cases they contain are records already filled in: they measure nothing about a model's ability to discover them. The empirical plan is in `PILOT_PLAN.md`.
