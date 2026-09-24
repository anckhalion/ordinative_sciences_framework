import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "runtime"))
import validate_lexx_output as runtime
from build_schema import contract
from prepare_run import template, prepare, package_documents
from prepare_review import review_template


SOURCE = "C1. Il servizio dura dodici mesi.\nC2. Il prezzo totale è 1200 euro.\nC3. Il Cliente può recedere.\n"


class RuntimeTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.source = self.root / "source.txt"
        self.output = self.root / "output.json"
        self.schema = self.root / "schema.json"
        self.source.write_text(SOURCE, encoding="utf-8")
        self.schema.write_text(json.dumps(contract()), encoding="utf-8")
        self.frameworks = self.root / "frameworks"
        self.frameworks.mkdir()
        profile = json.loads((ROOT / "compatibility.json").read_text(encoding="utf-8"))
        for item in profile["dependencies"]:
            raw = f"TEST FIXTURE ONLY: {item['component']} {item['version']}".encode()
            (self.frameworks / item["file"]).write_bytes(raw)
            item["sha256"] = runtime.sha256_bytes(raw)
        (self.root / "compatibility.json").write_text(json.dumps(profile), encoding="utf-8")
        self.patch = patch.object(runtime, "ROOT", self.root)
        self.patch.start()
        self.addCleanup(self.patch.stop)
        ledger = runtime.dependency_ledger(self.frameworks)
        self.base = template(runtime.sha256_bytes(self.source.read_bytes()), ledger, "synthetic-run")
        self.base["accordo"] = "SYNTHETIC TEST ONLY"
        self.base["insed"]["copertura"] = {"stato": "completa", "clausole_totali": ["C1", "C2", "C3"],
                                           "clausole_non_esaminate": [], "nota_limite": "Synthetic text only."}
        for index, line in enumerate(SOURCE.strip().splitlines(), 1):
            self.base["strip"].append({"clausola": f"C{index}", "evidence": self.quote(line),
                                      "iota": "erogazione del servizio", "f_dichiarata": "servizio",
                                      "f_effettiva": "servizio", "payload": []})
        self.base["verdetto_generale"] = "accordo_solido"
        self.base["verdetti"]["testo"] = {"esito": "accordo_solido", "motivazione": "Synthetic mechanics fixture", "confidence": "S3"}

    @staticmethod
    def quote(text):
        return {"anchor_type": "literal_quote", "quote": text, "evidence_level": "E0"}

    def run_data(self, data=None, review=None):
        self.output.write_text(json.dumps(data if data is not None else self.base, ensure_ascii=False), encoding="utf-8")
        review_path = None
        if review is not None:
            review_path = self.root / "review.json"
            review_path.write_text(json.dumps(review), encoding="utf-8")
        return runtime.validate(self.source, self.output, self.schema, self.frameworks, review_path)

    def assertCode(self, report, code):
        self.assertFalse(report["valid"], report)
        self.assertIn(code, {item["code"] for item in report["errors"]}, report)

    def with_flaw(self):
        data = copy.deepcopy(self.base)
        data["verdetto_generale"] = data["verdetti"]["testo"]["esito"] = "falle_puntuali"
        data["falle"] = [{"id": "FX-1", "clausole": ["C3"], "vettore_primario": "V-OM",
            "evidence": [self.quote("Il Cliente può recedere.")], "mechanism": "Termine non espresso",
            "impact": "Incertezza sul preavviso", "confidence": "S2",
            "scenario_6_fasi": ["scenario sintetico"] * 6,
            "test_contrario": {"esito": "confermata", "interpretazione_alternativa": "Recesso immediato",
                               "motivazione": "Ipotesi da sottoporre al revisore"},
            "classe_oct": "non_valutabile", "motivazione_classe": "Non certificata",
            "dote_residuo": 1, "motivazione_residuo": "Richiede cooperazione",
            "lyapunov": {"mode": "qualitative", "lambda_segno": "pos", "argomento": "Controversia possibile"},
            "cvi_banda": "alta", "criterio_cvi": "Precisare preavviso",
            "mitigazione_esterna": "Non valutata",
            "controproposta": {"status": "proposed", "tipo": "riscrittura_pi",
                "forma_equa": "Il Cliente può recedere con preavviso di trenta giorni.",
                "iota_originale": "erogazione del servizio",
                "ri_strip": {"iota_primo": "erogazione del servizio", "payload_primo": [],
                             "argomento_preservazione": "Continuità del servizio nel preavviso"},
                "lambda_post": "neg", "argomento_lambda_post": "Termine esplicito"}}]
        return data

    def complete_review(self, data):
        self.run_data(data)
        review = review_template(self.source, self.output)
        review.update(reviewer_id="synthetic-reviewer", review_run_id="synthetic-review-2", independent_declared=True)
        review["items"][0].update(independent_restrip={"iota_primo": "servizio", "payload_primo": []},
                                  invariant_preserved=True, lambda_post="neg", reason="Synthetic positive receipt")
        return review

    def test_positive(self):
        result = self.run_data()
        self.assertTrue(result["valid"], result)
        self.assertEqual(result["metrics"]["anchors_checked"], 3)
        self.assertFalse(result["empirical_validation"])
        self.assertEqual(result["technical_status"], "TECHNICALLY_CHECKED")

    def test_real_schema_rejects_nested_wrong_type(self):
        self.base["strip"] = 7
        self.assertCode(self.run_data(), "SCHEMA")

    def test_schema_rejects_unknown_fields(self):
        self.base["invented"] = True
        self.assertCode(self.run_data(), "SCHEMA")

    def test_schema_requires_consistency_stage(self):
        del self.base["consistenza"]
        self.assertCode(self.run_data(), "SCHEMA")

    def test_date_validation(self):
        self.base["jurisdiction_gate"]["sources_as_of_date"] = "2026-02-30"
        self.assertCode(self.run_data(), "SCHEMA")

    def test_unknown_states_and_bad_types(self):
        self.base["run_states"] = [{"fake": "CONFORMANT_VERIFIED"}]
        self.assertCode(self.run_data(), "SCHEMA")

    def test_source_hash(self):
        self.base["source_sha256"] = "0" * 64
        self.assertCode(self.run_data(), "SOURCE_HASH")

    def test_missing_quote(self):
        self.base["strip"][0]["evidence"]["quote"] = "Clausola inventata"
        self.assertCode(self.run_data(), "ANCHOR_NOT_FOUND")

    def test_quote_is_case_sensitive(self):
        self.base["strip"][0]["evidence"]["quote"] = "IL SERVIZIO DURA DODICI MESI."
        self.assertCode(self.run_data(), "ANCHOR_NOT_FOUND")

    def test_whitespace_normalization(self):
        self.base["strip"][0]["evidence"]["quote"] = "C1. Il servizio\n dura  dodici mesi."
        self.assertTrue(self.run_data()["valid"])

    def test_reversed_absence_context(self):
        self.base["strip"][0]["evidence"] = {"anchor_type": "structural_absence",
            "context_before": "Il Cliente può recedere.", "context_after": "Il servizio dura dodici mesi.",
            "missing_slot": "preavviso", "evidence_level": "E1"}
        self.assertCode(self.run_data(), "ABSENCE_CONTEXT_ORDER")

    def test_dependency_ledger_cannot_be_asserted(self):
        self.base["dependency_ledger"][0]["sha256"] = "0" * 64
        self.assertCode(self.run_data(), "DEPENDENCY_LEDGER")

    def test_changed_dependency_blocks(self):
        path = self.frameworks / self.base["dependency_ledger"][0]["source_file"]
        path.write_text("changed", encoding="utf-8")
        self.assertCode(self.run_data(), "INPUT_OR_CONFIGURATION")

    def test_self_verification_forbidden(self):
        self.base["verification"]["schema"] = "verified"
        self.assertCode(self.run_data(), "SCHEMA")

    def test_external_law_not_self_verified(self):
        self.base["jurisdiction_gate"]["external_sources_verified"] = True
        self.assertCode(self.run_data(), "SCHEMA")

    def test_numeric_engine_not_implemented(self):
        self.base["proporzione"] = {"mode": "quantitative_engine", "engine": "imaginary", "value": 0.5}
        self.assertCode(self.run_data(), "SCHEMA")

    def test_intent_never_s0(self):
        self.base["vettore_intenzione"]["confidence"] = "S0"
        self.assertCode(self.run_data(), "SCHEMA")

    def test_s1_requires_three_anchored_clauses(self):
        self.base["vettore_intenzione"].update(confidence="S1", effettivo="direzione")
        self.assertCode(self.run_data(), "S1_CONVERGENCE")

    def test_partial_coverage_not_solid(self):
        self.base["insed"]["copertura"]["stato"] = "parziale"
        self.assertCode(self.run_data(), "PARTIAL_POSITIVE_VERDICT")

    def test_confidence_cannot_increase(self):
        self.base["verdetti"]["testo"]["confidence"] = "S0"
        self.assertCode(self.run_data(), "CONFIDENCE_INFLATION")

    def test_stopped_run_never_passes(self):
        self.base["run_states"].append("INCOMPATIBLE_STOP")
        self.assertCode(self.run_data(), "STOP_STATE")

    def test_forgotten_document_only(self):
        self.base["run_states"].remove("DOCUMENT_ONLY")
        self.assertCode(self.run_data(), "REQUIRED_STATES")

    def test_bad_clause_reference(self):
        data = self.with_flaw()
        data["falle"][0]["clausole"] = ["C999"]
        self.assertCode(self.run_data(data), "UNKNOWN_CLAUSE")

    def test_intersection_needs_two_clauses(self):
        data = self.with_flaw()
        data["falle"][0]["vettore_primario"] = "V-IN"
        self.assertCode(self.run_data(data), "INTERSECTION_ARITY")

    def test_arithmetic_recalculated(self):
        self.base["consistenza"]["aritmetica"] = [{"verifica": "12 x 100", "operazione": "product",
            "operandi": ["12", "100"], "risultato_dichiarato": "1200", "esito": "incoerente",
            "evidence": [self.quote("Il prezzo totale è 1200 euro.")]}]
        self.assertCode(self.run_data(), "ARITHMETIC_RESULT")
        self.base["consistenza"]["aritmetica"][0]["esito"] = "coerente"
        self.assertTrue(self.run_data()["valid"])

    def test_round_trip_is_pending_without_review(self):
        result = self.run_data(self.with_flaw())
        self.assertTrue(result["valid"], result)
        self.assertEqual(result["round_trip"], "pending_independent_review")

    def test_independent_review_recorded(self):
        data = self.with_flaw()
        result = self.run_data(data, self.complete_review(data))
        self.assertTrue(result["valid"], result)
        self.assertEqual(result["round_trip"], "recorded_pass")

    def test_review_invalidated_by_output_change(self):
        data = self.with_flaw()
        review = self.complete_review(data)
        data["falle"][0]["controproposta"]["forma_equa"] += " Modificato."
        self.assertCode(self.run_data(data, review), "REVIEW_BINDING")

    def test_reviewer_failure_blocks(self):
        data = self.with_flaw()
        review = self.complete_review(data)
        review["items"][0]["independent_restrip"]["payload_primo"] = ["Controllo residuo"]
        self.assertCode(self.run_data(data, review), "ROUND_TRIP_FAILED")

    def test_review_same_run_not_independent(self):
        data = self.with_flaw()
        review = self.complete_review(data)
        review["review_run_id"] = data["run_id"]
        self.assertCode(self.run_data(data, review), "REVIEW_INDEPENDENCE")

    def test_review_malformed_does_not_crash(self):
        self.assertCode(self.run_data(self.with_flaw(), []), "REVIEW_FORMAT")

    def test_empty_template_is_not_analysis(self):
        draft = template(self.base["source_sha256"], self.base["dependency_ledger"])
        result = self.run_data(draft)
        self.assertTrue(result["valid"], result)
        self.assertEqual(result["analysis_status"], "not_assessed")
        self.assertFalse(result["ready_for_independent_review"])

    def test_invalid_utf8_reported(self):
        self.source.write_bytes(b"\xff\xfe")
        self.assertCode(self.run_data(), "INPUT_OR_CONFIGURATION")

    def test_duplicate_json_keys_reported(self):
        self.output.write_text('{"a":1,"a":2}', encoding="utf-8")
        self.assertCode(runtime.validate(self.source, self.output, self.schema, self.frameworks), "INPUT_OR_CONFIGURATION")

    def test_nan_rejected(self):
        self.output.write_text('{"a":NaN}', encoding="utf-8")
        self.assertCode(runtime.validate(self.source, self.output, self.schema, self.frameworks), "INPUT_OR_CONFIGURATION")

    def test_tampered_schema_rejected(self):
        self.schema.write_text('{"type":42}', encoding="utf-8")
        self.assertCode(self.run_data(), "INPUT_OR_CONFIGURATION")

    def test_shipped_schema_matches_builder(self):
        shipped = json.loads((ROOT / "schemas" / "lexx_output.schema.json").read_text(encoding="utf-8"))
        self.assertEqual(shipped, contract())

    def test_frozen_manifest_detects_change(self):
        self.run_data()
        frozen = self.root / "frozen.txt"
        frozen.write_text("original", encoding="utf-8")
        manifest = self.root / "run_manifest.json"
        manifest.write_text(json.dumps({"source_sha256": self.base["source_sha256"],
            "run_id": self.base["run_id"], "frozen_files": {"frozen.txt": runtime.sha256_bytes(frozen.read_bytes())}}), encoding="utf-8")
        frozen.write_text("changed", encoding="utf-8")
        result = runtime.validate(self.source, self.output, self.schema, self.frameworks, manifest_path=manifest)
        self.assertCode(result, "FROZEN_FILE_CHANGED")

    def test_report_does_not_call_rejected_review_a_pass(self):
        data = self.with_flaw()
        review = self.complete_review(data)
        review["output_sha256"] = "0" * 64
        result = self.run_data(data, review)
        self.assertFalse(result["valid"])
        self.assertNotEqual(result["round_trip"], "recorded_pass")

    def test_package_documents_resolve_by_edition(self):
        folder = self.root / "lexx_docs"
        folder.mkdir()
        english = ["README.md", "00_FOUNDATIONS.md", "TE_MODULE_LEXX_v0_1_EN.md", "03_PRE_PILOT_PROTOCOL.md", "release.json"]
        for name in english:
            (folder / name).write_text("fixture", encoding="utf-8")
        self.assertEqual([path.name for path in package_documents(folder)], english)
        (folder / "00_FONDAMENTA.md").write_text("fixture", encoding="utf-8")
        self.assertIn("00_FONDAMENTA.md", [path.name for path in package_documents(folder)])
        (folder / "00_FONDAMENTA.md").unlink()
        (folder / "00_FOUNDATIONS.md").unlink()
        with self.assertRaises(FileNotFoundError):
            package_documents(folder)


if __name__ == "__main__":
    unittest.main()
