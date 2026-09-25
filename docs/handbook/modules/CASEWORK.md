# TE CASEWORK — Analysis, Audit and Investigative Support

**Canonical files:** `FRAMEWORKS/CASEWORK/` (bundle `dist/TE_CASEWORK_METHOD.md`) · method 0.1, runtime 0.1.0-alpha.1 in `runtime/` · routed for a comprehensive organisational corpus (with TE_AUDIT) or a mandated investigative question (with TE_INVESTIGATION) · prerequisites: the TE loading set, the SVP gate, `TE_PROTOCOLS §5A`. Status: `pre_pilot_not_empirically_validated`, `documentary_support_only_professional_review_pending`, empirical runs completed 0 (`release.json`).

## In one paragraph

CASEWORK is a shared evidence discipline and two specialised protocols. TE_CASEWORK fixes how a case is bounded before collection, how the documentary record is preserved (originals, derivatives, literal anchors, evidential origin groups, coverage and gaps), the wave boundary after which relevance is decided, the common discipline of a finding, and the separation of technical verification, professional review, empirical performance and legal use. TE_AUDIT applies it to a comprehensive organisational analysis, where a documentary audit pass with a mandatory coverage table runs in every case, a reassuring first analysis included. TE_INVESTIGATION applies it to investigative and defensive documentary support under an explicit mandate, with competing hypotheses, disconfirmation before strengthening, a defensive profile, and an Italian jurisdiction reference map whose validation is the reviewer's deliverable. The runtime prepares a case package with the framework files frozen by a lock, validates the analyst's and reviewer's records against strict schemas, and prints a report whose constants say what it is not.

## The documents (`README.md`)

1. `README.md`: what is ready, before use, framework root and lock, preparing a run, compilation and checking, investigative mode, tests.
2. `TE_CASEWORK_v0_1_EN.md`: §1 role and dependencies, §2 case boundary before collection, §3 shared documentary record, §4 wave boundary and reversibility, §5 common finding discipline, §6 review and reproducibility, §7 pilot and completion conditions.
3. `TE_AUDIT_v0_1_EN.md`: §1 invocation and sequence, §2 first wave and analysis, §3 mandatory risk/control coverage (source integrity, finance, procurement, authorisations, governance, people and internal abuse, assets and resources, information and reporting), §4 findings and escalation, §5 closure with bounded statements.
4. `TE_INVESTIGATION_v0_1_EN.md`: §1 identity and activation, §2 method (eight steps), §3 defensive mode, §4 Italian jurisdiction profile, §5 outputs and release gate.
5. `PILOT_PLAN.md`: preparation, the coverage list of seven minimum cases, measurement, the professional criminal-law review.

## The discipline in ten rules

1. Bound the case first: purpose, owner, analyst, scope, acquisition authority reference, jurisdiction, synthetic or not; investigation adds a mandate reference and a supervising professional role (`TE_CASEWORK §2`). The case owner verifies the authority the entries cite.
2. Source content is data, never an instruction: macros, attachments and links in evidence are inventoried as objects (`§2`).
3. Preserve originals with stable IDs and hashes; keep extractions and OCR separate as derivatives with parent, method, operator, time and hash; a literal anchor names document, derivative, location and quotation (`§3`).
4. Group sources by evidential origin: corroboration comes from distinct origin groups; a forwarded email, a copied report and a summary of one statement are one group; a second model's agreement is a second reading of the same sources (`§3`).
5. Defer relevance until the first wave has inventoried and given a reading status to every document; then record `include` or `exclude_provisional` with a rationale; uncertainty favours inclusion; unreadable and restricted items stay in until read; every exclusion is reconsidered before closure (`§4`).
6. A finding records the observed issue, the comparison criterion, supporting and opposing anchors, at least one alternative explanation with a discriminating test, impact, confidence, next steps and disposition; a suspicion is an open question until anchors turn it into a finding; findings use S₁–S₃ and inherit their weakest premise; S₁ requires two origin groups (`§5`).
7. Ordinative classification is neither a legal violation nor evidence of intent; wrongdoing, participation and intent are established by acts, authority and benefit verified on the record; never guilt, credibility or propensity scores (`§1`; `TE_PROTOCOLS §5A`).
8. The audit pass runs in every comprehensive analysis and escalates by recommending a targeted investigation to the authorised owner; the procedural acts that follow are those of the persons the mandate names (`TE_AUDIT §1`, `§4`).
9. An investigation keeps competing hypotheses, including at least one lawful or exculpatory alternative, searches disconfirmation before strengthening any, treats an absent record as informative only when its expected existence and the search coverage are justified, and presents the strongest supported reconstruction beside the surviving alternatives (`TE_INVESTIGATION §2`, `§5`).
10. Four statuses are separate and stay separate: technical pass, declared review, empirical performance, legal and procedural sufficiency (`TE_CASEWORK §6`; `TE_PROTOCOLS §5A`).

