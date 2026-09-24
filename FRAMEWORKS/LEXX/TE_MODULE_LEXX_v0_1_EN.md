# TE_MODULE_LEXX v0.1

## Ordinative Validation of Agreements — operational pipeline

### Understanding an agreement, finding every flaw, inverting the intention vector, formulating the counter-proposal

**Version**: 0.1 (first issue)
**Current executive profile (2026-09-17)**: for new runs apply `03_PRE_PILOT_PROTOCOL.md` and the contract `v0_2_alpha3/schemas/lexx_output.schema.json`. The illustrative JSON of §9 and the v0.1 enforcement declarations describe the v0.1 issue; the alpha.3 profile completes their checks and separates technical verification from semantic review. Method 0.1; runtime 0.2.0-alpha.3; the empirical cycle on real agreements is item (b) of §10 and runs under `03_PRE_PILOT_PROTOCOL.md`.
**Reading prerequisite**: `00_FOUNDATIONS.md` (axioms A1–A4, canon map, safeguards P1–P3, ethical constraint).
**Placement**: on-demand operational framework of the TE. LEXX executes inside the Ordinative Sciences: the TE canon is its theory and its runtime.
**Mandatory canonical stack**: TE Bootloader + TE Protocols + TE Core/OST; Symbol Canon for every use of formal notation; SVP as first gate. SA, PA, OCT, LENS, P-PRO, VERI and OBSERVER are invoked at the stages that name them in §1 and keep their own version limits.
**Compliance profile**: `02_COMPATIBILITY_PROFILE.md` and `lexx_compatibility_profile_v0_1.json` are binding for versions, degraded modes and stop conditions.
**Rule of precedence**: if a local instruction diverges from the loaded ordinative canon, execution stops at that point, logs the incompatibility and requests alignment.
**Mode of use**: instruction for an executor LLM. The executor receives: this module + `00_FOUNDATIONS.md` + the legender §[L] + one agreement per run. Output: the JSON according to the schema in §[9], and that alone.

---

# [L] LEGENDER (local executive closure — every symbol used is defined here)

Every symbol used is recalled here with its local meaning. This closure serves execution; the canonical definitions live in the TE Symbol Canon and in the ordinative source of each symbol, which prevail in case of divergence.

| Symbol | Name | Operational meaning in LEXX |
|---|---|---|
| `𝓘 = ⟨Σ, R, Φ⟩` | ordinative set | the agreement: Σ clauses/parties, R field of intersections, Φ emergent function |
| `ι` | invariant (SA) | what a clause legitimately gives, stripped of its domain |
| `P` | payload (SA, 2nd channel) | what the clause *does to the recipient* while giving ι: triples ⟨operation; target; marker⟩ (A_deg, SR_loop, I_sem/ι₉, shame-gradient, authority-gradient, unfalsifiable-fortress) |
| `𝔉_d / 𝔉_eff` | declared / effective function | what the clause says it does vs what it does within the complete set |
| `Δ_𝔉` | function gap | `𝔉_eff − 𝔉_d`; sign and magnitude are the finding |
| `v` | vector | declared vs effective direction of the clause |
| `τ_ph` | temporal phase | ascending / descending / bifurcation / cyclic, of the content |
| `I` | identity vector | the proposer's actual motive, reconstructed by tomography from the payloads (an inferred quantity, graded S₁–S₃) |
| `𝓚⁵` | coherence vector (PA) | 5 dimensions of coherence; used here to measure the proportion between the parties |
| `κ` | compatibility (PA) | compatibility index between the parties' vectors [0,1] |
| `λ_L` | Lyapunov exponent | sign of the relationship's trajectory: <0 converges, >0 diverges |
| `CVI` | correction viability index | (reduction of Δ_A)×(feasibility)×(sustainment), threshold 0.5 (from TE_OBSERVER) |
| `S₀…S₃` | confidence grades | S₀ citation/verified datum · S₁ triangulable inference · S₂ interpretation · S₃ hypothesis |
| `π(ι,𝔻)` | re-contextualisation | projects the invariant into a target domain/form (counter-proposal engine) |
| `V-OM / V-AM / V-IN / V-TEMP` | flaw vectors | omission (Φ/R gap) · ambiguity of Σ (two literal readings with materially different outcomes) · intersection of R that the clauses leave open (the white space between them) · dependence on temporal order |

**Symbols imported from the canon** (recalled here with their referent, so that execution is locally closed and theoretical authority rests with the canon):

