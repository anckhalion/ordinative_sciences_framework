# LEXX — Ordinative Validation of Agreements

**If this folder reaches you in a new context, start here.**

**Operational update 2026-09-17:** name **LEXX**, method **0.1**, current runtime **0.2.0-alpha.3**. For new runs, read `03_PRE_PILOT_PROTOCOL.md` and use `v0_2_alpha3/`. `release.json` keeps the two versions separate. Earlier runtimes are historical and sit outside this repository; no real case has been validated yet.

LEXX reads a written agreement in order to do three things: (1) understand it and evaluate it as a system, (2) identify the vulnerabilities the analysis substantiates, (3) **invert the collapse** — infer the vector the text structurally enables and its possible gap from what is declared — and, where required, formulate a **counter-proposal**. Exhaustiveness lies outside its guarantee; the subjective intention of the proposer lies beyond what the text alone can prove.

It is the original vision of the LEX realised with the full canon of the Ordinative Sciences (TE, OST, PA, SA, OCT, Controfase, Lyapunov). The LEX project by a student of the Hypervisor — a separate, unpublished project — is the seed and prior art; the LEX has already been used in the field on real corporate documentation, beyond laboratory pilots.

## Canonical placement within the TE

**LEXX is a native operational framework of the Technology of Expressions, registered at the same level as SVP, LENS, VERI, P-PRO, SCIMS and OBSERVER.** It is the domain instance through which the TE analyses agreements and other normative systems as ordinative sets, reconstructs the vector their structure makes possible, and formulates a coherent counter-proposal.

LEXX constitutes no autonomous theory and cannot be distributed as one apart from the Ordinative Sciences. Its canonical hierarchy is:

`Ordinative Sciences → TE/OST and shared canon → TE_MODULE_LEXX → domain applications`.

Four constraints follow:

1. no local LEXX axiom may derogate from the TE Core, OST or the Symbol Canon;
2. Bootloader, TE Protocols and the confidence grades remain the mandatory governance of execution;
3. SVP remains the initial gate, and the other TE frameworks are invoked at the declared stages;
4. any operational package of LEXX is solely a TE loading profile; it carries no self-sustained theoretical version.

The local legender closes the execution over the symbols actually in use; it confers on LEXX no ontological or methodological independence from the canon.

## Reading order

1. **`00_FOUNDATIONS.md`** — the four axioms (agreement = ⟨Σ,R,Φ⟩; text = collapse invertible by tomography; proportion measurable; agreement = trajectory), the **canon integration map** (each instrument → its task), the three safeguards of rigour (verified anchoring, intention never S₀, empty field), the ethical constraint. **Read it first: everything else is application.**
2. **`02_COMPATIBILITY_PROFILE.md`** — the conformity contract with the canon: versions, dependencies, degraded modes and halt conditions.
3. **`lexx_compatibility_profile_v0_1.json`** — the same contract in machine-readable form.
4. **`TE_MODULE_LEXX_v0_1_EN.md`** — the operational module: the local legender (executive closure over the symbols in use, under the canon), the 10-stage pipeline, the scoring rubric, the JSON output schema (mirror of the pipeline).
5. **`01_ANNOTATED_EXAMPLE.md`** — a short agreement taken through the whole pipeline: how the E→I inversion is built and how a counter-proposal comes into being.
6. **`03_PRE_PILOT_PROTOCOL.md`** — the current pilot contract: coverage, evidence/confidence, dependencies, double verdict and separate review of the counter-proposals.
7. **`v0_2_alpha3/`** — current runtime: full schema, verification of the actual files, cross-checks, reproducible package and hash-bound review. The earlier runtimes (alpha, alpha.2) are historical and sit outside this repository. The runtime is experimental infrastructure; empirical validation is the task of the pilot cycle.

## What sets it apart from the student's LEX

**Design intent; validated capability comes with the empirical cycle.** LEXX v0.1 has **zero empirical runs** (as the LEX at its beginnings): the table states what LEXX is *designed* to do beyond the LEX; the performance comparison belongs to the v0.2 empirical cycle:

