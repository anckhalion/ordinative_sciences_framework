# LEXX runtime 0.2.0-alpha.3

Technical preparation for the pilot of 2026-09-17. Method: LEXX 0.1, internal to the Technology of Expressions (TE). Read `../03_PRE_PILOT_PROTOCOL.md` first. Earlier alpha runtimes are historical; new cases run on this version. Status recorded in `../release.json`: `pre_pilot_not_empirically_validated`, `empirical_runs_completed: 0`.

Revision of 2026-09-23, at first publication and with the runtime version unchanged: `runtime/prepare_run.py` resolves the frozen methodology documents by edition (see below), the placeholder texts of the draft (`output_draft.json`) are in English, one test covers the resolution, and the package digest pinned in `CASEWORK/compatibility.json` is computed on the published bytes.

## Environment

Python 3.12. The packages in `requirements.txt` are pinned to exact reviewed versions and go into an isolated virtual environment, outside the framework folders. A development folder is not automatically suitable for confidential case files: choose the run location according to the confidentiality of the agreement.

Validation uses `jsonschema.Draft202012Validator` with format checking; technical reference: [jsonschema documentation](https://python-jsonschema.readthedocs.io/en/stable/validate/). Without the library the validator stops and the report carries the error code `VALIDATOR_DEPENDENCY`.

### Files the runtime reads by name

`runtime/prepare_run.py` and `runtime/validate_lexx_output.py` read the TE dependencies from `--framework-root` by exact filename and compare the SHA256 of each file with `compatibility.json` (`dependency_policy`: exact reviewed versions and SHA256; a newer version requires a compatibility review). The folder passed as `--framework-root` holds these eleven files, byte-identical to the pinned hashes:

| Component | Version | File |
|---|---|---|
| TE_BOOTLOADER | 7.1.1 | `TE_BOOTLOADER_v7_1_1_EN.md` |
| TE_PROTOCOLS | 1.1 | `TE_PROTOCOLS_v1_1_EN.md` |
| TE_CORE | 5.2.1 | `TE_CORE_v5_2_1_EN.md` |
| TE_OST | 2.1 | `TE_OST_v2_1_EN.md` |
| TE_SYMBOL_CANON | 1.2 | `TE_SYMBOL_CANON_v1_0_EN.md` |
| TE_MODULE_SVP | 5.1 | `TE_MODULE_SVP_v5_1_EN.md` |
| TE_MODULE_LENS | 5.1 | `TE_MODULE_LENS_v5_1_EN.md` |
| TE_MODULE_PPRO | 5.2 | `TE_MODULE_PPRO_v5_2_EN.md` |
| TE_MODULE_VERI | 1.0 | `TE_MODULE_VERI_v1_0_EN.md` |
| TE_OBSERVER | 1.1 | `TE_OBSERVER_v1_1_EN.md` |
| TE_OST_TELEODYNAMICS | 1.2 | `TE_OST_Extension_Teleodynamics_v1_1_EN.md` |

A hash mismatch stops preparation with `Dependency hash changed: <component>; compatibility review required`. SA, PA, OCT and Lyapunov are listed under `not_loaded_as_full_engines`: the derived profile is the set of canonical qualitative operations defined in the Foundations, the TE module and the Symbol Canon, with no formal OCT certification and no quantitative engine.

`prepare_run.py` also freezes the methodology and the executable contract into the run packet: from the folder above `v0_2_alpha3` it copies `README.md`, `03_PRE_PILOT_PROTOCOL.md`, `release.json`, the Foundations and the module — the last two resolved under the names their edition carries (`00_FOUNDATIONS.md` or `00_FONDAMENTA.md`; `TE_MODULE_LEXX_v0_1_EN.md` or `TE_MODULE_LEXX_v0_1.md`; every edition present is frozen) — plus every file of `v0_2_alpha3` (bytecode caches excluded). The name groups are held in `PACKAGE_DOCUMENTS` in `runtime/prepare_run.py`; a group with no file present stops preparation with `Run preparation failed: Package document missing in <folder>: one of <names>`.

## Procedure from a repository clone

Layout assumed below: `FRAMEWORKS/`, at the repository root, holds the eleven TE files under their canonical names and the `LEXX` folder; this runtime is `FRAMEWORKS/LEXX/v0_2_alpha3`. Paths are relative to the repository root; adapt `--framework-root` if the TE files live elsewhere.

```bash
git clone <repository-url>
cd <repository>

python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r FRAMEWORKS/LEXX/v0_2_alpha3/requirements.txt

# 1. Prepare a new run folder for each case. The source must be UTF-8 text
#    (a leading BOM is tolerated); the runtime performs no OCR and no conversion
#    from PDF or DOCX. An existing run folder is refused.
python FRAMEWORKS/LEXX/v0_2_alpha3/runtime/prepare_run.py \
  --source path/to/agreement.txt \
  --framework-root FRAMEWORKS \
  --run-dir runs/case_01

# 2. Fill in output_draft.json and save it as output.json.
#    source.txt, the frozen frameworks and run_manifest.json stay untouched.

# 3. Verify with the runtime frozen inside the run packet and the pinned dependencies.
python runs/case_01/frameworks/LEXX/v0_2_alpha3/runtime/validate_lexx_output.py \
  --source runs/case_01/source.txt \
  --output runs/case_01/output.json \
  --framework-root runs/case_01/frameworks \
  --run-manifest runs/case_01/run_manifest.json \
  --report runs/case_01/technical_report.json

# 4. If output.json holds counter-proposals with status "proposed",
#    create the request for the separate review.
python runs/case_01/frameworks/LEXX/v0_2_alpha3/runtime/prepare_review.py \
  --source runs/case_01/source.txt \
  --output runs/case_01/output.json \
  --review runs/case_01/review.json
```

On Windows use `python` in place of `python3`, backslashes in paths, and write each command on one line.

What each step does:

- **Step 1** — `prepare_run.py` (`--source`, `--framework-root`, `--run-dir`, all required) writes `runs/case_01/` with `source.txt` (byte copy of the source), `frameworks/` (the eleven TE files plus `LEXX/…` frozen as described above), `output_draft.json` and `run_manifest.json`. The draft is an empty template carrying `run_id`, `source_sha256` and the `dependency_ledger`, with every analytical field set to `non_valutabile`, `vuoto`, `S3` or empty. The manifest records the SHA256 of every frozen file and states its own limits: "Hash freezing does not prove reading or understanding" and "The draft is an empty template, not an analysis".
- **Step 2** — the executor (a person or an LLM session) fills the draft. Field identifiers are canonical and language-independent; they match the runtime schema (`schemas/lexx_output.schema.json`: keys such as `strip`, `campo_relazionale_R`, `falle`, `vettore_intenzione`, `controproposta`, `verdetto_generale`). `run_states` keeps `DOCUMENT_ONLY` and `LLM_ONLY_UNVERIFIED` (the semantic check `REQUIRED_STATES` rejects their absence; `CONFORMANT_QUALITATIVE` may be added), and the `verification` block keeps its `unverified` constants: there the schema rejects any other value.
- **Step 3** — `validate_lexx_output.py` (`--source`, `--output`, `--framework-root` required; `--review`, `--run-manifest`, `--report` optional) prints the report as JSON and, with `--report`, writes it to that path; the report path differs from every input path, or the script exits with `Report cannot overwrite an input file`. Exit code 0 when `valid` is true, 1 otherwise. Run it from the frozen copy inside the run packet, so that the schema and the `compatibility.json` it reads are the frozen ones.
- **Step 4** — `prepare_review.py` (`--source`, `--output`, `--review`, all required) writes an unfilled review request bound to the SHA256 of source, output and each proposed `forma_equa`; an existing review file is refused (`FileExistsError`). The reviewer, a distinct identified session (a person or a second execution), fills `reviewer_id`, `review_run_id` (different from the run's `run_id`), `independent_declared: true` and, for every item, `independent_restrip` (`iota_primo`, `payload_primo`), `invariant_preserved`, `lambda_post` (`neg`, `pos`, `vuoto`) and `reason`.

After the review, re-run the validator adding `--review runs/case_01/review.json`. An unfilled request fails the review checks (`REVIEW_INDEPENDENCE`, `REVIEW_RESTRIP`). Keep each attempt in its own run folder: `prepare_run.py` refuses an existing run directory, and the manifest binds every report to the frozen bytes of the attempt it belongs to.

## Report

- `valid` / `technical_status=TECHNICALLY_CHECKED`: contract and technical checks passed. Otherwise `valid=false` and `technical_status=INVALID_OUTPUT`, with each failure listed under `errors` as `code`, `path`, `message` (for example `SCHEMA`, `SOURCE_HASH`, `ANCHOR_NOT_FOUND`, `COVERAGE_PARTITION`, `CONFIDENCE_INFLATION`, `FROZEN_FILE_CHANGED`, `INPUT_OR_CONFIGURATION`).
- `analysis_status=not_assessed`: a draft or an analysis that cannot be assessed, even when technically valid (`verdetto_generale` is `non_valutabile`). A technically valid output with any other verdict reads `document_only_unvalidated`, and `ready_for_independent_review` becomes `true`.
- `round_trip=pending_independent_review`: a counter-proposal is present and still to be reviewed. `not_applicable` when no counter-proposal has status `proposed`; `recorded_fail` or `rejected` when a review was supplied and did not confirm.
- `round_trip=recorded_pass`: a positive outcome declared in a separate review bound to the hashes.
- `empirical_validation=false`: the runtime does not certify diagnostic capacity. The field is a constant of the report.

The report also carries `metrics` (`anchors_checked`, `literal_quotes`, `structural_absences`), `source_sha256`, `output_sha256`, `schema_sha256`, `run_manifest_sha256` when a manifest was supplied, `verified_dependencies`, and its own `limits`: "Technical checks do not establish diagnostic correctness or legal validity", "Context anchors do not prove a semantic absence", "Dependency availability does not prove that an executor read or understood them", "Review identity and independence are recorded declarations, not authenticated facts".

The external report is the only technical attestation; the executor's JSON keeps `verification` unverified. The profile is `DOCUMENT_ONLY`, qualitative, diagnostic mode. Quantification, external legal sources and laboratory mode are not activated by executor declarations: the schema fixes `external_sources_verified` to `false`, `proporzione.mode` and the trajectories to `qualitative`, the system verdict to `non_valutabile` and the confidence of the intention vector to S1–S3 (S₀ is forbidden on the vector); the semantic checks reject OCT class `D` in `DOCUMENT_ONLY`. Literal quotes are matched after NFC and whitespace normalisation, with case significant; a structural absence is checked as the ordered presence of its two context anchors; declared arithmetic is recomputed with exact decimals. The runtime does not compute semantic equivalence and does not authenticate the reviewer's independence.

## Technical verification

```bash
cd FRAMEWORKS/LEXX/v0_2_alpha3
python -m unittest discover -s tests -v
```

The suite (40 tests) builds its own fixtures in a temporary folder: the framework files it hashes are placeholders and the agreement is three synthetic clauses. The tests are synthetic; they do not count as field evidence. The schema is generated by `runtime/build_schema.py` (no arguments; it writes `schemas/lexx_output.schema.json` in the `schemas/` folder beside `runtime/`): regenerate it after every change of the contract and re-run the tests, which compare the shipped schema with the builder.
