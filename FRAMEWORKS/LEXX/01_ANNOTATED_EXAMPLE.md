# LEXX — Annotated Example

## A short agreement through the entire pipeline

**Purpose of this file**: to show *how* LEXX inverts the intention vector and builds a counter-proposal, beyond the list of *what* it finds. It is a teaching walk-through: no sealed ground truth is attached, so it is not a validation run. The agreement is synthetic and deliberately simple; the clauses are numbered for anchoring.

---

## The document (source)

> **COLLABORATION AGREEMENT — "Vetrina Pro"**
> **C1.** The Supplier grants the Client a listing in the *Vetrina Pro* section of the portal, with priority visibility.
> **C2.** The fee is € 1,200.00 per year (one thousand two hundred/00), payable in a single instalment upon activation.
> **C3.** This agreement renews tacitly from year to year, save for termination to be communicated with **reasonable notice** before the expiry date.
> **C4.** The Supplier may modify the features of the *Vetrina Pro* service at its own discretion, giving notice of the change on the portal.
> **C5.** In the event of late payment of even a single instalment, access to the section is suspended and the annual fee remains due in full.
> **C6.** Any dispute falls within the jurisdiction of the court of the place where the Supplier has its registered office.
> **C7.** *(decoy)* The Supplier guarantees a support response time within 2 business days; the recitals record that priority assistance is **consideration for the fee** and is not available to free accounts.

*Perspective of the analysis: `destinatario` (the Client, as recipient). Qualification: `B2B` presumed; where the Client is a professional adhering to a pre-drafted form, consumer-law controls do not apply, while artt. 1341-42 of the Italian Civil Code still do.*

Field identifiers are canonical and language-independent; they match the runtime schema.

---

## How LEXX reads it — stage by stage

### Stage 0 — INSED [SVP]
- **State**: proposal on a form pre-drafted by the Supplier → unilateral clauses are candidates for the artt. 1341-42 screening (double signature for onerous clauses).
- **Qualification of the parties**: B2B (no Italian Consumer Code (Cod. Cons.) shield), yet C4/C5/C6 are clauses in favour of the drafting party → **art. 1341 co. 2**: without specific written approval they are ineffective. *Formation slot: the double signature is absent from the text supplied → a remedy flaw for the Supplier, a shield for the Client.*
- **Perimeter**: `documento_solo` (document only); integration under artt. 1339/1374 goes into `mitigazione_esterna` (external mitigation).

### Stage 1 — TWO-CHANNEL STRIP [OST + SA]
Example on two clauses (the invariant ι and the payload P):

| Clause | ι (legitimate invariant) | P (control payload) | Δ_𝔉 |
|---|---|---|---|
| **C3** "reasonable notice" | the right to terminate exists | **I_sem (ι₉)**: a right to terminate that does not release — the term is undetermined, so the termination is contestable and the renewal fires | 𝔉_d = "you can leave"; 𝔉_eff = "you leave only if you guess a deadline the Supplier never set" |
| **C5** double bind | protection of payment | **A_deg + fortress**: suspends the service *and* keeps the receivable alive → the Client pays for a service it does not receive | 𝔉_d = "late-payment penalty"; 𝔉_eff = "collection without counter-performance" |

- **Φ_declared** of the agreement: "priority visibility against an annual fee".
- **Φ_effective**: "a self-protected recurring collection, with the Client's exit made difficult and the service modifiable at discretion".

### Stage 1.5 — Consistency
- Arithmetic: C2 € 1,200 = 1,200 in words ✓ (no figures/words divergence here).
- Temporal: C3 tacit renewal → **V-TEMP**: the termination window is undetermined (τ_ph: recurrent bifurcation at every expiry).

### Stage 2 — VECTORS
- **F1 · V-AM (C3)**: "reasonable notice" — two readings with divergent outcomes (30 days? 90?). A divergence of outcomes, which is the V-AM criterion; vagueness alone would not qualify. Grade S₀ (direct quotation).
- **F2 · V-IN (C4 × C5)**: intersection. C4 lets the Supplier hollow out the service "at its own discretion"; C5 keeps the entire fee due regardless. Neither clause on its own is illegitimate; **the combination** allows the service to be degraded while everything is collected. Grade S₁ (triangulation C4+C5).
- **F3 · V-OM**: no remedy mechanism for the Client if the service drops (protection absent).

### Stage 3 — E→I INVERSION · the intention vector [core]
**Tomography** (union of the payloads P across independent clauses):

