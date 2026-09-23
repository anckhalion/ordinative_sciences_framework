"""Synthetic contract/regression tests. Not tests of diagnostic accuracy."""
import copy
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "runtime"))
import casework as cw
from casework_schema import contract, manifest_contract, review_contract


class CaseworkTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.source = self.root / "source"
        self.source.mkdir()
        (self.source / "invoice.txt").write_text("INVOICE A: 100 EUR; delivery pending.\n", encoding="utf-8")
        (self.source / "payment.txt").write_text("PAYMENT A: 100 EUR; settled once.\n", encoding="utf-8")
        self.frameworks = self.root / "frameworks"
        (self.frameworks / "CASEWORK" / "runtime").mkdir(parents=True)
        (self.frameworks / "TE_CORE_v5_2_1_EN.md").write_text("SYNTHETIC DEPENDENCY FIXTURE ONLY", encoding="utf-8")
        profile = {"dependencies": [{"family": "TE_CORE", "version": "5.2.1",
            "digest": cw.file_hash(self.frameworks / "TE_CORE_v5_2_1_EN.md")}]}
        cw.write_new(self.frameworks / "CASEWORK" / "compatibility.json", profile)
        for name in ("casework.py", "casework_schema.py"):
            (self.frameworks / "CASEWORK" / "runtime" / name).write_bytes((ROOT / "runtime" / name).read_bytes())
        files = [{"relative_path": p.relative_to(self.frameworks).as_posix(), "sha256": cw.file_hash(p)}
                 for p in (self.frameworks / "CASEWORK").rglob("*") if p.is_file()]
        self.lock = self.root / "lock.json"
        cw.write_new(self.lock, {"families": {
            "TE_CORE": {"version": "5.2.1", "snapshot_path": "TE_CORE_v5_2_1_EN.md", "sha256": profile["dependencies"][0]["digest"]},
            "TE_CASEWORK": {"version": cw.VERSION, "files": files}}})
        self.run = self.root / "run"
        self.metadata = dict(case_id="SYNTHETIC-ONLY", purpose="Contract tests, no real case", scope="Two synthetic records",
            owner="Test owner", analyst="Test analyst", acquisition_authority_ref="Synthetic fixture authorization",
            mode="audit", investigation_mandate_ref="", supervising_role="", jurisdiction="IT", synthetic=True)
        cw.prepare(self.source, self.run, self.frameworks, self.lock, **self.metadata)
        self.data = cw.load_json(self.run / "case.json")

    def save(self):
        (self.run / "case.json").write_text(json.dumps(self.data), encoding="utf-8")

    def validate(self, review=None):
        self.save()
        return cw.validate(self.run, review)

    def wave(self):
        self.data["wave1_complete"] = True
        for item in self.data["documents"]:
            item.update(reading="read", reading_note="Synthetic text read", reviewer="Test analyst",
                        relevance="include", relevance_reason="Relevant to fixture")

    def evidence(self):
        self.data["evidence"] = [
            {"id": "E1", "document_id": "DOC-00001", "derivative_id": None,
             "locator": "line 1", "quote": "INVOICE A: 100 EUR", "confidence": "S0"},
            {"id": "E2", "document_id": "DOC-00002", "derivative_id": None,
             "locator": "line 1", "quote": "PAYMENT A: 100 EUR", "confidence": "S0"}]

    def closed(self):
        self.wave()
        self.evidence()
        self.data["analysis"] = {"complete": True, "summary": "Synthetic supplied-record exercise.", "limitations": ["Not an empirical test."]}
        self.data["audit"]["complete"] = True
        for check in self.data["audit"]["checks"]:
            check.update(status="not_applicable", procedure="Review fixture applicability",
                         population_and_scope="Two synthetic documents only", result_note="Outside this synthetic fixture",
                         result="not_applicable")
        self.data["audit"]["checks"][0].update(status="tested", result="no_exception", evidence_ids=["E1", "E2"],
                                               result_note="Only declared literal anchors checked in synthetic fixture")

    def finding(self):
        self.evidence()
        self.data["audit"]["findings"] = [{"id": "F1", "category": "anomaly", "statement": "Delivery support to verify",
            "criterion": {"kind": "expected_control", "description": "Reconcile performance and payment",
                          "evidence_ids": [], "legal_reference_ids": []},
            "supporting_evidence": ["E1", "E2"], "opposing_evidence": [],
            "counterevidence_search": "Only synthetic invoice/payment considered; no conclusion of fraud",
            "alternatives": [{"explanation": "Delivery record not supplied", "test": "Request delivery record",
                              "outcome": "pending", "evidence_ids": []}],
            "confidence": "S2", "impact": "Unknown", "next_steps": ["Check fulfillment"], "disposition": "open"}]

    def rejected(self, phrase):
        with self.assertRaisesRegex(ValueError, phrase):
            self.validate()

    def test_empty_draft_not_analysis(self):
        report = self.validate()
        self.assertEqual(report["phase"], "wave1")
        self.assertEqual(report["legal_use"], "not_authorized_by_runtime")
        self.assertEqual(report["empirical_performance"], "not_assessed")

    def test_no_overwrite(self):
        with self.assertRaisesRegex(ValueError, "Destination exists"):
            cw.prepare(self.source, self.run, self.frameworks, self.lock, **self.metadata)

    def test_run_inside_source_rejected(self):
        with self.assertRaisesRegex(ValueError, "inside source"):
            cw.prepare(self.source, self.source / "run", self.frameworks, self.lock, **self.metadata)

    def test_empty_input_rejected(self):
        empty = self.root / "empty"
        empty.mkdir()
        with self.assertRaisesRegex(ValueError, "Empty source"):
            cw.prepare(empty, self.root / "new", self.frameworks, self.lock, **self.metadata)

    def test_no_relevance_before_wave(self):
        self.data["documents"][0].update(relevance="exclude_provisional", relevance_reason="Looks unimportant")
        self.rejected("before first-wave")

    def test_wave_pending_rejected(self):
        self.data["wave1_complete"] = True
        self.rejected("Wave 1 incomplete")

    def test_false_reading_without_reviewer_rejected(self):
        self.data["documents"][0]["reading"] = "read"
        self.rejected("reviewer and rationale")

    def test_document_omission_rejected(self):
        self.data["documents"].pop()
        self.rejected("Coverage inventory")

    def test_duplicate_ids_rejected(self):
        self.data["documents"].append(copy.deepcopy(self.data["documents"][0]))
        self.rejected("Duplicate record ID")

    def test_original_tampering_rejected(self):
        (self.run / "originals" / "DOC-00001.bin").write_text("changed", encoding="utf-8")
        self.rejected("Original changed")

    def test_framework_tampering_rejected(self):
        (self.run / "frameworks" / "TE_CORE_v5_2_1_EN.md").write_text("changed", encoding="utf-8")
        self.rejected("Framework hash mismatch")

    def test_literal_quote_required(self):
        self.evidence()
        self.data["evidence"][0]["quote"] = "Invented confession"
        self.rejected("Quotation not found")

    def test_unresolved_reference_rejected(self):
        self.finding()
        self.data["audit"]["findings"][0]["opposing_evidence"] = ["nonexistent"]
        self.rejected("Unresolved")

    def test_alternative_explanation_required(self):
        self.finding()
        self.data["audit"]["findings"][0]["alternatives"] = []
        self.rejected("Schema")

    def test_confidence_inflation_rejected(self):
        self.finding()
        self.data["evidence"][0]["confidence"] = "S3"
        self.rejected("Confidence inflated")

    def test_single_origin_not_triangulation(self):
        self.finding()
        self.data["audit"]["findings"][0].update(confidence="S1", supporting_evidence=["E1"])
        self.rejected("two declared origin")

    def test_identical_copies_not_independent(self):
        duplicate_source = self.root / "duplicates"
        duplicate_source.mkdir()
        for name in ("a.txt", "b.txt"):
            (duplicate_source / name).write_text("Same source", encoding="utf-8")
        duplicate_run = self.root / "duplicate_run"
        cw.prepare(duplicate_source, duplicate_run, self.frameworks, self.lock, **self.metadata)
        self.run = duplicate_run
        self.data = cw.load_json(self.run / "case.json")
        self.assertEqual(self.data["documents"][0]["source_group"], self.data["documents"][1]["source_group"])
        self.data["documents"][1]["source_group"] = "Pretend independent"
        self.rejected("Identical bytes")

    def test_unreadable_cannot_be_irrelevant(self):
        self.wave()
        self.data["documents"][0].update(reading="unreadable", relevance="exclude_provisional")
        self.rejected("Unread/restricted")

    def test_analysis_automatically_requires_audit(self):
        self.wave()
        self.data["analysis"].update(complete=True, summary="Synthetic first analysis")
        self.assertEqual(self.validate()["phase"], "audit_required")

    def test_audit_cannot_skip_pending_checks(self):
        self.wave()
        self.data["analysis"].update(complete=True, summary="Synthetic analysis")
        self.data["audit"]["complete"] = True
        self.rejected("Mandatory audit pass incomplete")

    def test_area_removal_rejected(self):
        self.data["audit"]["checks"].pop()
        self.rejected("area missing")

    def test_audit_reconsiders_exclusions(self):
        self.closed()
        self.data["documents"][0]["relevance"] = "exclude_provisional"
        self.rejected("reconsider exclusions")

    def test_not_testable_not_passed(self):
        self.closed()
        self.data["audit"]["checks"][0].update(status="not_testable", result="no_exception")
        self.rejected("status/result mismatch")

    def test_closed_with_no_findings_still_needs_review(self):
        self.closed()
        self.assertEqual(self.validate()["phase"], "independent_review_required")
        self.assertEqual(self.validate()["finding_count"], 0)

    def review(self):
        self.save()
        review = cw.review_template(self.run)
        review.update(reviewer="Distinct test reviewer", reviewer_role="Synthetic contract reviewer", decision="accept",
                      rationale="Only checks fixture consistency", reviewed_at=cw.now())
        review["checks"] = {key: "accept" for key in review["checks"]}
        path = self.run / "review.json"
        path.write_text(json.dumps(review), encoding="utf-8")
        return path

    def test_review_recorded_not_authenticated(self):
        self.closed()
        result = self.validate(self.review())
        self.assertEqual(result["phase"], "documentary_pass_review_recorded")
        self.assertEqual(result["review"], "accept_recorded_identity_unverified")
        self.assertEqual(result["legal_use"], "not_authorized_by_runtime")

    def test_revision_invalidates_review(self):
        self.closed()
        path = self.review()
        self.data["analysis"]["summary"] = "Revision"
        with self.assertRaisesRegex(ValueError, "Review invalidated"):
            self.validate(path)

    def test_self_review_rejected(self):
        self.closed()
        path = self.review()
        review = cw.load_json(path)
        review["reviewer"] = "  TEST ANALYST "
        path.write_text(json.dumps(review), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "distinct"):
            self.validate(path)

    def test_investigation_requires_explicit_mandate(self):
        metadata = {**self.metadata, "mode": "investigation"}
        with self.assertRaisesRegex(ValueError, "mandate"):
            cw.prepare(self.source, self.root / "invest", self.frameworks, self.lock, **metadata)

    def investigator(self):
        metadata = {**self.metadata, "mode": "investigation", "investigation_mandate_ref": "Synthetic mandate",
                    "supervising_role": "Synthetic supervisor, not professional validation"}
        self.run = self.root / "invest"
        cw.prepare(self.source, self.run, self.frameworks, self.lock, **metadata)
        self.data = cw.load_json(self.run / "case.json")
        self.closed()

    def test_investigation_requires_alternative_hypotheses(self):
        self.investigator()
        self.rejected("competing")

    def test_defensive_alternative_with_adverse_evidence_retained(self):
        self.investigator()
        for identity, kind in (("H1", "adverse"), ("H2", "non_criminal")):
            self.data["hypotheses"].append({"id": identity, "kind": kind, "proposition": "Synthetic competing reconstruction",
                "supporting_evidence": ["E1"], "opposing_evidence": ["E2"],
                "counterevidence_search": "Both synthetic documents considered", "falsifier": "New delivery records",
                "next_check": "Request authorized records", "status": "unresolved"})
        self.assertEqual(self.validate()["phase"], "independent_review_required")

    def test_derivative_provenance_and_quote(self):
        self.evidence()
        path = self.run / "derived" / "extract.txt"
        path.write_text("Authorized extraction", encoding="utf-8")
        self.data["derivatives"] = [{"id": "X1", "document_id": "DOC-00001", "path": "derived/extract.txt",
            "sha256": cw.file_hash(path), "method": "Synthetic fixture", "operator": "Test analyst", "created_at": cw.now()}]
        self.data["evidence"][0].update(derivative_id="X1", quote="Authorized extraction")
        self.validate()
        path.write_text("Changed extraction", encoding="utf-8")
        self.rejected("Derivative changed")

    def test_path_traversal_rejected(self):
        for relative in ("../escape", "C:/secret", "derived/a:ads", "/etc/passwd", "derived\\x"):
            with self.subTest(relative=relative), self.assertRaises(ValueError):
                cw.within(self.run, relative)

    def test_schema_rejects_fraud_certification(self):
        self.data["guilty"] = True
        self.rejected("Schema")

    def test_schema_rejects_impossible_date(self):
        self.data["legal_references"] = [{"id": "L1", "official_url": "https://example.invalid/",
            "provision": "Synthetic", "jurisdiction": "IT", "relevant_date": "2026-02-31",
            "checked_at": cw.now(), "checked_by": "Fixture", "applicability_note": "Not law",
            "status": "reference_only_professional_validation_pending"}]
        self.rejected("Schema")

    def test_duplicate_json_and_nan_rejected(self):
        path = self.root / "bad.json"
        for raw in ('{"x": 1, "x": 2}', '{"x": NaN}'):
            path.write_text(raw, encoding="utf-8")
            with self.assertRaises(ValueError):
                cw.load_json(path)

    def test_schema_generation_reproducible(self):
        for name, schema in (("case", contract()), ("manifest", manifest_contract()), ("review", review_contract())):
            self.assertEqual(cw.load_json(ROOT / "schemas" / f"{name}.schema.json"), schema)

    def test_extra_original_requires_new_inventory(self):
        (self.run / "originals" / "extra.bin").write_bytes(b"Unrecorded document")
        self.rejected("inventory differs")

    def test_sources_unchanged(self):
        manifest = cw.load_json(self.run / "manifest.json")
        for document in manifest["documents"]:
            self.assertEqual(cw.file_hash(self.source / document["original_relative_path"]), document["sha256"])

    def test_frozen_lock_tampering_rejected(self):
        (self.run / "te_frameworks.lock.json").write_text("{}", encoding="utf-8")
        self.rejected("Frozen lock changed")

    def test_legal_question_requires_reference(self):
        self.finding()
        self.data["audit"]["findings"][0]["criterion"]["kind"] = "legal_question"
        self.rejected("requires a reference")

    def test_execution_environment_change_rejected(self):
        with patch.object(cw, "tool_versions", return_value={"python": "different", "jsonschema": "different"}):
            self.rejected("environment differs")

    def test_inaccessible_subtree_is_not_silently_omitted(self):
        def bad_walk(source, onerror, followlinks):
            onerror(PermissionError("Cannot enumerate subtree"))
            return iter(())
        with patch.object(cw.os, "walk", side_effect=bad_walk):
            with self.assertRaises(PermissionError):
                cw.source_inventory(self.source)


if __name__ == "__main__":
    unittest.main()
