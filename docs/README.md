# Documentation map

This repository holds the **Technology of Expressions (TE) / Ordinative Sciences**
in four layers, each for a different reader. Start from the row that matches you.

| If you are… | Go to | What it is |
| --- | --- | --- |
| an **AI agent or analyst** configuring/operating the framework | [`framework/`](framework/) | The operative source of truth: ontology, router, modules. |
| a **reader** who wants the argument, front to back | [`book/`](book/) | *La porta. Una grammatica della coerenza* — long-form essay, bilingual. |
| someone who needs to **look up** an axiom, definition, or module | [`manual/`](manual/) | Reference manual — schematic, citable. Condensation of the book. |
| a **researcher** citing the work | [`papers/`](papers/) + `../CITATION.cff` | Abstracts and academic artifacts. |

## `framework/` — the operative framework (source of truth)

Everything else in this repo derives from here. If book and manual ever
disagree with these documents on a point of doctrine, **these prevail**.

- **`framework/core/`**
  - [`TE_CORE.md`](framework/core/TE_CORE.md) — ontology, foundational axioms, Arajat logograms, the `Controfase` mechanism.
  - [`TE_BOOTLOADER.md`](framework/core/TE_BOOTLOADER.md) — operative instructions, router, `P-AI` self-diagnostic.
- **`framework/ost/`** — Ordinative Set Theory
  - [`OST_Concise_Guide.md`](framework/ost/OST_Concise_Guide.md) — mathematical & semantic foundation.
  - [`OST_Teleodynamics_Causal_Inversion.md`](framework/ost/OST_Teleodynamics_Causal_Inversion.md) — advanced causal inversion.
- **`framework/modules/`** — dynamically loaded analytical lenses
  - `TE_MODULE_SVP` — Source Verification Protocol (**mandatory gate**, always first)
  - `TE_MODULE_LENS` — Integral Human Figure Analysis
  - `TE_MODULE_VERI` — Functional Impact Verification
  - `TE_MODULE_PPRO` — Psycho-Political Pattern Recognition
  - `TE_MODULE_SCIMS` — Smart Correlation Intelligence Monitoring
  - `TE_OBSERVER` — Integrated Observation & Lyapunov Trajectories

> Module identifiers (`TE_MODULE_SVP`, …) are the framework's vocabulary used by
> the router. Filenames match the identifier; document versions live in
> [`../CHANGELOG.md`](../CHANGELOG.md), not in the filename.

## `book/` — the essay

*La porta. Una grammatica della coerenza* (EN: *The Door. A Grammar of Coherence*).
Continuous prose, written to be read. Bilingual: `it/` is the authorial source,
`en/` a parallel (rewritten, not calqued) edition. See [`book/README.md`](book/README.md).

## `manual/` — the reference

A condensation of the book into a schematic, citable reference. Grows
incrementally; see [`manual/README.md`](manual/README.md) for the target layout
and editorial conventions.

## `papers/` — academic artifacts

Abstracts and submission-ready material. To cite the framework, use the
`CITATION.cff` at the repository root.

---

For how the three public repositories of the ecosystem fit together
(Theory · Practice · Validation), see [`../ECOSYSTEM.md`](../ECOSYSTEM.md).
