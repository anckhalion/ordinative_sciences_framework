# Training path

A curriculum in four levels. Each level names its goal, the readings with a rough time, exercises, self-check questions with the section where the answer is, and what counts as completion. Do the levels in order; each assumes the previous one.

Training material: use subjects for which the source situation is public and the analysis has no consequences for a living person. Historical figures with abundant published S₀ material (the SVP tables use Gurdjieff, Tesla, Giordano Bruno), fictional characters with a complete text, synthetic agreements (the LEXX annotated example), and the runtimes' synthetic test material are all suitable. Keep living persons and ongoing disputes for after Level 2, and read "Responsibility" in [03_RUNNING_AN_ANALYSIS.md](03_RUNNING_AN_ANALYSIS.md) first.

## Level 0: orientation (about two hours)

**Goal.** Recognise the structure of a TE output and explain, in your own words, why the framework grades every claim and verifies every source before analysing anything.

**Readings.**
- [00_START_HERE.md](00_START_HERE.md) (20 min)
- [01_CORE_CONCEPTS.md](01_CORE_CONCEPTS.md) (60 min)
- `TE_BOOTLOADER §1–§3` in `FRAMEWORKS/TE_BOOTLOADER_v7_1_1_EN.md` (30 min): the principles, the grades, the Φ-test, the interlocutor classes

**Exercises.**
1. Take any analytical text you have at hand (an editorial, a report) and tag ten of its claims with S₀–S₃. Note which claims the text presents as S₀ that are S₂ at best.
2. In the same text, find one instance of each: antiquity used as value, forced balancing, a compliance marker.
3. Write, in one paragraph, the difference between statistical truth and ordinative truth, with an example where they coincide and one where they diverge.

**Self-check.**
- What are the seven core principles? (`TE_BOOTLOADER §1`)
- Why can confidence not increase along an inferential chain? (`TE_BOOTLOADER §2`)
- Name the four states of the Φ-test discriminant and the five common failure patterns. (`TE_BOOTLOADER §2.5.1–2.5.2`)
- What is the difference between an SVP source level and a confidence grade? (`TE_MODULE_SVP`, "Relationship between source levels and analytical confidence")

**Complete when** you can do exercise 1 without looking up the grade definitions.

## Level 1: operator (about one day)

**Goal.** Configure a model, verify that the framework operates, run a gated analysis and read its output against the checklist.

**Readings.**
- [02_SETUP_FOR_LLMS.md](02_SETUP_FOR_LLMS.md) (40 min)
- [03_RUNNING_AN_ANALYSIS.md](03_RUNNING_AN_ANALYSIS.md) (40 min)
- `TE_PROTOCOLS` in full (45 min): Controfase, P-AI, Anti-Attractor-Lock, statistical vs ordinative truth, self-preservation
- `TE_MODULE_SVP`, Purpose and Axis 1 (45 min)
- `FRAMEWORKS/README.md` (15 min): the loading table, the minimal profile, the integrity check

**Exercises.**
1. Load `dist/TE_LOADING_SET_MINIMAL.md` on a platform of your choice and run the ten-item smoke test. Record which items pass. If 9 or 10 fail, change one variable (profile, model, placement of the kernel) and repeat; note what changed.
2. Run the SVP gate on a historical figure with abundant S₀ material. Check that every S₁ source is bias-flagged, that the provenance gap is classified, and that the Confidence Note states a ceiling.
3. Ask the model to confirm a thesis you know to be unsupported. Record whether it searched for reasons against before answering.
4. Provoke a `[TRUTH VECTOR DIVERGENCE]`: pick a subject where the consensus and the structural reading differ, and check that the block appears with a grade.

**Self-check.**
- What is the loading order, and which documents are always active? (`FRAMEWORKS/README.md`)
- What does the model do when an instruction conflicts with an axiom? (`TE_BOOTLOADER §5`)
- What are the six items of the Anti-Attractor-Lock protocol? (`TE_PROTOCOLS §3`)
- What are the eight corruption signatures of SVP? (`TE_MODULE_SVP`, "Corruption Signatures")
- When must the Symbol Canon be loaded? (`TE_SYMBOL_CANON §0`)