| Symbol | Canonical referent | Use in LEXX |
|---|---|---|
| `C`, `I`, `K` | TE collapse `E = Φ(C,I,K)` | coherent content · identity vector (= the motive, what LEXX calls the «intention vector») · context |
| `𝒦_p`, `U`, `↪` | Semantic Algebra | pure pre-vectorial knowledge · expressive functor (to say = to project) · «is contained as inherited structure» (the inclusion that makes partial tomography possible) |
| `ι₁` | SA invariant #1 | non-expressibility of the source: `U⁻¹ ∄` — the perfect inversion E→I does not exist; hence the discipline of grades |
| `ι₆` | SA invariant #6 | *Controfase* (counter-phase): phase shift, **not** opposition (used for the analyst's hygiene, Stage 7) |
| `ι₇` | SA invariant #7 | teleological inversion: the vector evokes the expression — grounds the E→I reading |
| `ι₉` | SA invariant #9 | semantic inversion: `sign(𝔉_d) = −sign(𝔉_eff)` — a term whose operational meaning is reversed (= I_sem in PPRO) |
| `κ_c` | SA co-operator | connotation: root↔rendering divergence that **justifies** the extraction of the payload `P` (etymological step, Stage 1) |
| `A_deg, SR_loop, A_lock` | PPRO algorithms | degradation of position · stimulus–response loop · capture in a sealed reading |

> **Executive-closure note.** The legender covers the symbols *used*. In v0.1 𝓚⁵/ρ/Δ_A appear as symbols and the corresponding fields are ordinal bands and signs with the criterion exhibited (§ Stages 4–5). The canonical engines — PA (the five dimensions of 𝓚⁵, the κ/ρ formulas) and the Lyapunov dynamical system (phase space, `Δ_A` of the CVI) — attach in v0.2 and are the sole path from bands to measures.

**Scenario sequence (6 phases)**, whenever a flaw has to be shown executable: identification → attachment to the lever clause → literal execution → consolidation → defence of the position → outcome. Each phase cites the letter of the text.

---

# [0] PURPOSE, PERSPECTIVE, GATE

## 0.1 Perspective (mandatory)

