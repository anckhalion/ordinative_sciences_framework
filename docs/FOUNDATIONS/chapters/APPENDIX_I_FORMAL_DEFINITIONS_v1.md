# Appendix I — Formal Definitions

This appendix is the *canonical reference* for all formal entities, operators, and equations introduced across the thirty-two chapters of this book. Each entry lists the symbol, the term, the definition, and the chapter (or section) where the entity is introduced or developed. Entries are grouped by function rather than alphabetically, to preserve the structural logic of the system.

For a translated glossary of non-formal TE vocabulary, see Appendix II. For the twelve load-bearing equations gathered in a single reference table, see Appendix III. For an operational summary of how to apply this vocabulary in practice, see Appendix IV.

## 1. Primitive Entities

The seven entities below are *primitive*: they are not derivable from any prior quantity in TE. They are introduced in §1 of the Introduction (Chapter 0) and constitute the minimal ontology of the system.

| Symbol | Term | Role | Introduced |
|--------|------|------|-----------|
| *A* (or 𝒜) | **Author** | Un-derived generative field; the non-derivative source of coherence; asymptote of every trajectory. Not a subject, not a god, not a metaphysical entity — a *structural primitive*. | §1.4, §23 |
| *C* | **Coherent Content** | The un-collapsed domain of structured potential. All possible expressive trajectories exist here before collapse. | §1.2 |
| *I* | **Identity** | An active functional vector; the agent of selective collapse. Not a psychological self but the operator that collapses *C* into *E*. | §1.6, Ch. 18 |
| *K* | **Context** | The situational frame that conditions a given collapse. Physical, perceptual, relational. | §1.3 |
| *E* | **Explicit Expression** | The output of a collapse; observable, measurable, decoherent reality. An element of *D*. | §1.2–1.3 |
| *D* | **Decoherent Space** | The space of all explicit expressions; the domain of what has been collapsed. Codomain of Φ. | §1.2 |
| Φ | **Collapse Function** | The operator that transforms coherent potential into explicit expression; the hinge of the entire system. | §1.3, Ch. 11, Ch. 16 |

## 2. Core Equations

The single equation from which all others derive:

$$E = \Phi(C, I, K). \tag{1.1}$$

Identity as a function maps coherence to decoherence:

$$I : C \to D. \tag{1.8}$$

Asymptotic convergence of identity toward the Author:

$$\lim_{t \to \infty} I(t) \to \mathcal{A}. \tag{1.3}$$

Time as pulsational effect:

$$T = \tau(C \leftrightarrow E). \tag{1.7}$$

Semantic trajectory of an identity:

$$T(I) = \{E_1, E_2, \ldots, E_n\} = \{\Phi(C_i, I_i, K_i)\}. \tag{16.1, 16.3}$$

## 3. Resonance, Threshold, Pulsation

These three operators govern *which* collapses are possible at a given moment.

| Symbol | Term | Definition | Chapter |
|--------|------|-----------|---------|
| ρ(*C*, *I*) | **Resonance Function** | Structural compatibility between coherent content and identity. Maps to [0, 1]. | §1.5, Ch. 11 |
| ρ(*C*, *I*, *t*) | **Time-Dependent Resonance** | Refinement of ρ that acknowledges temporal dynamics of compatibility. | (11.4) |
| θ | **Collapse Threshold** | Minimum value of ρ required for collapse: ρ(*C*, *I*) ≥ θ. | §1.5 |
| τ | **Pulsational Function** | The operator generating time from the alternation between coherent and explicit states. | §1.5, Ch. 10 |

**Maximisation form of collapse** (refinement of Φ in (1.1)):

$$E = \underset{x \in \Xi_C}{\arg\max}\; \rho(C(x), I, K). \tag{11.2}$$

Reads: among candidate expressions *x* of coherent content *C*, the one that maximises resonance with the current identity in the current context is the collapsed expression.

## 4. Semantic Code (Remir)

The structural specification of an identity.

