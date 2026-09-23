# LEXX — Compatibility Profile with the Ordinative Sciences

**Profile:** TE-LEXX-CONFORMANCE-0.1  
**Date:** 2026-09-16  
**Status:** binding for LEXX v0.1; experimental framework, empirical validation pending

**Executive revision 2026-09-17:** `03_PRE_PILOT_PROTOCOL.md` and `v0_2_alpha3/compatibility.json` govern the new alpha.3 runs. The latter binds the executive dependencies to actual files and SHA-256 digests, including LENS, P-PRO, VERI, OBSERVER and Teleodynamics. The gaps listed in §7 describe the initial plan; their current status is in the table of the pre-pilot protocol. The current profile issues no global `CONFORMANT_VERIFIED` attestation: the external report distinguishes technical checking, recorded semantic review and empirical effectiveness, the last of which is still to be demonstrated.

## 1. Placement

LEXX is the on-demand operational framework of the Technology of Expressions for agreements and normative systems. It has no autonomous theoretical mode.

Precedence hierarchy:

`Ordinative Sciences → OST/TE Core → TE Protocols and Symbol Canon → invoked TE frameworks → LEXX Foundations → LEXX pipeline → application to the document`.

In case of conflict the higher level prevails. The executor records the incompatibility and halts the stages involved.

## 2. Minimum mandatory stack

| Component | Canonical version | Function in LEXX | If absent or incompatible |
|---|---:|---|---|
| TE Bootloader | 7.1 | operational identity, confidence, Φ-test, router | non-conformant run; halt |
| TE Protocols | 1.0 | *Controfase* (counter-phase), P-AI and operational discipline | non-conformant run; halt |
| TE Core | content 5.2, historical file `v5_1` | ontology and modular architecture | halt |
| OST | 2.1 | agreement as `𝓘 = ⟨Σ,R,Φ⟩` | halt of the systemic STRIP |
| Symbol Canon | content 1.2, historical file `v1_0` | authority over notation | prose only, without symbols, or halt |
| SVP | 5.1 | provenance, formation and perimeter | LEXX does not start |

## 3. Dependencies by stage

| LEXX stage | Dependency | Assumed version/status | Mode admitted in v0.1 |
|---|---|---|---|
| 0 — INSED | SVP | 5.1 | mandatory |
| 1 — STRIP and field `R` | OST + SA | OST 2.1; SA/PA repository release 2.0.0 | two-channel STRIP according to the canon |
| 1.5 — consistency | TE/document checks | LEXX v0.1 rules | explicit arithmetic and temporal checks |
| 2 — flaw vectors | local LEXX, subordinate to OST/SA | v0.1 | V-OM, V-AM, V-IN, V-TEMP |
| 3 — `E→I` inversion | TE + LENS + P-PRO + SA | LENS 5.1; P-PRO 5.2 | graded inference; subjective intention never stated as fact |
| 4 — proportion | PA | repository release 2.0.0 | qualitative band only, until the engine is attached |
| 5 — trajectory | OBSERVER/Teleodynamics | OBSERVER 1.1; content extension 1.2 | qualitative sign and bifurcations only |
| 6 — class and residue | OCT + VERI | canonised A/B/C/D taxonomy; VERI 1.0 | argued classification; absolute measurement excluded |
| 7 — contrary test | Controfase + TE Protocols | Protocols 1.0 | mandatory |
| 8 — counter-proposal | SA `π` + trajectory test | SA/PA release 2.0.0 | re-strip issued; external verification still required |
| 9 — verdict | whole pipeline | preceding dependencies | inherits the weakest grade |

For OCT the assumed corpus/governance is repository release 5.3.2, with the A/B/C/D taxonomy aligned to the Symbol Canon. Until a tighter LEXX–OCT interface exists, LEXX does not present the class as a formal certification of the OCT system.

## 4. Degradation rules

1. **Without SVP:** no LEXX run.
2. **Without the anchoring orchestrator:** the result is `LLM_ONLY_UNVERIFIED`; P1 is unmet.
3. **Without the PA engine:** only reasoned qualitative bands are admitted; proportion figures are forbidden.
4. **Without phase space and temporal data:** `λ_L` remains an argued sign, or empty; numerical exponents are forbidden.
5. **Without verified external legal sources:** the verdict concerns the text; overall legal validity is out of scope.
6. **Without independent review:** the intention vector remains a structural inference; it cannot become a psychological imputation.
7. **Without the schema validator:** the output can be read; it cannot be declared machine-validated.
8. **Field unsupported by the data:** it stays empty, with a `nota_limite`; no plausible filling.

## 5. Run conformance states

| State | Meaning |
|---|---|
| `CONFORMANT_VERIFIED` | compatible stack, citations and schema verified externally, dependencies declared |
| `CONFORMANT_QUALITATIVE` | compatible stack; PA/Lyapunov used only qualitatively, according to v0.1 |
| `LLM_ONLY_UNVERIFIED` | pipeline executed without the P1 orchestrator; no automatic attestation |
| `DOCUMENT_ONLY` | external sources unverified; conclusions limited to the text |
| `INCOMPATIBLE_STOP` | version, symbol or dependency conflict; affected stages not executed |
| `INVALID_OUTPUT` | malformed JSON or inconsistent mandatory fields |

States may coexist only when they are not logically incompatible. For example, a run may be `CONFORMANT_QUALITATIVE` and `DOCUMENT_ONLY`; it cannot be `CONFORMANT_VERIFIED` and `LLM_ONLY_UNVERIFIED` at the same time.

## 6. Mandatory distinction on intention

LEXX can infer:

> the vector made possible, favoured or stabilised by the structure of the agreement.

It cannot demonstrate from the text alone:

> the mental state or subjective intention of the author.

The field `vettore_intenzione` keeps its historical name and is read as the **structurally enabled vector**. Any passage to the author's psychology requires verified external evidence and stays graded according to LENS. Field identifiers are canonical and language-independent; they match the runtime schema.

## 7. Open gaps for v0.2

- a real orchestrator for string-match, gates and round-trip;
- canonical JSON Schema and validator;
- automatic register of the loaded dependencies;
- machine-readable separation between evidence and confidence;
- gates for jurisdiction, applicable law and date of the sources;
- double verdict `testo` / `sistema` (text / system);
- formal interface with OCT;
- blind empirical cycle with sealed ground truth and decoys.
