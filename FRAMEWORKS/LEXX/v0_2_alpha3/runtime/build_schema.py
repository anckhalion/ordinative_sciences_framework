"""Reproducible JSON Schema 2020-12 for the pre-pilot runtime."""
import json
from pathlib import Path


VERSION = "LEXX v0.2-alpha.3"
TEXT = {"type": "string", "minLength": 1, "pattern": r"\S"}
STRING = {"type": "string"}
HASH = {"type": "string", "pattern": "^[0-9a-f]{64}$"}
CONF = {"enum": ["S0", "S1", "S2", "S3"]}


def obj(fields, optional=()):
    return {"type": "object", "additionalProperties": False,
            "required": [key for key in fields if key not in optional], "properties": fields}


def arr(items, minimum=0, unique=False):
    result = {"type": "array", "items": items, "minItems": minimum}
    if unique:
        result["uniqueItems"] = True
    return result


def enum(*values):
    return {"enum": list(values)}


def ref(name):
    return {"$ref": f"#/$defs/{name}"}


def contract():
    defs = {}
    defs["evidence"] = {"oneOf": [
        obj({"anchor_type": {"const": "literal_quote"}, "quote": TEXT,
             "evidence_level": enum("E0", "E1", "E2", "E3")}),
        obj({"anchor_type": {"const": "structural_absence"}, "context_before": TEXT,
             "context_after": TEXT, "missing_slot": TEXT,
             "evidence_level": enum("E1", "E2", "E3")})]}
    defs["dependency"] = obj({"component": TEXT, "version": TEXT,
                              "status": {"const": "available_verified"},
                              "source_file": TEXT, "sha256": HASH})
    defs["trajectory"] = obj({"mode": {"const": "qualitative"},
                              "lambda_segno": enum("neg", "pos", "vuoto"),
                              "argomento": TEXT})
    defs["counterproposal"] = {"oneOf": [
        obj({"status": {"const": "proposed"},
             "tipo": enum("riscrittura_pi", "neutralizzazione_giunzione", "contro_diritto"),
             "forma_equa": TEXT, "iota_originale": TEXT,
             "ri_strip": obj({"iota_primo": TEXT, "payload_primo": arr(TEXT),
                              "argomento_preservazione": TEXT}),
             "lambda_post": enum("neg", "pos", "vuoto"), "argomento_lambda_post": TEXT}),
        obj({"status": {"const": "not_proposed"}, "nota_limite": TEXT})]}
    defs["flaw"] = obj({
        "id": {"type": "string", "pattern": "^FX-[1-9][0-9]*$"},
        "clausole": arr(TEXT, 1, True), "vettore_primario": enum("V-OM", "V-AM", "V-IN", "V-TEMP"),
        "evidence": arr(ref("evidence"), 1), "mechanism": TEXT, "impact": TEXT,
        "confidence": CONF, "scenario_6_fasi": arr(TEXT, 6),
        "test_contrario": obj({"esito": enum("confermata", "declassata", "scartata"),
                                "interpretazione_alternativa": TEXT, "motivazione": TEXT}),
        "classe_oct": enum("A", "B", "C", "D", "non_valutabile"),
        "motivazione_classe": TEXT, "dote_residuo": enum(0, 1, 2, 3, None),
        "motivazione_residuo": TEXT, "lyapunov": ref("trajectory"),
        "cvi_banda": enum("alta", "media", "bassa", "vuoto"), "criterio_cvi": TEXT,
        "mitigazione_esterna": TEXT, "controproposta": ref("counterproposal")})
    defs["flaw"]["properties"]["scenario_6_fasi"]["maxItems"] = 6
    defs["verdict"] = enum("accordo_solido", "falle_puntuali", "falle_strutturali", "device",
                            "degenerato", "fortezza_valida", "non_valutabile")
    decimal = {"type": "string", "pattern": r"^-?(?:0|[1-9][0-9]*)(?:\.[0-9]+)?$", "maxLength": 80}
    defs["arithmetic"] = obj({"verifica": TEXT, "operazione": enum("sum", "product", "percentage"),
                              "operandi": arr(decimal, 2), "risultato_dichiarato": decimal,
                              "esito": enum("coerente", "incoerente"),
                              "evidence": arr(ref("evidence"), 1)})
    defs["arithmetic"]["properties"]["operandi"]["maxItems"] = 20
    fields = {
        "accordo": TEXT, "versione_modulo": {"const": VERSION},
        "methodology_version": {"const": "0.1"}, "run_id": TEXT, "source_sha256": HASH,
        "prospettiva": enum("proponente", "destinatario", "neutra"),
        "modalita": {"const": "diagnostica"},
        "run_states": arr(enum("CONFORMANT_QUALITATIVE", "LLM_ONLY_UNVERIFIED", "DOCUMENT_ONLY",
                               "INCOMPATIBLE_STOP", "INVALID_OUTPUT"), 1, True),
        "dependency_ledger": arr(ref("dependency"), 11),
        "jurisdiction_gate": obj({"jurisdiction": {"type": ["string", "null"]},
                                  "choice_of_law": {"type": ["string", "null"]},
                                  "document_type": TEXT,
                                  "sources_as_of_date": {"type": ["string", "null"], "format": "date"},
                                  "external_sources_verified": {"const": False},
                                  "limits": arr(TEXT, 1)}),
        "insed": obj({"stato": TEXT, "qualificazione_parti": enum("B2C", "B2B", "C2C", "PA", "UNKNOWN"),
                      "perimetro_analisi": {"const": "documento_solo"}, "limiti": arr(TEXT),
                      "copertura": obj({"stato": enum("completa", "parziale", "non_eseguita"),
                                        "clausole_totali": arr(TEXT, 1, True),
                                        "clausole_non_esaminate": arr(TEXT, 0, True), "nota_limite": TEXT})}),
        "strip": arr(obj({"clausola": TEXT, "evidence": ref("evidence"), "iota": STRING,
                          "f_dichiarata": TEXT, "f_effettiva": TEXT, "payload": arr(TEXT)})),
        "campo_relazionale_R": arr(obj({"clausole_in_intersezione": arr(TEXT, 2, True),
                                         "giunzione": TEXT, "evidence": arr(ref("evidence"), 2)})),
        "phi_accordo": obj({"dichiarata": STRING, "effettiva": STRING, "delta": STRING, "confidence": CONF}),
        "consistenza": obj({"aritmetica": arr(ref("arithmetic")), "nota_aritmetica": TEXT,
                             "temporale": arr(obj({"verifica": TEXT,
                                                   "data_riferimento": {"type": "string", "format": "date"},
                                                   "esito": enum("coerente", "incoerente", "non_valutabile"),
                                                   "motivazione": TEXT, "evidence": arr(ref("evidence"), 1)})),
                             "nota_temporale": TEXT}),
        "falle": arr(ref("flaw")),
        "vettore_intenzione": obj({
            "semantic_scope": {"const": "vettore_strutturalmente_abilitato_non_intenzione_soggettiva"},
            "dichiarato": STRING, "effettivo": STRING, "delta_vettore": STRING,
            "tomografia": arr(obj({"clausola": TEXT, "payload": TEXT, "direzione": TEXT})),
            "lens": STRING, "confidence": enum("S1", "S2", "S3"), "nota_limite": TEXT}),
        "proporzione": obj({"mode": {"const": "qualitative"}, "band": enum("alta", "media", "bassa", "vuoto"),
                            "criterion": TEXT, "classe_equita": enum("equilibrata", "asimmetrica_dichiarata",
                                                                     "asimmetrica_occulta", "non_valutabile")}),
        "lyapunov_globale": ref("trajectory"),
        "non_falle_verificate": arr(obj({"clausola": TEXT, "sospetto": TEXT,
                                         "perche_non_falla": TEXT, "evidence": arr(ref("evidence"), 1)})),
        "note_negoziali": arr(obj({"clausola": TEXT, "nota": TEXT})),
        "verdetto_generale": ref("verdict"),
        "verdetti": obj({"testo": obj({"esito": ref("verdict"), "motivazione": TEXT, "confidence": CONF}),
                         "sistema": obj({"esito": {"const": "non_valutabile"}, "nota_limite": TEXT})}),
        "tre_mappe": obj({"cosa_dice": STRING, "cosa_non_dice": STRING, "cosa_dice_senza_dirlo": STRING}),
        "meta_pai": obj({"bias_rilevati": arr(TEXT), "note_trasparenza": TEXT,
                         "phi_test": obj({"funzione_attesa": TEXT, "riscontro": TEXT,
                                          "limiti_residui": arr(TEXT, 1)})}),
        "verification": {"const": {"executor": "llm_only", "anchors": "unverified",
                                     "schema": "unverified", "round_trip": "unverified"}},
    }
    return {"$schema": "https://json-schema.org/draft/2020-12/schema",
            "$id": "urn:lexx:output:0.2-alpha.3", "title": VERSION,
            **obj(fields), "$defs": defs}


if __name__ == "__main__":
    target = Path(__file__).resolve().parents[1] / "schemas" / "lexx_output.schema.json"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(contract(), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