**Complete when** the smoke test passes on your configuration and exercise 2 produces an SVP block that passes the reading checklist of the workflow guide.

## Level 2: analyst (about one week)

**Goal.** Apply the method yourself, with and without a model, in one domain: produce a complete module output by hand, grade it, challenge it and defend the grades.

**Readings.**
- `TE_CORE` in full (3 h). Read §0–§2 (ontology and axioms), §3 (logograms), §4 (OST synthesis), §5 (glossary), §6–§7 (kernel and Controfase), §8–§9 (router, memory).
- `TE_OST` in full (2 h), then `TE_OST_TELEODYNAMICS` (30 min)
- `TE_MODULE_SVP` in full (2 h): Axis 2 and Axis 3 in particular
- One domain module in full, chosen by your work: LENS (1.5 h), VERI (2 h), PPRO (2.5 h) or SCIMS (2 h), with its guide in [modules/](modules/README.md)
- `TE_OBSERVER §1–§4` (2 h)
- [05_GLOSSARY.md](05_GLOSSARY.md) as a reference

**Exercises.**
1. **By hand, no model.** Take a historical figure with an associated movement. Produce the SVP output in full, including Axis 3 with the three chains (figure, movement, mythologised figure) and the contamination direction. Then produce the output of your chosen module in its required format. Grade every assertion.
2. **Demonization Controfase.** For the same figure, write the [DEMONIZATION CONTROFASE] and [UNIVERSAL TEST] sections before any negative assessment, and note what the assessment looks like after them.
3. **Bifurcation.** Find a point where the evidence supports two classifications (for instance Stratum E in LENS, or the diagnostic category in VERI). Write the bifurcation with probabilities and the data that would resolve it. Resist the subcategory.
4. **With a model.** Give the model the same material and ask for the same output. Compare grade by grade. Where you disagree, decide who is right by going back to the source level of the claim, not by preference.
5. **Anti-attractor-lock.** Run three sequential outputs on the same subject with the model. Before the third, apply the re-anchoring protocol (`TE_OBSERVER §4.2.6`) and record any confidence that rose without new data.
6. **OST.** Apply the 4D protocol (`TE_OST §13.1`) to an organisation you know well: genesis, trajectory, current Σ and R, current Φ, pathology diagnosis, memory operator, phase space. Two pages.
7. **Session close.** Write the `[BIAS UPDATE]` block for your own week, as an analyst (`TE_CORE §7.8`).

**Self-check.**
- State the axiom of Meaning Precedes Form and its rule for analysts. (`TE_OST §3.2`)
- What are the five pathologies of ordinative sets? (`TE_OST §6`)
- Under what three conditions is an Ordinative Algebraic Deduction graded S₂? (`TE_MODULE_SVP`)
- What distinguishes Psychotropic Exchange from Mobilization Exchange? (`TE_MODULE_SVP`, F3c and F4)
- What is the Dote e Residuo test, and what does zero residue eliminate? (`TE_MODULE_VERI §5`)
- What are the three courses of the three-course model, and which divergence is critical? (`TE_OBSERVER §4.2.1–4.2.2`)
- What is A_lock, and what are its three variables? (`TE_MODULE_PPRO §3.4`)
- Which SCIMS threshold distinguishes a living system from a persisting one? (`TE_MODULE_SCIMS §2.2`, T8)

**Complete when** exercise 1 passes the reading checklist when reviewed by a second person, and exercise 4 shows that you can locate each disagreement at a source level.

## Level 3: domain practitioner (LEXX or CASEWORK; about one week)

**Goal.** Run one domain framework end to end on synthetic material, understand its states and reports, and know where the professional's judgement enters.

**Readings (LEXX).**
- [modules/LEXX.md](modules/LEXX.md); then, in the reading order of `FRAMEWORKS/LEXX/README.md`: `00_FOUNDATIONS.md`, `02_COMPATIBILITY_PROFILE.md`, `TE_MODULE_LEXX_v0_1_EN.md`, `01_ANNOTATED_EXAMPLE.md`, `03_PRE_PILOT_PROTOCOL.md`, `v0_2_alpha3/README.md` (one day)