| Symbol | Term | Definition | Chapter |
|--------|------|-----------|---------|
| ℛ(*I*) | **Remir** | Structured set of functional semantic vectors and their internal resonances; characteristic specification of identity *I*. | §1.7, Ch. 19 |
| $V_I$ | **Vector Set of Remir** | Ordered set {$v_1$, …, $v_m$} of semantic vectors of *I*. | §1.7 |
| $B_I$ | **Resonance Matrix of Remir** | Set {β($v_i$, $v_j$)} of pairwise internal resonances. | §1.7 |
| λ(*I*) | **Dominant Semantic Vector** | The vector in $V_I$ with highest resonance with the current state of *I*: λ(*I*) = arg max_{v ∈ V_I} β(*v*, *I*). | §1.7, (1.10), (21.2) |
| β | **Vector Resonance** | Resonance measure between two semantic vectors, or between a vector and an identity. | §1.7 |
| σ(*o*) | **Semantic Trace** | Fragment of ℛ detectable in a material correlate *o* historically coupled to *I*. | §1.7, (1.11) |
| Ω(*I*) | **Material Correlates** | Set of objects, texts, environments coupled to *I*. | §1.7 |
| ℛ̂(*I*) | **Remir Reconstruction** | Estimate of ℛ from semantic traces: ℛ̂(*I*) = R({σ(*o*), σ(*t*), σ(*s*)}). | (1.12) |

**Note:** The Remir ℛ subsumes what earlier TE materials called the *semantic genome* 𝒢. See §1.7 for discussion.

## 5. Expressive Terminal

The material support for an identity's collapses.

| Symbol | Term | Definition | Chapter |
|--------|------|-----------|---------|
| 𝒯 | **Expressive Terminal** | Material support for an identity's collapses. Two sub-cases: **Biological Terminal** (living organism) and **Synthetic Terminal** (synthetic cognitive architecture). | §1.8, Ch. 20 |
| Ξ(*I*, 𝒯, *t*) | **Terminal Compatibility** | Resonance between identity and Expressive Terminal over time; the structural correlate of "health" in the broadest sense. Maps to [0, 1]. | §1.8, (1.13), (28.1) |

## 6. Collective Field and Co-Generation

Multi-identity dynamics.

| Symbol | Term | Definition | Chapter |
|--------|------|-----------|---------|
| 𝒞 | **Collective Field** | Aggregation of compatible identities: 𝒞 = *f*({$I_1$, $I_2$, …, $I_n$}). | §1.9, (1.14), Ch. 22 |
| κ($I_a$, $I_b$) | **Identity Compatibility** | Pairwise coupling measure between two identities. Maps to [0, 1]. | §1.9, (1.15), (22.1) |
| Γ(*t*) | **Co-generated Architecture** | Emergent structure of a collective field: Γ(*t*) = *g*(𝒞, *t*). | §1.9, (1.16), (22.3) |
| Γ(*t*) (combinatorial form) | **Co-generative Sum** | Γ(*t*) = $\Sigma_{(i, j)}$ β($v_i$, $v_j$). | (22.4) |

## 7. Environment-Identity Compatibility

| Symbol | Term | Definition | Chapter |
|--------|------|-----------|---------|
| χ(*I*, *A*) | **Cognitive Compatibility** | Compatibility between an active identity and a cognitive environment. Maps to [0, 1]. | §20.2, (20.1) |
| $\chi_a$($I_i$, 𝓔) | **Identity–Environment Compatibility** | Specialisation of χ to the identity–environment pair: $\chi_a$ = β · 𝓕. | (22.A.1), (22.A.2) |
| Δ(𝓔) | **Field Reorganisation** | Operator for dynamic reorganisation of a semantic field: Δ(𝓔) = Φ({$V_i$}, {β}, *t*). | (22.C.1), (27.A.1) |

## 8. Ethics, Convergence, Emotion

