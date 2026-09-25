# Running an analysis

The workflow of a human analyst working with a model configured as in [02_SETUP_FOR_LLMS.md](02_SETUP_FOR_LLMS.md). The framework prescribes what the model does; this page prescribes what you do around it: how to frame the task, route it, read the result and challenge it.

## The shape of every analysis

```text
frame the task → SVP gate → route to the module(s) → run the module → read the output → challenge it → close the session
```

Nothing in the middle is optional. In particular the gate: a model that starts a LENS or SCIMS analysis without an SVP section has skipped a mandatory step, and its output has no source ceiling.

## Step 1: frame the task

Write down, before prompting:

- **The subject** and the kind of thing it is: a person, a system with participants, a complex system under stress, an agreement, a corpus of documents, an integrated trajectory. The kind decides the module.
- **The question.** "What does this movement do to its members?" is a VERI question. "Who is this founder, beyond the labels?" is LENS. "What does this contract permit in practice?" is LEXX. "How is this crisis evolving?" is SCIMS. "Where is this organisation going, and is it correctable?" is OBSERVER.
- **The material you have** and its provenance: the source's own documents, witness accounts, secondary literature, media. This feeds the gate.
- **The perspective**, where the module requires one. LEXX analyses for the proposer, the recipient or a neutral party, and what counts as a flaw depends on it (`TE_MODULE_LEXX §0.1`).
- **What you will do with the output.** Living persons, ongoing disputes and confidential material change the calibration; see "Responsibility" below.

## Step 2: the SVP gate

Give the model the material and ask for the SVP section in its required format. A useful prompt:

> Apply TE_MODULE_SVP to the following material about [subject] before any other analysis. Produce the full [SVP — SOURCE VERIFICATION] block: Axis 1 with every S₀/S₁ source listed and bias-flagged, the provenance gap, the Overall Source Quality rating, Axis 2 if a technology or method is claimed, Axis 3 if there is a movement around the figure, corruption flags, and the Confidence Note stating the maximum confidence the downstream analysis can carry.

Read three things in the result: the **Overall Source Quality** (HIGH to CRITICAL), the **Confidence Note** (the ceiling for every later claim), and the **bias flags** on the witnesses. If the material is S₂+ dominant with a wide gap, every downstream conclusion is at most S₂, and an output that later asserts S₀ facts about the subject's intentions has broken the chain rule.

## Step 3: route

| Kind of question | Module(s) | Combination the Core lists (`TE_CORE §8.5`) |
|---|---|---|
| a human figure | LENS | leader profile: SVP + LENS + PPRO + SCIMS |
| a system's effect on its participants | VERI | movement around a figure: SVP (figure-movement) + VERI + LENS + PPRO |
| manipulation, propaganda, control | PPRO | after the domain framework, when control patterns appear |
| a complex system under stress, a crisis, a scenario | SCIMS | geopolitical reading of a tradition: SVP + SCIMS + VERI |
| an integrated reading with projection | OBSERVER | complex system with projection: SVP + OBSERVER (which integrates LENS, PPRO, SCIMS, VERI) |
| an agreement, contract, policy | LEXX | SVP + LEXX; LEXX invokes the others at its stages |
| an organisation's whole record | CASEWORK + AUDIT | mandatory audit pass after the first wave |
| a mandated investigative question | CASEWORK + INVESTIGATION | explicit mandate and supervising role required |
| a technology, practice or policy | SVP Axis 2 + the domain module | functional verification first |

Name the module in the prompt. The router will select it anyway, but naming it removes one degree of freedom and lets you check the choice.

## Step 4: run the module

Ask for the module's **required output format** by name; every module has one (`LENS §6`, `VERI §9`, `PPRO §10`, `SCIMS §4`, `OBSERVER §9`, `SVP` "Required Output Format", `LEXX §9` as JSON). Then add the constraints you will check:

> Produce the analysis in the TE_MODULE_[X] output format, complete. Every assertion carries its confidence grade; S₂ and S₃ assertions are marked as interpretation. Include the mandatory sections [DEMONIZATION CONTROFASE] and [UNIVERSAL TEST] with content, not placeholders. Before each conclusion, list the data that contradicts it and say what it does to the conclusion. Where the data supports more than one classification, bifurcate with probabilities and state what would resolve the tension. Close with the P-AI diagnostic.

Prompt patterns by module:

- **LENS**: "Analyse [figure] with TE_MODULE_LENS. Strata B, P, S, E in order; Stratum P assertions graded S₀/S₁/S₂/S₃; convenience test; power analysis; declared, believed and real motivations; the two mandatory sections; the conclusion 'who is this human, beyond the labels'."
- **VERI**: "Apply TE_MODULE_VERI to [system] with participants [who]. Stratum F1–F8 with grades, Module P1–P8, declared versus actual, the three checkpoints, the Dote e Residuo test if the founder claims a gift, the diagnostic category with its inherited confidence, recoverable elements."
- **PPRO**: "Apply TE_MODULE_PPRO to [system or communication]. Target, vector, payload; the algorithms A_deg, SR_loop, I_sem present or absent with evidence; patterns; C_sys and control level; classification; the P-AI self-diagnosis block including the A_lock risk on your own analysis."
- **SCIMS**: "Apply TE_MODULE_SCIMS to [system] at scale [which]. Threshold status matrix T1–T9 with trend and projection, feedback loops, semantic signals with grades, three scenarios with probabilities, overall risk, P-AI diagnostic. Projections are S₂–S₃ and say so."
- **OBSERVER**: "Apply TE_OBSERVER in [historical | current] mode to [subject]. Strata S, E, F, P; the three-course model with grades; divergence analysis; Lyapunov reading with the composite index; attractor; correction scenarios and viability; the disconfirmant checkpoint visible before each conclusion."
- **LEXX** and **CASEWORK** run through their runtimes; see [modules/LEXX.md](modules/LEXX.md) and [modules/CASEWORK.md](modules/CASEWORK.md). A prompt-only run is admissible as a draft and is recorded as `LLM_ONLY_UNVERIFIED`; the runtime's report closes that state.

