# LEXX — Ordinative Validation of Agreements

**If this folder reaches you in a new context, start here.**

**Operational update 2026-09-17:** name **LEXX**. Status: method **0.1** · runtime **0.2.0-alpha.3**, shipped as `v0_2_alpha3/`; the alpha and alpha.2 runtimes are archived outside this repository · validation on real cases is the task of the pilot cycle (`03_PRE_PILOT_PROTOCOL.md`; `release.json`: `empirical_runs_completed: 0`). `release.json` keeps the two versions separate. For new runs, read `03_PRE_PILOT_PROTOCOL.md` and use `v0_2_alpha3/`.

LEXX reads a written agreement in order to do three things: (1) understand it and evaluate it as a system, (2) identify the vulnerabilities the analysis substantiates, (3) **invert the collapse** — infer the vector the text structurally enables and its gap from what the text says of itself — and, where required, formulate a **counter-proposal**. Its findings are the vulnerabilities the text substantiates; the intention it reconstructs is a graded inference from the text.

It is the original vision of the LEX realised with the full canon of the Ordinative Sciences (TE, OST, PA, SA, OCT, Controfase, Lyapunov). The LEX project by a student of the Hypervisor — a separate, unpublished project — is the seed and prior art; the LEX has already been used in the field on real corporate documentation, beyond laboratory pilots.

## Canonical placement within the TE

**LEXX is a native operational framework of the Technology of Expressions, registered at the same level as SVP, LENS, VERI, P-PRO, SCIMS and OBSERVER.** It is the domain instance through which the TE analyses agreements and other normative systems as ordinative sets, reconstructs the vector their structure makes possible, and formulates a coherent counter-proposal.

LEXX is a domain instance of the Ordinative Sciences and travels with them. Its canonical hierarchy is:

`Ordinative Sciences → TE/OST and shared canon → TE_MODULE_LEXX → domain applications`.

Four constraints follow:

1. every local LEXX axiom conforms to the TE Core, OST and the Symbol Canon;
2. Bootloader, TE Protocols and the confidence grades govern execution;
3. SVP is the initial gate, and the other TE frameworks enter at the stages the module fixes;
4. every operational package of LEXX is a TE loading profile.

The local legender closes the execution over the symbols in use, under the canon.

## Reading order

1. **`00_FOUNDATIONS.md`** — the four axioms (agreement = ⟨Σ,R,Φ⟩; text = collapse invertible by tomography; proportion measurable; agreement = trajectory), the **canon integration map** (each instrument → its task), the three safeguards of rigour (verified anchoring, intention never S₀, empty field), the ethical constraint. **Read it first: everything else is application.**
2. **`02_COMPATIBILITY_PROFILE.md`** — the conformity contract with the canon: versions, dependencies, degraded modes and halt conditions.
3. **`lexx_compatibility_profile_v0_1.json`** — the same contract in machine-readable form.
4. **`TE_MODULE_LEXX_v0_1_EN.md`** — the operational module: the local legender (executive closure over the symbols in use, under the canon), the 10-stage pipeline, the scoring rubric, the JSON output schema (mirror of the pipeline).
5. **`01_ANNOTATED_EXAMPLE.md`** — a short agreement taken through the whole pipeline: how the E→I inversion is built and how a counter-proposal comes into being.
6. **`03_PRE_PILOT_PROTOCOL.md`** — the current pilot contract: coverage, evidence/confidence, dependencies, double verdict and separate review of the counter-proposals.
7. **`v0_2_alpha3/`** — current runtime: full schema, verification of the actual files, cross-checks, reproducible package and hash-bound review. The runtime is the pilot's working infrastructure.

## What sets it apart from the student's LEX

The table states what LEXX is designed to add to the LEX; the v0.2 empirical cycle measures the performance:

| | LEX (student) | LEXX |
|---|---|---|
| Core | document-level detection (reduced SA+OST) | **E→I inversion of the intention vector** by tomography (graded heuristic) |
| Proportion | — | **PA** — disproportion as a **qualitative band** in v0.1 (quantitative engine in v0.2) |
| Time | static temporal validity | **Lyapunov** — direction of the trajectory (sign), bifurcations (qualitative in v0.1) |
| Counter-proposal | strategy options | **π(ι,𝔻) with the re-strip shown + check of the sign of λ** — the invariant survives, the payload falls |
| Enforcement | anchoring as a stated requirement | **P2 active at schema level** (intention never S₀); **P1** requires the orchestrator (outside v0.1); schema with the mirror property |
| Self-sufficiency | symbols taken as read | **closed legender** over the symbols in use |

## Safeguards of rigour — and who enforces them in v0.1

The three safeguards — P1 verified anchoring, P2 graded intention, P3 empty field — and who executes each in v0.1 are in `00_FOUNDATIONS.md` [3].

## Ethical constraint

A defensive and diagnostic instrument; the ethical constraint is in `00_FOUNDATIONS.md` [4].

## State

**v0.1** — first release (2026-08-20). TE framework formulated; empirical validation cycle (sealed ground truth on real agreements) and threshold calibration scheduled for v0.2. Extension to other domains (policy, cyber, institutional agreements) to follow, with the same pipeline, its lexicon adapted and its structure kept. **Architecture decision 2026-09-16**: LEXX lives inside the Ordinative Sciences.

**v0.2-alpha runtime** — started 2026-09-16. JSON contract, dependency register, jurisdictional gate, evidence/confidence separation and external anchoring verifier available.

**v0.2.0-alpha.3 runtime** — pre-pilot revision of 2026-09-17. Completes Draft 2020-12 validation, binds the dependencies to controlled files and hashes, reintroduces the consistency stage in the schema, checks coverage/references/confidence, distinguishes text/system verdicts and creates the hash-bound review step for the counter-proposals. A distinct review carries the semantic verification. `03_PRE_PILOT_PROTOCOL.md` gives the current executive profile.

## Custody

At the birth of every new file or module: update this README and register the file (role, SHA-256) before considering it delivered. Any validation ground truth goes in `_SEALED/` with `rag_index:false` and stays sealed on the orchestrator's side. Every new version also carries its own compatibility matrix with TE Core, Bootloader, TE Protocols, OST, Symbol Canon and the algebras invoked.

## alpha.3 compatibility — 2026-09-17

Pin revision for Bootloader 7.1.1, Core 5.2.1 and Protocols 1.1. LEXX delivers qualitative document analysis. The software keeps the alpha.2 controls. Corporate audit and investigative support are separate CASEWORK protocols (`CASEWORK/README.md`, `CASEWORK/TE_AUDIT_v0_1_EN.md`, `CASEWORK/TE_INVESTIGATION_v0_1_EN.md`).
