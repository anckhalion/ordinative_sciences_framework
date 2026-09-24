# LEXX — Compatibility Profile with the Ordinative Sciences

**Profile:** TE-LEXX-CONFORMANCE-0.1  
**Date:** 2026-09-16  
**Status:** binding for LEXX v0.1; validation status in `README.md` (status line) and `release.json`

**Executive revision 2026-09-17:** `03_PRE_PILOT_PROTOCOL.md` and `v0_2_alpha3/compatibility.json` govern the new alpha.3 runs. The latter binds the executive dependencies to file names and SHA-256 digests, including LENS, P-PRO, VERI, OBSERVER and Teleodynamics. The gaps listed in §7 describe the initial plan; their current status is in the table of the pre-pilot protocol. `CONFORMANT_VERIFIED` is issued per run by the external report, once technical checking, recorded semantic review and empirical effectiveness are all on record.

## 1. Placement

LEXX is the on-demand operational framework of the Technology of Expressions for agreements and normative systems.

Precedence hierarchy:

`Ordinative Sciences → OST/TE Core → TE Protocols and Symbol Canon → invoked TE frameworks → LEXX Foundations → LEXX pipeline → application to the document`.

In case of conflict the higher level prevails. The executor records the incompatibility and halts the stages involved.

## 2. Minimum mandatory stack

| Component | Canonical version | Function in LEXX | If absent or incompatible |
|---|---:|---|---|
| TE Bootloader | 7.1 | operational identity, confidence, Φ-test, router | `INCOMPATIBLE_STOP` |
| TE Protocols | 1.0 | *Controfase* (counter-phase), P-AI and operational discipline | `INCOMPATIBLE_STOP` |
| TE Core | content 5.2, historical file `v5_1` | ontology and modular architecture | halt |
| OST | 2.1 | agreement as `𝓘 = ⟨Σ,R,Φ⟩` | halt of the systemic STRIP |
| Symbol Canon | content 1.2, historical file `v1_0` | authority over notation | prose alone, or halt |
| SVP | 5.1 | provenance, formation and perimeter | halt before stage 0 |

## 3. Dependencies by stage

| LEXX stage | Dependency | Assumed version/status | Mode admitted in v0.1 |
|---|---|---|---|
| 0 — INSED | SVP | 5.1 | mandatory |
| 1 — STRIP and field `R` | OST + SA | OST 2.1; SA/PA repository release 2.0.0 | two-channel STRIP according to the canon |
| 1.5 — consistency | TE/document checks | LEXX v0.1 rules | explicit arithmetic and temporal checks |
| 2 — flaw vectors | local LEXX, subordinate to OST/SA | v0.1 | V-OM, V-AM, V-IN, V-TEMP |
| 3 — `E→I` inversion | TE + LENS + P-PRO + SA | LENS 5.1; P-PRO 5.2 | graded inference; the vector is reported as structurally enabled, at the grade LENS assigns |
| 4 — proportion | PA | repository release 2.0.0 | argued qualitative band |
| 5 — trajectory | OBSERVER/Teleodynamics | OBSERVER 1.1; content extension 1.2 | argued qualitative sign and bifurcations |
| 6 — class and residue | OCT + VERI | canonised A/B/C/D taxonomy; VERI 1.0 | argued classification |
| 7 — contrary test | Controfase + TE Protocols | Protocols 1.0 | mandatory |
| 8 — counter-proposal | SA `π` + trajectory test | SA/PA release 2.0.0 | re-strip issued; a distinct reviewer verifies it (`03_PRE_PILOT_PROTOCOL.md` §Counter-proposal and round-trip) |
| 9 — verdict | whole pipeline | preceding dependencies | inherits the weakest grade |

For OCT the assumed corpus/governance is repository release 5.3.2, with the A/B/C/D taxonomy aligned to the Symbol Canon. LEXX reports the A/B/C/D class as an argued classification; formal OCT certification requires the LEXX–OCT interface listed in §7.

## 4. Degradation rules

1. **SVP:** a run begins at stage 0 with SVP 5.1 loaded; the halt before stage 0 is in §2.
2. **Anchoring orchestrator:** a run executed by the LLM alone carries `LLM_ONLY_UNVERIFIED`; the external report of `validate_lexx_output.py` closes that state (P1, `00_FOUNDATIONS.md` §3).
3. **PA engine:** proportion is an argued qualitative band; figures require the PA engine pinned in `compatibility.json`.
4. **Phase space and temporal data:** `λ_L` is an argued sign, or empty; numerical exponents require phase-space and temporal data in the packet.
5. **External legal sources:** the verdict concerns the text; legal validity is judged in the separate assisted legal pass, with current official sources. In this profile the schema fixes `external_sources_verified` to `false` and the `sistema` verdict to `non_valutabile`, and the semantic checks reject OCT class D.
6. **Independent review:** the intention vector is a structural inference at the grade LENS assigns; the passage to the author's psychology requires verified external evidence (§6).
7. **Schema validator:** machine validation is the external report of `validate_lexx_output.py`; an output read by eye is an executor's draft.
8. **Field the data leave open:** it stays empty, with a `nota_limite`.

## 5. Run conformance states

| State | Meaning |
|---|---|
| `CONFORMANT_VERIFIED` | compatible stack, citations and schema verified externally, dependencies recorded |
| `CONFORMANT_QUALITATIVE` | compatible stack; PA/Lyapunov used qualitatively, according to v0.1 |
| `LLM_ONLY_UNVERIFIED` | pipeline executed by the LLM alone; attestation rests with the external report |
| `DOCUMENT_ONLY` | the verdict concerns the text (§4, external legal sources) |
| `INCOMPATIBLE_STOP` | version, symbol or dependency conflict; the executor halts the affected stages |
| `INVALID_OUTPUT` | JSON parse error, or a mandatory field that fails a check of the external report |

Compatible states coexist: a run is, for example, `CONFORMANT_QUALITATIVE` and `DOCUMENT_ONLY` at once. `CONFORMANT_VERIFIED` and `LLM_ONLY_UNVERIFIED` exclude each other.

## 6. Mandatory distinction on intention

LEXX can infer:

> the vector made possible, favoured or stabilised by the structure of the agreement.

It cannot demonstrate from the text alone:

> the mental state or subjective intention of the author.

The field `vettore_intenzione` keeps its historical name and is read as the **structurally enabled vector**. Any passage to the author's psychology requires verified external evidence and is graded according to LENS. Field identifiers and status strings are canonical and language-independent; they match the runtime schema.

## 7. Open gaps for v0.2

- an orchestrator for string-match, gates and round-trip;
- canonical JSON Schema and validator;
- automatic register of the loaded dependencies;
- machine-readable separation between evidence and confidence;
- gates for jurisdiction, applicable law and date of the sources;
- double verdict `testo` / `sistema` (text / system);
- formal interface with OCT;
- blind empirical cycle with sealed ground truth and decoys.
