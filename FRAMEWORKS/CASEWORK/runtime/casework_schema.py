"""Strict, reproducible JSON contracts; no diagnostic or legal assertions."""
import json
from pathlib import Path

VERSION = "0.1.0-alpha.1"
TEXT = {"type": "string", "minLength": 1, "pattern": r"\S"}
STRING = {"type": "string"}
HASH = {"type": "string", "pattern": "^[0-9a-f]{64}$"}
BOOL = {"type": "boolean"}
CONF = {"enum": ["S0", "S1", "S2", "S3"]}
DATE = {"type": "string", "format": "date-time"}


def enum(*values):
    return {"enum": list(values)}


def obj(fields):
    return {"type": "object", "additionalProperties": False,
            "required": list(fields), "properties": fields}


def arr(item, minimum=0):
    return {"type": "array", "items": item, "minItems": minimum}


def ids():
    return {"type": "array", "items": TEXT, "uniqueItems": True}


def contract():
    alternative = obj({"explanation": TEXT, "test": TEXT,
                       "outcome": enum("pending", "supported", "refuted", "unresolved"),
                       "evidence_ids": ids()})
    finding = obj({
        "id": TEXT, "category": enum("anomaly", "control_weakness", "possible_abuse",
            "possible_fraud", "possible_corruption", "possible_violation"),
        "statement": TEXT, "criterion": obj({"kind": enum("policy", "contract", "expected_control", "legal_question"),
            "description": TEXT, "evidence_ids": ids(), "legal_reference_ids": ids()}),
        "supporting_evidence": ids(), "opposing_evidence": ids(), "counterevidence_search": TEXT,
        "alternatives": arr(alternative, 1), "confidence": enum("S1", "S2", "S3"),
        "impact": TEXT, "next_steps": arr(TEXT, 1),
        "disposition": enum("open", "supported", "not_supported", "unresolved")})
    schema = obj({
        "runtime_version": {"const": VERSION}, "case_id": TEXT, "manifest_sha256": HASH,
        "wave1_complete": BOOL,
        "documents": arr(obj({"id": TEXT, "reading": enum("pending", "read", "unreadable", "restricted"),
            "reading_note": STRING, "reviewer": STRING,
            "relevance": enum("deferred", "include", "exclude_provisional"), "relevance_reason": STRING,
            "exclusion_recheck": STRING, "source_group": TEXT, "group_reason": TEXT}), 1),
        "derivatives": arr(obj({"id": TEXT, "document_id": TEXT, "path": TEXT, "sha256": HASH,
            "method": TEXT, "operator": TEXT, "created_at": DATE})),
        "evidence": arr(obj({"id": TEXT, "document_id": TEXT,
            "derivative_id": {"type": ["string", "null"]}, "locator": TEXT, "quote": TEXT,
            "confidence": CONF})),
        "gaps": arr(obj({"id": TEXT, "expected_record": TEXT, "expectation_basis": TEXT,
            "search_performed": TEXT, "status": enum("not_provided", "not_found", "inaccessible", "resolved"),
            "next_step": TEXT})),
        "legal_references": arr(obj({"id": TEXT, "official_url": {"type": "string", "format": "uri"},
            "provision": TEXT, "jurisdiction": TEXT, "relevant_date": {"type": "string", "format": "date"},
            "checked_at": DATE, "checked_by": TEXT, "applicability_note": TEXT,
            "status": {"const": "reference_only_professional_validation_pending"}})),
        "analysis": obj({"complete": BOOL, "summary": STRING, "limitations": arr(TEXT)}),
        "audit": obj({"complete": BOOL, "checks": arr(obj({"id": TEXT, "area": TEXT,
            "status": enum("pending", "tested", "not_testable", "not_applicable"),
            "procedure": STRING, "population_and_scope": STRING, "result_note": STRING,
            "result": enum("pending", "no_exception", "exception", "inconclusive", "not_applicable"),
            "evidence_ids": ids(), "finding_ids": ids()}), 1), "findings": arr(finding)}),
        "hypotheses": arr(obj({"id": TEXT, "kind": enum("adverse", "non_criminal", "exculpatory", "alternative_cause"),
            "proposition": TEXT, "supporting_evidence": ids(), "opposing_evidence": ids(),
            "counterevidence_search": TEXT, "falsifier": TEXT, "next_check": TEXT,
            "status": enum("open", "supported", "disfavored", "unresolved")})),
        "chronology": arr(obj({"id": TEXT, "event": TEXT, "time_description": TEXT,
            "time_kind": enum("event", "document", "registration", "inferred", "unknown"),
            "evidence_ids": ids(), "confidence": CONF})),
        "relationships": arr(obj({"id": TEXT, "from_entity": TEXT, "to_entity": TEXT,
            "relation": TEXT, "evidence_ids": ids(), "confidence": CONF})),
    })
    schema["$schema"] = "https://json-schema.org/draft/2020-12/schema"
    return schema


def manifest_contract():
    return obj({"runtime_version": {"const": VERSION}, "case_id": TEXT, "created_at": DATE,
        "tool_versions": obj({"python": TEXT, "jsonschema": TEXT}),
        "source_directory": TEXT, "purpose": TEXT, "scope": TEXT, "owner": TEXT, "analyst": TEXT,
        "acquisition_authority_ref": TEXT, "mode": enum("audit", "investigation"),
        "investigation_mandate_ref": STRING, "supervising_role": STRING,
        "jurisdiction": TEXT, "synthetic": BOOL, "lock_sha256": HASH,
        "documents": arr(obj({"id": TEXT, "original_relative_path": TEXT, "path": TEXT,
            "sha256": HASH, "size": {"type": "integer", "minimum": 0}}), 1),
        "framework_files": arr(obj({"path": TEXT, "sha256": HASH}), 1)})


def review_contract():
    return obj({"case_sha256": HASH, "manifest_sha256": HASH,
        "reviewer": STRING, "reviewer_role": STRING,
        "decision": enum("pending", "accept", "revise"), "rationale": STRING,
        "reviewed_at": {"anyOf": [DATE, {"type": "null"}]},
        "checks": obj({name: enum("pending", "accept", "revise") for name in
            ("coverage", "anchors_and_interpretation", "source_independence", "alternatives", "bounded_conclusions")}),
        "legal_use": {"const": "not_authorized_by_runtime"}})


if __name__ == "__main__":
    destination = Path(__file__).resolve().parents[1] / "schemas"
    destination.mkdir(exist_ok=True)
    for name, schema in (("case", contract()), ("manifest", manifest_contract()), ("review", review_contract())):
        (destination / f"{name}.schema.json").write_text(json.dumps(schema, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
