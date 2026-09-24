# TE CASEWORK — Analysis, Audit and Investigative Support

Method **0.1**, runtime **0.1.0-alpha.1**. A native package of the Technology of Expressions.

## What is ready

- `TE_CASEWORK_v0_1_EN.md`: the shared discipline of evidence, coverage, sources, confidence and review.
- `TE_AUDIT_v0_1_EN.md`: organisational analysis with a mandatory audit pass; relevance is decided after the first wave.
- `TE_INVESTIGATION_v0_1_EN.md`: investigative support, including the defensive profile, under a case-specific mandate.
- Strict JSON schemas and commands to prepare a dossier, check the registers and request a review bound to the hashes.

The runtime prepares copies and an inventory and checks the work that analyst and reviewer record; reading, extraction and reconciliation are the analyst's, recorded in the run; collection and investigative acts belong to the persons the mandate names (`TE_CASEWORK_v0_1_EN.md` §2). Scanned, image and office documents enter the analysis through verified extractions, with the originals preserved.

A passing test suite certifies that the software constraints hold on the recorded state. Effectiveness is measured by the pilot; truth of the facts and independence of the sources are established by analyst and reviewer; the authority for each acquisition is verified by the case owner (`TE_CASEWORK_v0_1_EN.md` §6); use in proceedings is decided by counsel. Investigations are documentary support. Status: runtime 0.1.0-alpha.1; the 42 tests run on synthetic material; the professional review of the penal profile and the field trials are the next two steps (`PILOT_PLAN.md`; `release.json`: `empirical_runs_completed: 0`).

## Before use

Define mandate, access, purpose, owner, analyst and retention. Use an explicitly authorised input folder and an environment appropriate to the confidentiality of the case; the environment provides encryption, permissions and custody (`TE_CASEWORK_v0_1_EN.md` §2). The example below runs on synthetic material.

**Environment.** The pilot environment uses Python 3.12; `requirements.txt` pins `jsonschema` 4.26.0 and its dependencies. From a clone of the repository:

```bash
git clone <repository-url> te-frameworks
cd te-frameworks
python3 -m venv .venv && source .venv/bin/activate    # Windows: .venv\Scripts\activate
pip install -r FRAMEWORKS/CASEWORK/requirements.txt
```

**Framework root and lock.** The `prepare` command takes `--framework-root`, the directory that holds the framework files, and `--lock`, the inventory `te_frameworks.lock.json` that binds every framework file to its SHA-256. `FRAMEWORKS/`, at the repository root, is the framework root. The code reads three paths at fixed positions under it — `CASEWORK/compatibility.json`, `CASEWORK/runtime/casework.py`, `CASEWORK/runtime/casework_schema.py` — and the two scripts must hash-match the lock; the executing script is compared with the lock as well (`Executing runtime differs from snapshot` otherwise). Every family pinned in `CASEWORK/compatibility.json` must be present at the exact version and digest:

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
- TE_MODULE_LEXX 0.2.0-alpha.3 → the `LEXX/v0_2_alpha3/` package (code, schemas, tests and configuration), listed as a multi-file family

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

The runtime checks that every listed path exists under the framework root with the listed SHA-256 (`Framework hash mismatch`), that every dependency in `compatibility.json` has a lock family with the same `version` and with `sha256` or `package_digest` equal to its `digest` (`Dependency version differs from the reviewed compatibility profile` / `Dependency digest differs from the reviewed compatibility profile`), and that every snapshot path is listed once. A run freezes exactly the files the lock lists into `<run>/frameworks/`, together with the lock itself. `FRAMEWORKS/te_frameworks.lock.json` ships with the release, generated against the published bytes by `CASEWORK/runtime/make_lock.py`, which also states the digest algorithm: `package_digest` is the SHA-256 of the UTF-8 text made of one line per file, `<relative_path>  <sha256>`, sorted by path in byte order. A package covers code, schemas, tests and configuration; Markdown documentation is excluded, so the digest is the same wherever the runtime bytes are the same. Regenerate the lock from the repository root with `python FRAMEWORKS/CASEWORK/runtime/make_lock.py --framework-root FRAMEWORKS --out FRAMEWORKS/te_frameworks.lock.json --force`; any change to a listed file requires a regenerated lock, an updated digest in `compatibility.json` where the family is pinned, and a compatibility review.

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

The destination must be new and outside the source (`Destination exists; use a new run directory`, `Run directory must be separate from the source tree.`). The command creates `originals/` (one `DOC-nnnnn.bin` per acquired file), `derived/`, the `frameworks/` snapshot, `te_frameworks.lock.json`, `manifest.json` and `case.json`. It records the Python and jsonschema versions and checks them at every later execution (`Recorded Python/jsonschema environment differs; reproduce it or prepare a reviewed new run`); the operator keeps the environment reproducible. The manifest appears once every copy has succeeded and re-hashed. An interrupted preparation leaves a partial packet: resolve the cause and prepare a new run. The enumeration raises on a subfolder whose access is denied and refuses links and reparse points, in the source tree and among the ancestors of both the source and the run directory. On macOS `/tmp` and `/var` are symlinks, so both source and run directory need a real path; for cloud-synced files carrying such attributes prepare a suitable local source. The check is a boundary: given real paths, the runtime proceeds.

## Compilation and checking

