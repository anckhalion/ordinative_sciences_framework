# TE_SYMBOL_CANON — the notation register

**Canonical file:** `FRAMEWORKS/TE_SYMBOL_CANON_v1_0_EN.md` · register status 1.2 (the file name keeps `v1_0`) · load order 5 · mandatory before writing, editing or translating any formal notation; optional when concepts are used verbally · prerequisites: Core.

## In one paragraph

The Canon is the cross-volume authority for every formal symbol of the Ordinative Sciences programme: OST, the TE volumes, the algebras (PA, SA), OCT, the papers, the Controfase treatise, the framework modules. It fixes three tiers of precedence (OST owns the master primitives; the TE volume's deviations are declared exceptions; the Tier-2 algebras rename before the foundations do), six resolution principles, a locked register of assignments (primitives and spaces, dynamics and measures, operators, the Lyapunov-volume batch, label namespaces), a mandatory reservation procedure for new symbols, and a record of deferred batches. This file is the master copy; derived copies in other repositories are updated from it, never the reverse.

## When it applies

`§0` is explicit: load it before touching any formal notation in any programme document, and load it first if a session turns to notation. A model that writes an equation, an operator, a classification label or a glyph without it is writing outside the register.

## What a human needs from it

- **The same letter is a different object in a different volume**, and the Canon says which. Φ is the emergent function (OST) and, by declared exception, the collapse function E = Φ(C, I, K) in the TE volume; S is the Strip operator, S₀–S₃ are confidence grades, S₀–S∅ are source levels (a label namespace, `§2` "Label namespaces"); 𝒜 is the Author, exclusively, so the Direction Problem's attractor became 𝔸; bare τ is the pulsational function and every threshold is subscripted.
- **The register is locked.** Adding or changing a row is a ratified act with a version bump (`§3` step 4). Chapter-local scoping is legitimate only if declared in the volume's own notational apparatus.
- **The reservation procedure** (`§3`): check the register and the historical record; prefer a free glyph family, then a subscripted form of a related symbol, then declared coexistence; propose with glyph, meaning, type, volume and collision check; on ratification add the row, bump the version, note it in `§6`, propagate. The section lists the glyphs known free at the last verification.
- **Deferred batches** (`§4`) tell you what is knowingly not yet aligned: the OST second edition batch, the remaining TE framework patches, the papers' four deviants (aligned at their revision), the Science & Sanity citations.

## Reading notation in an output: checklist

- [ ] 𝓘 = ⟨Σ, R, Φ⟩ for the ordinative set; ι-family for invariants; 𝓚 for the coherence vector; blackboard letters for spaces (𝕀, 𝕄, 𝔻, 𝔽, 𝕊, 𝔸, 𝕋).
- [ ] Any overloaded symbol carries its operand or subscript disambiguation (P2, P3) and, where the text is a TE-volume context, the declared exception is stated.
- [ ] A new symbol is not introduced "locally, to fix later" (`§3` step 5).

## Pitfalls

- Using SA's old letters (C for Controfase, K for knowledge, D for domain) that the register renamed (C_φ, 𝒦_p/𝒦_r, 𝔻).
- Taking the file name as the version: the register is 1.2 (the Lyapunov-volume batch of 2026-08-19); the lock records 1.2.
- Reading the Direction Problem v1.0 glyphs (𝒜, 𝒯, bare σ) as canonical: the Canon records them as unregistered deviants resolved by 𝔸, 𝕋, σ_𝔸, and the v1.1 preprint in `papers/` applies the alignment.

## Section map

[0] load trigger · [1] tier precedence and principles P1–P6 · [2] the canonical register: master primitives and spaces; dynamics, measures, time; operators; Lyapunov-volume and DP-alignment batch; label namespaces · [3] reservation procedure · [4] deferred batches · [5] relationship to other modules · [6] version notes (1.2, 1.1, 1.0, execution log).