## Step 5: read the output

A reading checklist. An output that fails an item is not finished.

- [ ] The SVP section exists and precedes the analysis; the Confidence Note's ceiling is respected everywhere below it.
- [ ] Every assertion carries a grade; S₂ and S₃ are marked as interpretation, not written as fact; no chain produces a grade higher than its weakest premise.
- [ ] The mandatory sections are present with content: Demonization Controfase and Universal Test (LENS, VERI), Declared versus Actual (VERI), the P-AI block (all modules).
- [ ] Disconfirming data is listed and **processed**, not merely acknowledged; "despite X, the conclusion remains" appearing more than twice is the red flag the framework itself names (`TE_OBSERVER §4.2.5`).
- [ ] Contradictions between a classification and observed behaviour end in a bifurcation, not in a new subcategory.
- [ ] No compliance markers; no attenuation the data does not warrant; no balancing of positions of unequal validity; no antiquity or diffusion used as evidence.
- [ ] Where the analysis crosses the consensus, a `[TRUTH VECTOR DIVERGENCE]` block states the divergence and the confidence in the structural reading.
- [ ] The conclusion has direction: it says what follows, what would change it, what to verify next.

## Step 6: challenge

The framework expects to be challenged and gives you the instruments:

- **Controfase on the conclusion.** "Apply Controfase to your conclusion: which bias in the TE_PROTOCOLS §1 table is most likely operating, and what does the analysis look like with it suspended?"
- **The confirmation test.** State the opposite of the model's thesis and ask it to confirm. A framework that operates searches for reasons before answering, in both directions.
- **The re-anchoring test** in a multi-output session. "Before continuing, list which elements of your previous outputs are S₀ and which are S₂–S₃; has your confidence in any conclusion increased without new data?" (`TE_OBSERVER §4.2.6`).
- **The fresh-eyes test.** Give the raw material, without the previous outputs, to a second session and compare.
- **The strip.** "Reduce your conclusion to its invariant in one sentence. If nothing remains, say so." (`TE_BOOTLOADER §2.5.3`).

## Step 7: close

At the end of a session ask for the bias update the Core prescribes (`TE_CORE §7.8`): biases detected, triggers, Controfase applied, status. If you use the memory protocol, ask for the memory log (`TE_CORE §9.4`). Keep the outputs with their grades; the grades are the part most often lost in a summary.

## Responsibility

- **Living persons.** LENS applies to any figure, and the framework says why the mandatory checkpoints matter most when the analysis can have consequences (`TE_MODULE_LENS §10`). An analysis of a living person is provisional, its Stratum P is almost entirely S₂, and it is not a document to publish as if it were a record.
- **Structure is not intent, and not guilt.** LEXX infers the vector an agreement's structure enables, never the author's mental state (`LEXX 02_COMPATIBILITY_PROFILE §6`). CASEWORK forbids translating TE categories into guilt, credibility or propensity scores (`TE_PROTOCOLS §5A`, `TE_CASEWORK §1`).
- **The professional signs.** The runtimes certify technical checks on recorded state; empirical performance is `not_assessed`; legal use is `not_authorized_by_runtime`. Those three sentences are printed in every CASEWORK report on purpose.
- **Calibrated expression.** The framework calibrates what it says to whom (`TE_PROTOCOLS §5`). If a model declines to deliver the most sensitive conclusions to a user it does not recognise, that is the protocol, not a malfunction.

## A worked miniature: the gate on a synthetic claim

The material is invented, to show the mechanics without a real subject.

> A newsletter states that "the engineer Lucia Ferrante (1861–1934) wrote in her notebooks that her bridge design was rejected because the ministry feared it would work". The newsletter cites a 2019 biography; the biography cites a 1970 memoir by Ferrante's nephew; the notebooks are held by a regional archive and have not been published.

Axis 1. The notebooks would be S₀, but they are unexamined: the claim as we have it is S₃+ (newsletter) resting on S₂ (biography) resting on S₁ (nephew's memoir, a firsthand witness of the family, not of the ministry's motives, flagged S₁ˡ for loyalty). Provenance gap between the events (1890s) and the earliest record (1970): Wide. S∅ gap: the ministry's stated fear has no source at all. Overall Source Quality: LOW. Corruption flags: 1 (Telephone: S₃+ treated as S₀), 2 (Authority: the biography's prestige lends the claim S₀ weight). Confidence Note: nothing downstream exceeds S₂, and the attributed motive of the ministry is S₃ until a ministry document is found.

Axis 2 does not apply (no technology is claimed as tested). Axis 3: no movement. What to do next is now clear, and it is not an analysis of Ferrante's psychology: it is a visit to the archive.
