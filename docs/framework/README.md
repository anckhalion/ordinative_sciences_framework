# Framework — operative TE / Ordinative Sciences

This folder is the **source of truth** of the Technology of Expressions.
If you are configuring an AI agent (system prompt, custom GPT, RAG corpus)
or running an analysis by hand, you operate from here. The book and the
manual are derivatives.

## Quickstart — load the framework in an AI conversation

The framework is designed to bootstrap an AI agent into a TE-compliant
operative state. Minimal viable load:

1. **[`core/TE_CORE.md`](core/TE_CORE.md)** — ontology, foundational axioms,
   Arajat logograms, the *Controfase* mechanism. Load first; everything else
   presupposes it.
2. **[`core/TE_BOOTLOADER.md`](core/TE_BOOTLOADER.md)** — operative
   instructions, router logic, and the `P-AI` continuous self-diagnostic.
   Tells the agent *how* to use `TE_CORE` in interaction.
3. **[`modules/TE_MODULE_SVP.md`](modules/TE_MODULE_SVP.md)** — the
   **mandatory gate**: SVP must pass before any other analytical module
   fires. The router refuses to run downstream modules without it.

The remaining modules load **on demand**, triggered by the router based on
what the user asks. Do not preload everything — that defeats the design.

## Module router — when each module fires

| Trigger (in the user's request) | Module | What it does |
| --- | --- | --- |
| **Any analysis at all** | [`TE_MODULE_SVP`](modules/TE_MODULE_SVP.md) | Source & provenance verification — **prerequisite for every other module** |
| Geopolitics, crisis, systemic scenario | [`TE_MODULE_SCIMS`](modules/TE_MODULE_SCIMS.md) | Smart Correlation Intelligence Monitoring — complex systems |
| Participant impact, expressive-system effects | [`TE_MODULE_VERI`](modules/TE_MODULE_VERI.md) | Functional impact verification (replaces VERT v5.0) |
| Public, historical, or mythological figures | [`TE_MODULE_LENS`](modules/TE_MODULE_LENS.md) | Integral human figure analysis |
| Manipulation, propaganda, control | [`TE_MODULE_PPRO`](modules/TE_MODULE_PPRO.md) | Psycho-political pattern recognition |
| Observation across time, trajectories | [`TE_OBSERVER`](modules/TE_OBSERVER.md) | Integrated observation, Lyapunov trajectories |

Full router logic — handoff sequences, conflict resolution, the P-AI loop —
is in [`core/TE_BOOTLOADER.md`](core/TE_BOOTLOADER.md).

## OST — the formal layer

The two OST documents formalize the mathematics and semantics underlying TE:

- **[`ost/OST_Concise_Guide.md`](ost/OST_Concise_Guide.md)** — the triad
  ⟨Σ, R, Φ⟩, properties of ordinative sets, the semantic foundation TE
  rests on.
- **[`ost/OST_Teleodynamics_Causal_Inversion.md`](ost/OST_Teleodynamics_Causal_Inversion.md)**
  — advanced extension on teleodynamics and causal inversion. Not required
  for routine analysis; load when the request involves temporal reversal or
  teleological constructs.

## Versioning

Document versions live in [`../../CHANGELOG.md`](../../CHANGELOG.md), not in
filenames. This keeps citation links and external system-prompt references
stable across releases. Each operative document also carries its own
version in its front matter.

## Reading vs. operating

This folder is for **operating** TE. If you are encountering the framework
for the first time and want the argument front-to-back, go to
[`../book/`](../book/) — the long-form essay *La porta. Una grammatica della
coerenza*. For schematic lookup of a single axiom or definition, use
[`../manual/`](../manual/).
