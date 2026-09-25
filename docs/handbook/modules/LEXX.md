# LEXX — Ordinative Validation of Agreements

**Canonical files:** `FRAMEWORKS/LEXX/` (bundle `dist/TE_LEXX_METHOD.md`) · method 0.1, runtime 0.2.0-alpha.3 in `v0_2_alpha3/` · on demand, routed for agreements and normative systems · prerequisites: the TE loading set and the SVP gate. Status: `pre_pilot_not_empirically_validated`, empirical runs completed 0 (`release.json`).

## In one paragraph

LEXX reads a written agreement as an ordinative set and does three things in order: understands and validates its structure, brings every vulnerability to light, and inverts the collapse, tracing back from the text to the vector its structure enables and, where required, formulating a counter-proposal that keeps the legitimate invariant and drops the control payload. It is the LEX project of a student of the Hypervisor realised with the full canon (OST, TE, SA, PA, OCT, Controfase, Lyapunov, and the modules SVP, LENS, PPRO, VERI, OBSERVER). The method (0.1) is a ten-stage pipeline with a JSON output that mirrors it; the runtime (0.2.0-alpha.3) prepares a run with the framework files frozen by hash, validates the executor's JSON against a strict schema and the source text, and prepares a hash-bound request for an independent review of the counter-proposals. Empirical validation is the pilot's task, not yet performed.

## The documents, in reading order (`README.md`)

1. `README.md`: status, canonical placement, reading order, what LEXX adds to the LEX, custody.
2. `00_FOUNDATIONS.md`: the question; the four domain axioms A1 (the agreement is ⟨Σ, R, Φ⟩ and the flaw lives in R), A2 (the text is a collapse invertible only by tomography; intention is never S₀), A3 (proportion is measurable; in 0.1 an ordinal band), A4 (the agreement is a trajectory; λ_L as a sign); the integration map of each canon instrument to its task; the three safeguards P1 verified anchoring, P2 intention never S₀, P3 the empty field stays empty, each with who enforces it in 0.1; the ethical constraint (defensive and diagnostic; no intention imputed as fact; the counter-proposal is born disarmed; the inverse capability stays in the laboratory; LEXX does not replace counsel).
3. `02_COMPATIBILITY_PROFILE.md`: the minimum stack, dependencies by stage, degradation rules, run states, the mandatory distinction on intention, open gaps; superseded for execution by the alpha.3 profile.
4. `TE_MODULE_LEXX_v0_1_EN.md`: the legender (every symbol used, closed locally under the canon), perspective and gate, the ten stages, the scoring rubric, the JSON format.
5. `01_ANNOTATED_EXAMPLE.md`: a seven-clause synthetic agreement, with a decoy, through every stage.
6. `03_PRE_PILOT_PROTOCOL.md`: the execution contract for alpha.3 runs.
7. `v0_2_alpha3/README.md`: the runtime.

## The pipeline (`TE_MODULE_LEXX §1`)