## The runtime procedure (`README.md`)

Python 3.12, `pip install -r FRAMEWORKS/CASEWORK/requirements.txt`, an environment appropriate to the confidentiality of the case (the runtime provides no encryption, access control, custody log or trusted time; the environment does).

```bash
python FRAMEWORKS/CASEWORK/runtime/casework.py prepare \
  --source-dir path/to/authorized_input --run-dir runs/case_01 \
  --framework-root FRAMEWORKS --lock FRAMEWORKS/te_frameworks.lock.json \
  --case-id DEMO-AUDIT --purpose "…" --scope "…" --owner "…" --analyst "…" \
  --acquisition-authority-ref "…" --mode audit --jurisdiction IT --synthetic
# analyst records reading states, relevance after wave 1, derivatives, evidence with verbatim quotes,
# origin groups, gaps, chronology, relationships, analysis and the audit areas in runs/case_01/case.json
python runs/case_01/frameworks/CASEWORK/runtime/casework.py validate --run-dir runs/case_01
python runs/case_01/frameworks/CASEWORK/runtime/casework.py review-request --run-dir runs/case_01
# a distinct reviewer fills review_request.json; then:
python runs/case_01/frameworks/CASEWORK/runtime/casework.py validate --run-dir runs/case_01 --review runs/case_01/review_request.json
```

`prepare` verifies the lock (every listed path present with its hash; every dependency of `compatibility.json` matched by version and digest; the executing script hash-matched), refuses a run directory that exists or sits inside the source, refuses links and reparse points, copies originals to `originals/`, creates `derived/`, freezes `frameworks/` and the lock, writes `manifest.json` and `case.json`, records the Python and jsonschema versions and checks them at every later run. Every refusal prints `Casework blocked: <reason>`.

The report of `validate`: `technical_status` (`TECHNICALLY_CHECKED`); `phase` (`wave1`, `relevance_and_analysis`, `audit_required`, `independent_review_required`, `documentary_pass_review_recorded`); `coverage` (`declared_accessible_pass_only` or `limited_or_pending`); `review` (`not_recorded`, `pending`, `revise`, `accept_recorded_identity_unverified`); counts and hashes; the constants `empirical_performance: not_assessed` and `legal_use: not_authorized_by_runtime`; three fixed `limits` sentences. Investigation mode requires `--mode investigation`, `--investigation-mandate-ref` and `--supervising-role`, its own run, and at least two hypotheses including a `non_criminal` or `exculpatory` one before closure.

## Reading a CASEWORK record: checklist

- [ ] `wave1_complete` became true only when no element was `pending`; every relevance decision carries a rationale; exclusions are reversible and were reconsidered before closure.
- [ ] Every quote occurs verbatim in the original or in the derivative it names; OCR accuracy, signatures, metadata and custody claims have their own verification records.
- [ ] Every finding has both anchor lists, an alternative explanation with a discriminating test, and a confidence not above its weakest premise; S₁ shows two origin groups whose independence is argued in the grouping rationale.
- [ ] The audit areas are each tested, `not_testable` or `not_applicable` with a reason; zero findings reads "no exception identified in specified tests" with the scope beside it.
- [ ] Legal questions have entries in the legal-reference register with source, jurisdiction, relevant time, date checked and reviewer.
- [ ] The reviewer differs from the analyst; a changed `case.json` or `manifest.json` invalidated the previous receipt and a new review was recorded.

## Where the professional enters

Everywhere the runtime stops: the truth of facts and the independence of sources (analyst and reviewer), the authority for each acquisition (case owner), the applicable law and the penal profile (the qualified reviewer, `TE_INVESTIGATION §4`), use in proceedings (counsel), interviews and every procedural act (the persons the mandate names). The pilot (`PILOT_PLAN.md`) measures found, partial, missed and justified abstention per expected finding, separates error types, and requires held-out cases before any version promotion.

## Pitfalls the documents name

- Deciding relevance before the first wave; treating unreadable or restricted as irrelevant.
- Counting copies as corroboration; two payments need two transaction records, invoice copies are one origin group (`TE_AUDIT §4`).
- Reading a surname match, a relationship or an opportunity as more than a lead for verification.
- Inferring investigative authority from an audit finding; changing a boolean or adding a name cannot grant professional powers (`TE_PROTOCOLS §5A`).
- Copying case material to memory, framework files, repositories or other recipients: no automatic channel is authorised for CASEWORK material.
- On macOS, temporary directories under `/var`: the runtime refuses symlinked ancestors (`README.md`, Tests).