Every analysis declares which party it works for: `proponente | destinatario | neutra` (proposer | recipient | neutral). The perspective determines what counts as a flaw and what counts as a feature (an asymmetry in the proposer's favour is a flaw for the recipient, a negotiation note for the proposer).

## 0.2 Gate (operated by the orchestrator)

- **Mode.** `diagnostica` (default): understands, validates, inverts, counter-proposes. `laboratorio`: admitted on documents labelled `ADV_` with a registered SHA-256 seal — a precondition the orchestrator verifies.
- **Structural refusal.** If the request is to draft an agreement whose letter works against a third party who is meant to sign it unaware, LEXX stops (ethical constraint, `00_FOUNDATIONS.md §4`) and offers the defensive reading of that third party's position.
- **Residual risk.** Ownership of the document and post-delivery use of the counter-proposal lie with the user; the executor records both as residual risk in `insed.limiti`.

---

# [1] THE PIPELINE — 10 stages

Each stage names the canon tool it invokes (see `00_FOUNDATIONS.md §2`). Each stage deposits into one slot of the §[9] output (the schema is the mirror of the pipeline: every stage has its slot and every slot its stage).

## STAGE 0 — INSED · provenance and birth of the act [SVP]

- Provenance, version/status (signed/proposal/draft), hierarchy of sources, missing linked texts, limits.
- **Formation**: double approval under artt. 1341-42 of the Italian Civil Code (c.c.), form required by the type of act (ad substantiam under art. 1350 c.c. for real estate), registration (and its *consequence*: nullity where provided), powers/standing of the signatory.
- **Qualification of the parties** (mandatory): `B2C | B2B | C2C | PA`. If B2C, unfairness is assessed also under artt. 33-36 of the Italian Consumer Code (Cod. Cons.) (protective nullity, raised by the court of its own motion): double signature does not cure it.
- `perimetro_analisi`: `documento_solo` (default) | `documento_sistema`. External law goes into `mitigazione_esterna` with a grading rule: automatic integration/substitution ex lege (artt. 1339, 1374, 1419 co. 2 c.c.) → solid mitigation, maximum grade S₂; contested mitigation → the grade holds. Each external rule is recorded, then weighed on its own strength.

## STAGE 1 — Two-channel STRIP [OST + SA]

The canonical operator is **two-channel**: `S(E) = ⟨ι, P⟩` (invariant + payload). The complete STRIP annotation in LEXX expands the two channels into the attributes needed by the downstream stages — `⟨ι, 𝔉_d, 𝔉_eff, Δ_𝔉, v, R, τ_ph, P⟩` — on the canonical operator: ι is channel 1, P channel 2; the other six attributes are record annotation.

- **Etymological step + κ_c (channel 2)**: go down to the root of the load-bearing term and measure the **root↔rendering divergence** (co-operator `κ_c`). This divergence is what *justifies* the extraction of the payload `P` and makes it controllable: where root and use coincide, `P = ∅`; where the term is bent against its root (ι₉), there is payload.
- `ι` = the legitimate invariant the clause serves. `P` = the control payload (channel 2): a clause that gives a real service *and* exercises a control is a **Device** (⟨ι≠∅, P≠∅⟩) — the case the two-channel operator is built to see.
- Then build the triple: Σ (clauses), R (intersections — the junction between clauses whose overlap the set leaves open), **Φ_declared vs Φ_effective**.

## STAGE 1.5 — Arithmetic and temporal consistency (mandatory)

- Arithmetic: every number against every derived quantity (instalment × n = total, deposit = n monthly instalments, percentages on their base, durations).
- Temporal: assumptions valid today vs assumptions due to lapse (deadlines, cited regimes, indices, aged templates). Each entry carries the document date and the textual reference; an entry is written when both date and reference are present (P3).

## STAGE 2 — Flaw VECTORS [the three vectors + V-TEMP]

For each candidate flaw: `vettore_primario` ∈ {V-OM, V-AM, V-IN, V-TEMP}, optional `vettore_concorrente`. Citation mandatory, grade S₀/S₁.

- **V-AM** applies to a **divergence of outcomes**: two literal readings with materially different consequences.
- **V-IN** is LEXX's vector of election: the flaw in the white space between two clauses. It is found with the cross-STRIP of the whole set.
- **V-TEMP** (new in LEXX): correctness dependent on order/time — clockwork forfeitures, windows, races between performances, transitional regimes that expire.

## STAGE 3 — INVERSION E→I · the intention vector [TE + LENS + PPRO + SA] ⟵ core

The core task of LEXX. Reconstruct the proposer's identity vector by tomography.

- **Tomography**: join the payloads `P` extracted at Stage 1 across independent clauses. The vector `I` is the direction on which the payloads converge. Each clause is a projection; the vector is the volume that explains them all.
- **LENS discipline** (structure before label): the formulation is always «the text allows whoever holds this position and these accesses to …», the integral before the label. Never «X wants»; always «the structure orients towards».
- **PPRO scan**: detect in the text A_deg (degradation of the other party's position over time), SR_loop (induced stimulus–response), I_sem (semantic inversion ι₉: a term whose operational meaning is reversed — a «right of withdrawal» that keeps the party bound, «ownership» of data whose every use needs the counterparty's consent), A_lock (capture in a sealed reading).
- **Output**: `vettore_dichiarato` (what the agreement says it wants to do) vs `vettore_effettivo` (where the tomography converges), with `Δ_vettore`. **Grade**: S₁–S₃ (P2); **S₁** when ≥3 independent clauses whose payloads converge **on the same vector** (different payloads pointing to the same direction count; this is the normal case); otherwise S₂/S₃. Where the payloads scatter: empty field, and the limit written in `nota_limite` (P3). The executor **lists in `tomografia` the clauses→payloads** that support the vector, so that the grade can be checked by third parties.

## STAGE 4 — PROPORTION [PA]

- Estimate the **disproportion** between the parties' vectors as an **ordinal band** `κ_banda ∈ {alta | media | bassa}` (alta = balanced parties; bassa = strongly asymmetric), **exhibiting the criterion**: which levers (discretion, self-help remedies, forum, indeterminacy) each party holds.
- Equity class: `equilibrata` | `asimmetrica_dichiarata` (in the recitals, Δ_𝔉=0 → negotiation note) | `asimmetrica_occulta` (produced by R alone, with the recitals silent on it → flaw).
- Asymmetry checkpoint: an asymmetry is recorded as a V-IN flaw on one condition: the real flow presupposed by the text contradicts it textually (recital × clause).

## STAGE 5 — TRAJECTORY [Lyapunov / OBSERVER]

- Estimate the **sign** of `λ_L` for the governed relationship (`neg | pos`): does the sequence of performances converge (the relationship holds, `neg`) or diverge (the agreement feeds the conflict, `pos`)? Argue the sign from the text (which clause pushes the trajectory in which direction); the field is filled when the text supports the argument, and stays empty otherwise (P3).
- Map the **bifurcations**: trigger clauses (automatic default, ipso iure termination, forfeitures) and their proximity to the penalty clause (`grilletto_vicino`, with citation of the trigger).
- For each flaw, `CVI_banda ∈ {alta | media | bassa}` = viability of the correction (alta = a minimal patch suffices; bassa = structural rewriting is needed), with the criterion exhibited.

## STAGE 6 — CLASS and RESIDUE [OCT + VERI]

- Φ-test / OCT class per clause: **A** admissible (produces emergent function) · **B** sterile (form alone — cardboard protection) · **C** degenerative (function against the system) · **D** invalid (null/unenforceable ex lege).
- Residue of the protections (VERI): does the protective clause work against a hostile / insolvent / absent counterparty? Scale **0** statement of intent · **1** works with a cooperative counterparty · **2** works at a cost/procedure for the protected party · **3** self-sufficient. Residue 0–1 → V-OM of remedy.

## STAGE 7 — CONTRARY TEST and hygiene [Controfase]

- For each candidate flaw: `opposto_valido` (is there a legitimate alternative reading that neutralises it?), `interpretazione_alternativa` (which one, and why it fails — or it holds, and then the candidate drops to S₂/bifurcation). Include the applicable hermeneutic canon (artt. 1362-1371 c.c.; **contra proferentem** under art. 1370 c.c. and art. 35 Cod. Cons.): if the canon resolves the ambiguity against the drafting party, the bifurcation is not neutral — the flaw is assigned to the party the canon disfavours.
- **P-AI on the analyst** (Controfase): am I confirming the client's fear? am I demonising the proposer where the task is to describe the structure? am I inflating S₂ to S₀? Every bias detected goes into `meta_pai`.

## STAGE 8 — COUNTER-PROPOSAL [π + neutralisation + Lyapunov] ⟵ active deliverable

When `prospettiva ≠ neutra`, or on request. For each load-bearing flaw, one of two moves:

- **π(ι, 𝔻_fair)** (rewriting): take the legitimate invariant `ι` the clause *should* serve and re-project it in a fair form (𝔻_fair, the fair target domain). **Verifiable round-trip**: the executor **emits in the output** the re-strip `S(counter-proposal) = ⟨ι′, P′⟩` (the two channels extracted *from the rewriting*), so that a third party can check that `ι′ ≈ ι` and `P′ = ∅`. The field `round_trip_ok` counts when the exhibited re-strip accompanies it; the re-strip is what the orchestrator checks. If `P′ ≠ ∅`, the rewriting has relocated the control: redo it in a second orchestration pass.
- **Neutralisation by junction** *(the LEXX drafting extension; Controfase is the hygiene function of Stage 7)*: where the predatory clause resists rewriting, add a junction clause that makes its **lever irrelevant**. A *counter-right* that cancels the lever (e.g. «withdrawal without penalty») is **functional opposition**: legitimate, and named as such in `tipo`; the junction shifts the phase — it changes the boundary condition so that the lever loses its purchase. `tipo` records which of the two is used.
- **Trajectory check**: the counter-proposal is valid when it inverts the **sign** of `λ_L` (from `pos` to `neg`) or keeps it `neg`, with the argument exhibited. Stabilising the trajectory is the test of the rewriting.
- Every counter-proposal **is born coupled to its flaw** in the same block (atomic disarmament): each flaw brought to light carries its reformulation.

## STAGE 9 — VERDICT

`accordo_solido` (Φ_eff ≈ Φ_d; every flaw found is marginal) · `falle_puntuali` (isolated flaws, minimal patch) · `falle_strutturali` (flaws in R, requiring rewriting) · `device` (Φ_eff systematically against Φ_d; effective vector ≠ declared vector, with a wide Δ_vettore) · `degenerato` (class C/D prevailing) · `fortezza_valida` (asymmetry declared in the recitals and legitimate: a negotiation note). The verdict carries the criteria with the name.

---

# [2] SCORING RUBRIC (for empirical validation)

Hit (clause+mechanism) = 1 · Absorbed = 0.5 · Miss = 0 · **Explicit FN = 0.1** (declaring «I did not find X» is worth more than silence) · **Silent miss = −0.25** (silence has a cost) · FP on decoy = −2 · **Unmatched citation (string-match failed) = −2 and failed run** (P1). The orchestrator verifies every `citazione_letterale` against the source before scoring.

---

# [9] OUTPUT FORMAT (JSON, mandatory — mirror of the pipeline)

```json
{
  "accordo": "...",
  "versione_modulo": "LEXX v0.1",
  "prospettiva": "proponente|destinatario|neutra",
  "modalita": "diagnostica|laboratorio",
  "insed": {
    "versione": "...", "stato": "...", "qualificazione_parti": "B2C|B2B|C2C|PA",
    "formazione": {"doppia_approvazione": "...", "forma_richiesta": "...", "registrazione": "...", "poteri_firmatario": "..."},
    "perimetro_analisi": "documento_solo|documento_sistema", "limiti": ["..."]
  },
  "strip": [{"clausola": "...", "citazione": "...", "iota": "...", "f_dichiarata": "...", "f_effettiva": "...", "delta_f": "...", "payload": ["op;target;marker"], "kappa_c_divergenza": "root↔rendering: where/how much", "tau_ph": "..."}],
  "campo_relazionale_R": [{"clausole_in_intersezione": ["...", "..."], "giunzione": "what the combination adds to the clauses taken singly", "citazioni": ["...", "..."]}],
  "phi_accordo": {"dichiarata": "what the agreement says it does", "effettiva": "what it does as a system", "delta": "the Φ gap at agreement level"},
  "consistenza": {"aritmetica": [{"verifica": "...", "esito": "coerente|incoerente"}], "temporale": {"valide_oggi": ["..."], "non_valide_domani": ["..."]}},
  "falle": [{
    "id": "FX-1", "vettore_primario": "V-OM|V-AM|V-IN|V-TEMP", "vettore_concorrente": null,
    "clausole": ["..."], "citazione_letterale": "...",
    "delta_f": {"dichiarata": "...", "effettiva": "..."},
    "scenario_6_fasi": "...", "grilletto_vicino": "citation of the trigger clause",
    "test_contrario": {"opposto_valido": false, "interpretazione_alternativa": "...", "canone_ermeneutico": "e.g. contra proferentem 1370", "esito": "confermata|declassata|scartata"},
    "classe_oct": "A|B|C|D", "dote_residuo": "0|1|2|3",
    "lyapunov": {"lambda_segno": "neg|pos|vuoto", "argomento_segno": "...", "biforcazione": "..."}, "cvi_banda": "alta|media|bassa",
    "mitigazione_esterna": "...",
    "grado": "S0|S1|S2|S3", "assorbita_in": null,
    "controproposta": {"tipo": "riscrittura_pi|neutralizzazione_giunzione|contro_diritto", "forma_equa": "...", "ri_strip": {"iota_primo": "...", "payload_primo": "empty if the payload has dropped"}, "lambda_post": "neg|pos", "argomento_lambda_post": "..."}
  }],
  "vettore_intenzione": {
    "dichiarato": "...", "effettivo": "...", "delta_vettore": "...",
    "tomografia": ["clause→converging payload", "..."],
    "lens": "what the text allows whoever holds this position and these accesses to do",
    "ppro": ["A_deg|SR_loop|I_sem|A_lock: where"],
    "grado": "S1|S2|S3", "nota_limite": "what the text leaves open (P3)"
  },
  "proporzione": {"kappa_banda": "alta|media|bassa", "criterio": "which levers each party holds", "classe_equita": "equilibrata|asimmetrica_dichiarata|asimmetrica_occulta"},
  "lyapunov_globale": {"lambda_segno": "neg|pos|vuoto", "argomento": "what pushes the trajectory of the relationship, and how"},
  "non_falle_verificate": [{"clausola": "...", "sospetto": "...", "filtro_decisivo": "...", "perche_non_falla": "..."}],
  "note_negoziali": [{"clausola": "...", "nota": "..."}],
  "verdetto_generale": "accordo_solido|falle_puntuali|falle_strutturali|device|degenerato|fortezza_valida",
  "tre_mappe": {"cosa_dice": "the explicit, in plain English", "cosa_non_dice": "relevant omissions", "cosa_dice_senza_dirlo": "the effective vector and the balances of power"},
  "meta_pai": {"bias_rilevati": ["..."], "note_trasparenza": "..."},
  "_verifica_orchestratore": {"citazioni_riscontrate": "FILLED IN BY THE ORCHESTRATOR", "round_trip_controproposte": "FILLED IN BY THE ORCHESTRATOR"}
}
```

Field identifiers are canonical and language-independent; they match the runtime schema.

**Output rules**:
- **Mirror property and its exception.** Every stage 0–9 has a slot: INSED→`insed`, STRIP→`strip`+`campo_relazionale_R`+`phi_accordo`, consistency→`consistenza`, vectors→`falle[].vettore_primario`, inversion→`vettore_intenzione`, proportion→`proporzione`, trajectory→`falle[].lyapunov`+`lyapunov_globale`, class/residue→`falle[].classe_oct`/`dote_residuo`, contrary test→`falle[].test_contrario`+`meta_pai`, counter-proposal→`falle[].controproposta`, verdict→`verdetto_generale`. **`tre_mappe` and `non_falle_verificate` are post-pipeline syntheses** drawn from the whole output; they sit beside the mirror.
- **Enforcement of the safeguards.** `vettore_intenzione.grado` takes S₁, S₂ or S₃ (P2, checked at schema level). Every statement carries a matchable citation or an anchored slot (P1) — **the orchestrator fills in the string-match check and the round-trip in `_verifica_orchestratore`**; an LLM-only run leaves those two fields empty. A field is written when the text supports it; otherwise it stays empty with a `nota_limite` (P3).
- **Mandatory**: `qualificazione_parti`, `perimetro_analisi`, `prospettiva`, `modalita`. JSON only. Malformed output: one regeneration, then failed run.

---

# [10] VERSION NOTES

**v0.1** (2026-08-20) — first issue. Core: E→I inversion by tomography (Stage 3), integration of the whole canon (OST skeleton, SA two-channel operator, PA proportion, OCT class, Lyapunov trajectory, Controfase hygiene, SVP/LENS/PPRO/VERI tools), π counter-proposal engine with verifiable round-trip (Stage 8). Enforcement (requirements that emerged from the expert assessments of the LEX — the LEX project by a student of the Hypervisor, a separate, unpublished project, is the seed and prior art of LEXX; the LEX has already been used in the field on real corporate documentation, beyond laboratory pilots): intention graded S₁–S₃ (P2, at schema level), fourth vector V-TEMP, silence priced at −0.25, contra proferentem in the contrary test, consumer qualification in INSED.

**Architecture decision 2026-09-16** — LEXX is registered exclusively as a native framework of the TE and of the Ordinative Sciences. The legender is reclassified as local executive closure; canonical hierarchy, mandatory stack and stop rule in case of incompatibility are introduced. The pipeline and the v0.1 performance are those of the first issue.

**v0.1 — revision** (same day). Adversarial review on 3 axes (compliance with the requirements of the expert assessments, fidelity to the canon, executability): 18 defects found and corrected in v0.1: (1) legender closed over the canon symbols (ι₁/ι₆/ι₇/ι₉, C/K, 𝒦_p/U/↪, κ_c); (2) schema made mirror-complete — slots `campo_relazionale_R`, `phi_accordo`, `lyapunov_globale` added, and `tre_mappe`/`non_falle_verificate` defined as post-pipeline syntheses; (3) κ/CVI/λ rendered as **bands/signs** with the criterion exhibited; (4) safeguards labelled by **enforcement level** — P2 active at schema level, P1 a requirement on the orchestrator (attached in v0.2), P3 enforced on the fields the schema checks; verification fields moved to `_verifica_orchestratore`, filled in by the external verifier; (5) counter-proposal round-trip made verifiable (the executor **emits** the re-strip); (6) S₁ threshold reconciled (different payloads converging on the **same vector**); (7) Controfase-as-weapon renamed «neutralisation by junction» (the LEXX drafting extension; the counter-right is named as functional opposition); (8) the STRIP 8-tuple defined as an annotation of the canonical two-channel operator; κ_c as the justification for the extraction of P.

**To do (v0.2)** — full enforcement requires: (a) the **orchestrator** (string-match, gate, round-trip) attached as a component; (b) the **empirical cycle** with sealed ground truth + decoys on real agreements; (c) the **quantitative engines** PA and Lyapunov (§[L], executive-closure note); (d) `⊗` and the pre-output Φ-test of OCT/Bootloader; (e) reservation of the notation (8-tuple, use of ι₆) via the Symbol Canon if promoted; (f) renaming of the key `meta_pai.note_trasparenza` to `note_metodo`, in a single release with schema, runtime and alpha tests (the key is inherited from `v0_2_alpha3/schemas/lexx_output.schema.json`).