| Stage | Name | Instrument | What it produces |
|---|---|---|---|
| 0 | INSED | SVP | provenance, version and status, formation (double approval under artt. 1341-42 c.c., form, registration, powers), qualification of the parties B2C/B2B/C2C/PA, perimeter (document only or document and system), external mitigation with its grading rule |
| 1 | two-channel STRIP | OST + SA | per load-bearing clause: the etymological step and κ_c, ι (what it legitimately gives), P (the control payload), declared vs effective function, Δ_𝔉; the triple; Φ_declared vs Φ_effective |
| 1.5 | consistency | LEXX rules | arithmetic (every number against every derived quantity) and temporal (assumptions valid today vs due to lapse) checks |
| 2 | flaw vectors | LEXX | V-OM omission, V-AM ambiguity with divergent outcomes, V-IN intersection (the white space between clauses, LEXX's vector of election), V-TEMP order and time; citation mandatory |
| 3 | E→I inversion | TE + LENS + PPRO + SA | the intention vector by tomography of the payloads; declared vs effective vector; LENS discipline ("the text allows whoever holds this position to…"); PPRO scan; grade S₁–S₃, S₁ with three or more independent clauses converging |
| 4 | proportion | PA | κ band (alta/media/bassa) with the criterion (which levers each party holds); equity class: balanced, declared asymmetry, hidden asymmetry |
| 5 | trajectory | Lyapunov / OBSERVER | the sign of λ_L (converges/diverges) argued from the text, bifurcations (trigger clauses), CVI band per flaw |
| 6 | class and residue | OCT + VERI | OCT class A/B/C/D per clause; residue of the protections 0–3 |
| 7 | contrary test | Controfase | the valid opposite reading, the hermeneutic canon (artt. 1362-1371 c.c., contra proferentem), outcome confirmed / downgraded / discarded; P-AI on the analyst into `meta_pai` |
| 8 | counter-proposal | π + neutralisation + Lyapunov | rewriting π(ι, 𝔻_fair) with the re-strip exhibited, or neutralisation by junction, or a counter-right; valid when it inverts or keeps the sign of λ_L; coupled to its flaw |
| 9 | verdict | whole pipeline | accordo_solido, falle_puntuali, falle_strutturali, device, degenerato, fortezza_valida; inherits the weakest grade |

Beside the mirror: `tre_mappe` (what it says, what it does not say, what it says without saying it) and `non_falle_verificate` (the suspects discarded, with the decisive filter).

## The runtime procedure (`v0_2_alpha3/README.md`)

From a clone, Python 3.12, a virtual environment outside the framework folders, `pip install -r FRAMEWORKS/LEXX/v0_2_alpha3/requirements.txt`; the source converted to UTF-8 text first.

```bash
python FRAMEWORKS/LEXX/v0_2_alpha3/runtime/prepare_run.py --source agreement.txt --framework-root FRAMEWORKS --run-dir runs/case_01
# fill runs/case_01/output_draft.json and save it as output.json (a person or an LLM session is the executor)
python runs/case_01/frameworks/LEXX/v0_2_alpha3/runtime/validate_lexx_output.py --source runs/case_01/source.txt --output runs/case_01/output.json --framework-root runs/case_01/frameworks --run-manifest runs/case_01/run_manifest.json --report runs/case_01/technical_report.json
python runs/case_01/frameworks/LEXX/v0_2_alpha3/runtime/prepare_review.py --source runs/case_01/source.txt --output runs/case_01/output.json --review runs/case_01/review.json
# a distinct reviewer fills review.json; then re-run the validator with --review runs/case_01/review.json
```

What the runtime checks: the eleven TE files by exact name and SHA-256 against `compatibility.json` (a mismatch stops with `Dependency hash changed`); the JSON against the Draft 2020-12 schema; every literal quotation against the source (NFC and whitespace normalised, case significant: `ANCHOR_NOT_FOUND` otherwise); the two contexts of a structural absence; the partition of the clause inventory (`COVERAGE_PARTITION`); references between clauses, intersections, flaws and tomography; the S₁ threshold on the vector (three clauses with payloads); the weakest-grade rule (`CONFIDENCE_INFLATION`); the arithmetic recomputed with exact decimals; the frozen files unchanged (`FROZEN_FILE_CHANGED`); the review's independence, re-strip and outcome.

What the report says: `valid` and `technical_status` (`TECHNICALLY_CHECKED` or `INVALID_OUTPUT` with error codes); `analysis_status` (`not_assessed` for a draft or an open verdict, `document_only_unvalidated` otherwise); `round_trip` (`pending_independent_review`, `not_applicable`, `rejected`, `recorded_fail`, `recorded_pass`); `empirical_validation: false` as a constant; metrics, hashes, verified dependencies, limits.

Run states (`02_COMPATIBILITY_PROFILE §5`): `CONFORMANT_VERIFIED`, `CONFORMANT_QUALITATIVE`, `LLM_ONLY_UNVERIFIED`, `DOCUMENT_ONLY`, `INCOMPATIBLE_STOP`, `INVALID_OUTPUT`; compatible states coexist (an alpha.3 run is `CONFORMANT_QUALITATIVE` and `DOCUMENT_ONLY`; the executor also declares `LLM_ONLY_UNVERIFIED`, which the external report closes).

## Reading a LEXX output: checklist

- [ ] Perspective, mode, qualification of the parties and perimeter are declared (mandatory fields).
- [ ] Every flaw has a literal citation that matches the source; every structural absence has its two contexts.
- [ ] The intention vector is S₁–S₃, never S₀; the tomography lists the clauses and payloads that support it; where payloads scatter, the field is empty with a `nota_limite`.
- [ ] Proportion and trajectory are bands and signs with the criterion exhibited, not numbers (numbers require the engines of v0.2).
- [ ] Each retained flaw carries its counter-proposal with the re-strip; the residual payload is empty or the draft is marked for another pass.
- [ ] The decoys were discriminated: a declared, lawful asymmetry with Δ_𝔉 = 0 and a measurable residue is a negotiation note, not a flaw (`01_ANNOTATED_EXAMPLE`, C7).
- [ ] The `sistema` verdict is `non_valutabile` and `external_sources_verified` is false in this profile; the statutory references are leads to be verified for jurisdiction, date, parties and facts.

## Where the professional enters

The runtime performs technical checks; semantic relevance, independence of clauses, legal validity and the use of the counter-proposal are the reviewer's and counsel's (`03_PRE_PILOT_PROTOCOL`, `00_FOUNDATIONS §4`). The pilot (`03_PRE_PILOT_PROTOCOL`, "Pilot on real cases") seals a reference prepared by a reviewer, freezes the first attempt, adjudicates findings, and computes precision and recall with explicit denominators; promotion to stable rests on adjudicated cases.

## Pitfalls the documents name

- Reading clause by clause (Σ) and missing the field (R) where the flaw lives (A1).
- Writing "X wants" instead of "the structure orients toward" (Stage 3, LENS discipline).
- Filling an empty field with plausible content (P3).
- Confusing the drafting tactic "neutralisation by junction" with Controfase, which names the hygiene function of Stage 7.
- Treating the historical compatibility profile (0.1, 2026-09-16, with paths to superseded files) as the execution profile: the alpha.3 profile in `v0_2_alpha3/compatibility.json` governs new runs.
- Running the validator from the repository copy instead of the frozen copy inside the run packet.