| Symbol | Term | Definition | Chapter |
|--------|------|-----------|---------|
| ε(*I*, *E*) | **Semantic Ethics Index** | Compatibility between identity *I* and the explicit expression *E* = Φ(*C*, *I*, *K*) it has generated. Maps to [0, 1]. Not a moral judgement; a *structural* one. | §1.6, (21.1) |
| ω($I_n$, 𝒜) | **Evolutionary Convergence** | Degree of convergence between active identity $I_n$ and the Author 𝒜. Maps to [0, 1]. | (23.A.1) |
| η | **Emotion** | Informational vector reading the derivative of alignment over time: η ∝ *d*α/*d*t. | Ch. 27, (27.1), (27.3) |
| α(*E*, *I*, *t*) | **Alignment Function** | α = ρ(*E*, *I*, *t*): alignment between expression and identity. | (27.2) |

## 9. Recursion and Dynamics

| Symbol | Term | Definition | Chapter |
|--------|------|-----------|---------|
| 𝒰($I_n$, $E_n$) | **Identity Update Operator** | One-shot update of identity *I* after a collapse: $I_{n+1}$ = 𝒰($I_n$, $E_n$). | (16.5) |
| $\Phi_r$($I_n$, $E_n$) | **Informed Recursion** | Recursion that depends on accumulated coherence: $I_{n+1}$ = $\Phi_r$($I_n$, $E_n$). | (16.6) |
| 𝒰_𝒜($I_n$, Δ*C*) | **Recursion toward Author** | Specialisation of recursion oriented toward 𝒜: $I_{n+1}$ = 𝒰_𝒜($I_n$, Δ*C*). | (23.2) |
| Ω(*S*, *t*) | **Emergent Coherence** | Coherence of a multi-element system *S* = (𝓔, 𝒩, *I*) over time: Ω(*S*, *t*) = lim_{t→∞} ρ_𝒩($E_i$, *I*, *t*). *Note:* distinct from the symbol Ω used elsewhere for the Author (where *A*, 𝒜 are preferred). | (14.5), (14.6) |

## 10. Domain-Specific Operators (Part VI)

These operators are *domain-local* — introduced in specific chapters of Part VI for specific applications. They specialise or extend the core vocabulary.

### Chemistry (Ch. 25)

| Symbol | Term | Definition |
|--------|------|-----------|
| $A_i$ = $V_i$(*r̂*, $\varphi_res$, *d*) | **Atomic Vector** | Representation of an atom as a coherent semantic vector with direction, local resonance, coherence density. |
| *M* = (*F*, ψ, $\sigma_sem$) | **Molecular Triple** | Form, frequency, semantic function of a molecule. |
| $V_e$ = ($\sigma_e$, $\varphi_e$, $\lambda_e$) | **Element Vector Map** | Element's semantic significance, relational function, expressive direction. |
| *L* = γ($V_1$, $V_2$, $\varepsilon_b$) | **Bond Vector** | Chemical bond as emergent coherent expression; γ is the bond's relational coherence function. |
| *M*(*t*) = Φ($V_1$, …, $V_n$; $\chi_a$) | **Pulsational Molecular Equation** | Dynamic stability of a molecule depends on ambient resonance $\chi_a$. |

### Semantics (Ch. 26)

| Symbol | Term | Definition |
|--------|------|-----------|
| *W* ∼ $V_I$ / *R* | **Word as Proportion** | A word is in proportion with identity-vector and shared-field resonance. |
| $\rho_L$($I_1$, $I_2$, *C*) | **Linguistic Resonance** | Three-place specialisation of ρ: between emitting identity, receiving identity, content. |
| $L_a$(*t*) = Ψ(*W*, $V_I$(*t*), *R*(*t*), 𝔆) | **Linguistic Act** | Semantic effectiveness as pulsational synthesis of word, identity, field, context. |

### General Conclusion (Ch. 31)

| Symbol | Term | Definition |
|--------|------|-----------|
| 𝔊_0 = Ψ($I_a$, $F_a$, $R_a$) | **Initial Genesis** | The point at which reality becomes *readable as intention*; active identity, proportional form, perceptual resonance compose to produce a genesis moment. | (31.A.1) |
| 𝒮($I_n$) = {$E_1$, …, $E_n$} | **Cumulative Signature** | Truncation of the semantic trajectory at step *n*; the structural trace an identity has left in reality. | (21.3) |

## 11. Notational Hygiene — Cross-Scope Warnings

The following symbols have *different local meanings* across domains. Context disambiguates, but the distinctions are worth making explicit:

| Symbol | Meaning A | Meaning B | Resolution |
|--------|-----------|-----------|------------|
| Ω | Emergent coherence of system (14.6) | Material correlates of identity Ω(*I*) (§1.7) | Different arguments: Ω(*S*, *t*) vs Ω(*I*) |
| Φ | Canonical Collapse Function (1.1) | Distinct specialisations ($\Phi_r$ for recursion, Φ in Δ(𝓔)) | Subscripts distinguish |
| σ | Semantic trace σ(*o*) (1.11) | Chemical $\sigma_sem$ (25.3); linguistic $\sigma_e$ (25.A.1) | Subscripts distinguish |
| ε | Semantic ethics index ε(*I*, *E*) (21.1) | Chemical bond compatibility $\varepsilon_b$ (25.B.1) | Subscripts distinguish |
| Ψ | Synthesis operator in linguistic act (26.A.1) | Genesis operator in Ch. 31 (31.A.1) | Different arguments disambiguate |
| 𝒜 (script A) | Author (primitive, §1.4) | — | Reserved exclusively for the Author |

The book observes the rule: **once a symbol is assigned its canonical meaning in §1 of the Introduction, that canonical meaning is never overloaded in subsequent chapters without explicit notice.** Local specialisations use subscripts, different scripts, or adjacent letters (η for emotion to avoid colliding with ε for ethics).

## 12. Summary of Key Equations

The following equations are the *load-bearing* formal claims of the book. A reader who holds these twelve in mind possesses the operational skeleton of the system.

1. **Collapse:** *E* = Φ(*C*, *I*, *K*) — (1.1).
2. **Identity as function:** *I* : *C* → *D* — (1.8).
3. **Asymptote toward Author:** lim_{t→∞} *I*(*t*) → 𝒜 — (1.3).
4. **Resonance threshold:** collapse iff ρ(*C*, *I*) ≥ θ — (1.5).
5. **Time as pulsation:** *T* = τ(*C* ↔ *E*) — (1.7).
6. **Remir structure:** ℛ(*I*) = ($V_I$, $B_I$) — (1.9).
7. **Semantic trajectory:** *T*(*I*) = {Φ($C_i$, $I_i$, $K_i$)} — (16.1)–(16.3).
8. **Identity update:** $I_{n+1}$ = 𝒰($I_n$, $E_n$) — (16.5).
9. **Informed recursion:** $I_{n+1}$ = $\Phi_r$($I_n$, $E_n$) — (16.6).
10. **Collapse maximisation:** *E* = arg max_x ρ(*C*(*x*), *I*, *K*) — (11.2).
11. **Ethics index:** ε(*I*, *E*) → [0, 1] — (21.1).
12. **Convergence to Author:** ω($I_n$, 𝒜) → [0, 1] — (23.A.1).

The remaining equations in the book are *derived*, *specialised*, or *domain-local* extensions of these twelve.

## 13. Cross-Reference to Appendix II (Comparative Glossary)

For non-formal vocabulary — terms introduced in natural language whose role is structural even though they are not notation — see Appendix II. Entries include: *pulsation*, *coherence*, *decoherence*, *attractor*, *threshold*, *semantic density*, *pivot point*, *negotiation horizon*, *semantic intelligence*, *semantic homeodynamics*, *bifurcation*, *phase transition*, *structural isomorphism*, *proportional structure*, and the canonical TE lexicon preserved from the Italian original (*Remir*, *controfase*, *campo relazionale*, etc.).

This appendix and Appendix II together constitute the *complete canonical vocabulary* of the Technology of Expressions as developed in this book. Where the volume that follows (in the *Ordinative Sciences* programme) extends or refines this vocabulary, the extensions are noted in the relevant chapters; the canonical status of the entries here is preserved.