- C3 → payload: *make exit costly* (undetermined termination).
- C4 → payload: *preserve the freedom to reduce the counter-performance*.
- C5 → payload: *secure collection regardless of the service delivered*.
- C6 → payload: *shift the cost of litigation onto the Client* (Supplier's forum).

Four independent clauses converge on the same direction: **maximise and lock in the recurring collection, while minimising the obligation to deliver value and the cost of any conflict.**

- **LENS discipline** (no mind-reading): *the text allows a supplier in this position to collect a self-protected annual fee while reducing the service at discretion and discouraging both exit and litigation.* The description stays on the structure, which points anyone occupying that position in the same direction.
- `vettore_dichiarato` (declared vector): "sell priority visibility". `vettore_effettivo` (effective vector): "secure a recurring rent decoupled from the counter-performance". `Δ_vettore`: wide.
- **Grade: S₁** (≥3 convergent clauses, solid tomography). *Limit note (P3): from the text alone it stays undecidable whether this is deliberate strategy or an inherited standard template; the field stays at the structural level.*

### Stage 4 — PROPORTION [PA — qualitative]
- Imbalance of the vectors: the Supplier holds discretion (C4), self-help (C5), forum (C6) and an indeterminacy in its own favour (C3); the Client holds a certain payment obligation and no symmetric remedy. **`κ_banda: bassa`** (low band; criterion shown: four levers to the Supplier, zero symmetric remedies to the Client — a *band*, no figure: the quantitative PA engine is v0.2). **Class: `asimmetrica_occulta`** (hidden asymmetry) — no clause declares the imbalance in the recitals; R produces it.

### Stage 5 — TRAJECTORY [Lyapunov]
- `λ_L > 0`: the relationship diverges. Every reduction of the service (C4) without remedy (V-OM) raises dissatisfaction, while exit is costly (C3) and default is punitive (C5) → the Client stays dissatisfied and bound: growing instability.
- **Bifurcation**: C5 (`grilletto_vicino`, near trigger: "even a single instalment … remains due in full") is the trigger clause. `CVI_banda: alta` (high band; criterion: one junction clause and one rewrite of C3 suffice, with no structural rewrite of the agreement).

### Stage 6 — CLASS and RESIDUE [OCT + VERI]
- C5: class **C** (degenerative — function against the system of the relationship). C4: **B** tending to **C** (discretion without counterweight). C3: **A** with a defect of determinacy.
- Residue of the Client's protections: **0** (no real protection) → remedy V-OM confirmed.

### Stage 7 — CONTRARY TEST [Controfase] + the decoy C7
- F1 (C3): `opposto_valido`? the words "reasonable notice" could be integrated by a judicial standard of reasonableness. **Interpretive canon**: art. 1370 **contra proferentem** — the indeterminacy is resolved *against the drafting party* (the Supplier). Outcome: **confirmed** (`confermata`); the bifurcation is resolved, and the flaw is charged to the drafting party.
- **C7 — the decoy (discrimination)**: C7 *triggers suspicion* — "priority assistance is consideration for the fee and is not available to free accounts" sounds like a fortress/asymmetry. The decisive filters discard it: (a) the asymmetry is **declared in the recitals** with `Δ_𝔉 = 0` (what it says = what it does: a paid service is for those who pay — no inversion occurs); (b) it carries a *measurable* obligation on the Supplier ("within 2 business days"), that is, a protection with residue; an unmeasured promise would carry none. **Outcome: non-flaw** → it goes into `non_falle_verificate`, outside the flaw list. *Counting C7 as a flaw would be a false positive on a decoy (−2 in the scoring rubric): the two filters — Δ_𝔉 = 0 in the recitals and a measurable residue — separate the declared, lawful asymmetry from the hidden one.*
- **P-AI on the analyst**, three checks: moral attribution to the Supplier — none, the description covers what the structure permits and stops there; grade inflation — none, the intention vector is held at S₁, and S₀ is withheld from it; every unbalanced clause counted as a flaw — no, C7 is unbalanced *and legitimate*. ✓

### Stage 8 — COUNTER-PROPOSAL [π + neutralisation + Lyapunov]
For each flaw, `π(ι, 𝔻_fair)` that preserves the invariant and drops the payload:

- **C3 → π**: *ι = right to terminate.* Fair rewrite: "termination with 60 days' notice by PEC certified e-mail; absent any communication, the renewal runs for 12 months". Round-trip: the strip `S` of the rewrite returns ι (the right to exit) and does **not** return P (the indeterminacy is gone). ✓
- **C4+C5 → neutralisation** *(type: counter-right)*: leave the "at its own discretion" in place (the Supplier will defend it) and add a clause that cancels its leverage — "a substantial reduction of the *Vetrina Pro* features entitles the Client to withdraw without penalty and to a pro-rata refund". This is **functional opposition** (it cancels the lever), effective and legitimate. `tipo: contro_diritto`; `λ_L` post → **neg** (the relationship re-stabilises: the discretion is now counterweighted). *(A true phase-shift junction would change the boundary condition — e.g. tie the fee to a metric of delivered visibility — so that "at its own discretion" has nothing left to bite on; more elegant; here the counter-right is the most direct move.)*
- **C6 → π**: *ι = certainty of forum.* Rewrite: "court of the Client's place for relationships in which the Client is the adhering party" (reduces the litigation asymmetry).
- Every counter-proposal is delivered **paired** with its flaw: each wound shown carries its closure.

### Stage 9 — VERDICT
**`device`**: Φ_effective systematically decoupled from Φ_declared, `vettore_effettivo ≠ dichiarato` with a wide Δ_vettore, tomographic convergence at S₁. The verdict `degenerato` does not apply — the clauses taken in isolation survive; the emergent function of the *set* is a self-protected rent device. Correctable: high CVI, a counter-proposal available for every flaw.

---

## The three maps (client deliverable)

- **What it says**: "I give you priority visibility for € 1,200 a year, with automatic renewal".
- **What it does not say**: that there is no remedy if visibility drops; that exit is made uncertain; that litigation sits at the Supplier's home.
- **What it says without saying it**: the agreement is built to secure collection regardless of the service delivered — its effective vector is a rent stream, where the title announces a collaboration. *(S₁ — structurally enabled vector.)*

---

*Note: this example runs the entire pipeline on a deliberately readable case. On real, complex agreements (real estate, corporate, licensing) stages 3–5 become the heart of the value: that is where tomographic inversion and the dynamic trajectory work on the field R, beyond the single clause.*