1. Read the current protocols. Use `case.json` to record the state of every document (`reading`: `pending`, `read`, `unreadable`, `restricted`). Keep `wave1_complete=false` while any element is `pending`; relevance is decided after that boundary (`relevance` stays `deferred` until then).
2. At the end of the first wave, give reasons for provisional inclusions and exclusions (`include` or `exclude_provisional`, each with `relevance_reason`). An unreadable document is recorded as a limitation; the validator admits `exclude_provisional` for a document whose reading is `read`.
3. Record separate extractions (`derivatives`, stored under `derived/` with method, operator, time and hash), literal quotations (`evidence`: each `quote` must occur verbatim in the original or in the derivative it names), origin groups (`source_group`), gaps, chronology, relationships and analysis. Originals, snapshot and manifest stay as `prepare` wrote them. The hash detects changes relative to the packet; the manifest carries the owner and analyst named at `prepare`.
4. Complete the applicable audit areas (audit mode: `source_integrity`, `finance`, `procurement`, `authorizations`, `governance`, `people_internal_abuse`, `assets_resources`, `information_reporting`; investigation mode: `source_integrity`, `chronology`, `attribution`, `counterevidence`), giving reasons for tests, examined populations, results and limits. Findings require supporting evidence, at least one alternative explanation with a discriminating test, a counter-evidence search and next steps; a finding's confidence (S1–S3) is at most that of its weakest supporting premise, and S1 requires at least two recorded origin groups. A `legal_question` criterion requires an entry in `legal_references`.
5. Run the validator and have the dossier reviewed by a distinct reviewer. To reopen or revise, keep a copy of the previous case revision and of its report; the history of a case lives in the copies the analyst keeps.

```bash
python runs/case_01/frameworks/CASEWORK/runtime/casework.py validate --run-dir runs/case_01
python runs/case_01/frameworks/CASEWORK/runtime/casework.py review-request --run-dir runs/case_01
```

The second command validates the run first, then writes `review_request.json` with `decision: pending` and every check `pending`; a positive review is the reviewer's separate act. The file is written once (`File exists` on a second call): move or delete the previous request to issue another. After the reviewer has filled it in (`reviewer`, `reviewer_role`, `decision`, `rationale`, `reviewed_at`, the five checks), pass it with `--review` to the validator. Any change to `case.json` or `manifest.json` invalidates the receipt (`Review invalidated by changed case/manifest`). An `accept` decision requires a completed audit pass and all five checks at `accept`; the reviewer must differ from the analyst named in the manifest. The runtime records the reviewer's identity as entered; independence and professional qualification are established by the owner and the mandate.

The report printed by `validate` carries these fields. Field identifiers are canonical and language-independent; they match the runtime schema.

- `technical_status`: `TECHNICALLY_CHECKED` — the technical checks passed on the recorded state; a failed check prints `Casework blocked: <reason>` in place of the report.
- `phase`: `wave1` (elements at `pending`), `relevance_and_analysis` (wave closed, analysis open), `audit_required` (analysis complete, audit pass due), `independent_review_required` (audit complete, review acceptance on the current hashes due), `documentary_pass_review_recorded` (an `accept` review bound to the current hashes).
- `coverage`: `declared_accessible_pass_only` when every document is `read`, every check stands at `tested` or `not_applicable` with a result among `no_exception`, `exception` or `not_applicable`, the limitations list is empty and every gap is `resolved`; `limited_or_pending` otherwise.
- `review`: `not_recorded` (validator run with `--review` omitted), `pending`, `revise`, or `accept_recorded_identity_unverified`.
- `document_count`, `finding_count`, `case_sha256`, `manifest_sha256`: the counts and the hashes the review receipt binds to.
- `empirical_performance`: `not_assessed` and `legal_use`: `not_authorized_by_runtime`, both constants (`TE_CASEWORK_v0_1_EN.md` §6).
- `limits`: three fixed sentences, the runtime's statement of its scope (`TE_CASEWORK_v0_1_EN.md` §6 and §2).

The `audit_required` phase is computed automatically once the analysis is complete. It means the audit pass is now due, and the analyst performs it. The routing in the prompt is an operating instruction; the mechanical check happens when the command runs.

## Investigative mode

Use a new run with `--mode investigation`, `--investigation-mandate-ref` and `--supervising-role` stated explicitly (`Explicit investigative mandate and supervising role required` otherwise). Leave the manifest of an already acquired audit as it is; an investigative mandate needs its own run. The mode can be invoked directly, as the first run on a case. Closure requires competing hypotheses (`hypotheses`, at least two), including at least one of kind `non_criminal` or `exculpatory`, each with counter-evidence and discriminating checks (`Investigation requires competing and non-criminal/exculpatory hypotheses` otherwise).

This mode works on the acquired documents. The Italian jurisdiction profile in `TE_INVESTIGATION_v0_1_EN.md` §4 is a map of references; the reviewer's deliverables before penal use are listed in that section.

## Tests

```bash
cd FRAMEWORKS/CASEWORK
python -m unittest discover -s tests -v
```

The suite has 42 tests. On macOS set `TMPDIR` to a directory whose path is made of real directories (for example `mkdir -p tmp && TMPDIR=$PWD/tmp python -m unittest discover -s tests -v`): the default temporary directory sits under `/var`, a symlink to `/private/var`, and the runtime refuses symlinked ancestors. The JSON schemas in `schemas/` are generated by `python runtime/casework_schema.py`; `test_schema_generation_reproducible` checks that the committed files match the code.

The tests verify software constraints on records already filled in, correct and suspicious cases alike; the empirical plan is in `PILOT_PLAN.md`.