| | LEX (student) | LEXX — *as designed, verification pending* |
|---|---|---|
| Core | document-level detection (reduced SA+OST) | **E→I inversion of the intention vector** by tomography (graded heuristic) |
| Proportion | absent | **PA** — disproportion as a **qualitative band** in v0.1 (quantitative engine in v0.2) |
| Time | static temporal validity | **Lyapunov** — direction of the trajectory (sign), bifurcations (qualitative in v0.1) |
| Counter-proposal | strategy options | **π(ι,𝔻) with the re-strip shown + check of the sign of λ** — the invariant survives, the payload falls |
| Enforcement | anchoring as a stated requirement | **P2 active at schema level** (intention never S₀); **P1** requires the orchestrator (outside v0.1); schema with the mirror property |
| Self-sufficiency | undefined symbols | **closed legender** over the symbols in use; the quantitative engines are declared external |

Each cell is a design direction; the performance measurement is the task of the v0.2 empirical cycle.

## Safeguards of rigour — and who enforces them in v0.1

A safeguard holds only when it names *who* executes it. In v0.1:

- **P2 — Intention is never S₀** — **active, at schema level**: the field `vettore_intenzione.grado` admits no S₀; the vector is always a graded inference (S₁ only when ≥3 clauses converge on the same vector). Verifiable without the orchestrator.
- **P1 — Verified anchoring** — **requirement of the orchestrator, outside v0.1**: the string-match of the citations and the round-trip of the counter-proposals are filled in by an external verifier (`_verifica_orchestratore`), never by the executor. The LLM-only run does not attest them.
- **P3 — The empty field stays empty** — **partial**: imposed at schema level (bands/signs, never uncalculated figures); the penalty on silence requires the empirical cycle (v0.2).

## Ethical constraint

A defensive and diagnostic instrument. No intention is imputed as fact (always in the LENS form: "what the text allows to whoever holds this position"). The counter-proposal is born disarmed. The inverse capacity (drafting against an unaware third party) is not a LEXX product. It does not replace legal counsel.

## State

**v0.1** — first release (2026-08-20). TE framework formulated; empirical validation cycle (sealed ground truth on real agreements) and threshold calibration scheduled for v0.2. Extension to other domains (policy, cyber, institutional agreements) to follow, with the same pipeline adapted in lexicon and unchanged in structure. **Architecture decision 2026-09-16**: every autonomous trajectory is excluded; LEXX remains natively and mandatorily internal to the Ordinative Sciences.

**v0.2-alpha runtime** — started 2026-09-16. JSON contract, dependency register, jurisdictional gate, evidence/confidence separation and external anchoring verifier available. The state remains experimental: no blind benchmark completed. This runtime sits outside this repository.

**v0.2.0-alpha.3 runtime** — pre-pilot revision of 2026-09-17. Completes Draft 2020-12 validation, binds the dependencies to controlled files and hashes, reintroduces the consistency stage in the schema, checks coverage/references/confidence, distinguishes text/system verdicts and creates the hash-bound review step for the counter-proposals. Semantic verification remains entrusted to a distinct review; the quantitative engines and the empirical calibration remain open. The base method keeps version 0.1; the current executive profile is declared in `03_PRE_PILOT_PROTOCOL.md`.

## Custody

At the birth of every new file or module: update this README and register the file (role, SHA-256) before considering it delivered. Any validation ground truth goes in `_SEALED/` with `rag_index:false` and is never shown to an executor. Every new version also declares its own compatibility matrix with TE Core, Bootloader, TE Protocols, OST, Symbol Canon and the algebras invoked.

## alpha.3 compatibility — 2026-09-17

Pin revision for Bootloader 7.1.1, Core 5.2.1 and Protocols 1.1. The capabilities of LEXX remain those of method 0.1: qualitative document analysis. The software keeps the alpha.2 controls; the alpha and alpha.2 runtimes are historical, unchanged, and kept outside this repository — `v0_2_alpha3/` is the one shipped here. The method remains 0.1. Corporate audit and investigative support are separate CASEWORK protocols (`CASEWORK/README.md`, `CASEWORK/TE_AUDIT_v0_1_EN.md`, `CASEWORK/TE_INVESTIGATION_v0_1_EN.md`). No real case validated.