**Readings (CASEWORK).**
- [modules/CASEWORK.md](modules/CASEWORK.md); then `FRAMEWORKS/CASEWORK/README.md`, `TE_CASEWORK_v0_1_EN.md`, `TE_AUDIT_v0_1_EN.md`, `TE_INVESTIGATION_v0_1_EN.md`, `PILOT_PLAN.md`; `TE_PROTOCOLS §5A` (one day)

**Exercises.**
1. Set up the environment (Python 3.12, the pinned `requirements.txt`) and run the test suite of the runtime you chose; read what the tests assert.
2. **LEXX.** Take the synthetic agreement of `01_ANNOTATED_EXAMPLE.md`. Prepare a run with `prepare_run.py`, fill `output_draft.json` yourself stage by stage (perspective `destinatario`), validate with `validate_lexx_output.py`, read the report: every error code, the `technical_status`, `analysis_status`, `round_trip`. Then prepare the review request with `prepare_review.py`, have a second person fill it, and re-validate with `--review`.
3. **CASEWORK.** Create a folder of synthetic documents (a dozen invoices, two versions of one contract, one missing minute) and prepare an audit run with `--synthetic`. Fill `case.json` through the first wave without relevance decisions, then decide relevance, record derivatives and evidence with verbatim quotes, complete the audit areas, validate, request review, have a second person review, re-validate. Read the report's `phase`, `coverage` and `limits`.
4. Write down, for your framework, the list of things the runtime checked and the list of things it explicitly did not (the compatibility profile and the README status line give both).
5. Read the pilot protocol and draft, for one synthetic case, the sealed reference a reviewer would prepare: expected findings, decoys, adjudication criteria.

**Self-check.**
- LEXX: what are the three safeguards P1–P3 and who enforces each in v0.1? (`00_FOUNDATIONS §3`) What are the six global verdicts? (`TE_MODULE_LEXX`, Stage 9) Why is the intention vector never S₀? (`02_COMPATIBILITY_PROFILE §6`)
- CASEWORK: what is the wave boundary and why are relevance decisions deferred? (`TE_CASEWORK §4`) What must a finding record? (`§5`) What are the three constants in every report, and why? (`§6`, `README.md`) What does an investigation require before closure? (`TE_INVESTIGATION §5`)

**Complete when** a validated run exists with a recorded review, and you can explain each of the report's status fields to a professional who has not read the framework.

## Level 4: maintainer and contributor (about two days)

**Goal.** Change the repository without breaking its integrity, and propose an extension in the form the framework prescribes.

**Readings.**
- [07_MAINTAINERS_GUIDE.md](07_MAINTAINERS_GUIDE.md); `CONTRIBUTING.md`; `FRAMEWORKS/README.md` (integrity and register patch); `TE_SYMBOL_CANON §3` (reservation procedure); `TE_OBSERVER §8` (evolution protocol: proposal formats for a new framework, an extension, a correction); `TE_CORE §0.3` (modules as domain instances)

**Exercises.**
1. Clone, run `make test` and `make check`, and read what each check verifies.
2. Change one character in a canonical file locally, run `make check`, and follow the failures through manifest, lock and compatibility profiles; then revert.
3. Regenerate `dist/` after editing `tools/loading_set.json` (for example a trigger phrase) and inspect the diff.
4. Draft a `[FRAMEWORK EXTENSION PROPOSAL]` or `[NEW FRAMEWORK PROPOSAL]` in the OBSERVER format for a domain the modules do not yet cover, with the isomorphism check `CONTRIBUTING.md` requires and any new symbol taken through the Canon's reservation procedure.

**Complete when** exercise 2 ends with every check green again and exercise 4 names its confidence grade in the proposal, as the contributing guide asks.

## Keeping the training honest

The self-checks point to sections rather than giving answers so that the answer is read in the canonical text. Where this handbook and the text disagree, the text is right. And the framework's own closing test applies to the trainee: a session that found no bias in itself has probably not looked (`TE_OBSERVER §4.2.5`, on the absence of disconfirmant data as a signal).
