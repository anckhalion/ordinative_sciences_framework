"""Prepare/freeze a local dossier and validate declared documentary workflow.

No OCR, inference engine, surveillance, witness contact, legal verdict or network.
"""
from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime, timezone
import hashlib
import importlib.metadata
import json
import os
from pathlib import Path, PurePosixPath
import platform
import shutil
import stat

from jsonschema import Draft202012Validator, FormatChecker
from casework_schema import VERSION, contract, manifest_contract, review_contract

ROOT = Path(__file__).resolve().parents[1]
AUDIT_AREAS = ("source_integrity", "finance", "procurement", "authorizations", "governance",
               "people_internal_abuse", "assets_resources", "information_reporting")
INVESTIGATION_AREAS = ("source_integrity", "chronology", "attribution", "counterevidence")


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def file_hash(path):
    value = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            value.update(block)
    return value.hexdigest()


def now():
    return datetime.now(timezone.utc).isoformat()


def tool_versions():
    return {"python": platform.python_version(), "jsonschema": importlib.metadata.version("jsonschema")}


def source_inventory(source):
    """Do not silently omit an inaccessible subtree, link or special file."""
    def fail(error):
        raise error
    inventory = []
    for directory, subdirs, names in os.walk(source, onerror=fail, followlinks=False):
        for name in subdirs + names:
            no_link(Path(directory) / name)
        for name in names:
            path = Path(directory) / name
            if not stat.S_ISREG(path.stat().st_mode):
                raise ValueError(f"Non-regular input file: {path}")
            inventory.append(path)
    return sorted(inventory)


def load_json(path):
    def pairs(values):
        result = {}
        for key, value in values:
            if key in result:
                raise ValueError(f"Duplicate JSON key: {key}")
            result[key] = value
        return result
    def bad_number(value):
        raise ValueError(f"Non-finite JSON number: {value}")
    return json.loads(Path(path).read_text(encoding="utf-8-sig"),
                      object_pairs_hook=pairs, parse_constant=bad_number)


def write_new(path, value):
    with Path(path).open("x", encoding="utf-8") as stream:
        stream.write(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


def check_schema(value, schema):
    errors = sorted(Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(value),
                    key=lambda e: str(list(e.absolute_path)))
    if errors:
        raise ValueError("Schema: " + "; ".join(f"{list(e.absolute_path)}: {e.message}" for e in errors[:12]))


def no_link(path):
    info = Path(path).lstat()
    if stat.S_ISLNK(info.st_mode) or getattr(info, "st_file_attributes", 0) & stat.FILE_ATTRIBUTE_REPARSE_POINT:
        raise ValueError(f"Symlink/reparse-point source not supported: {path}")


def within(root, relative):
    """Reject traversal, Windows ADS/absolute paths, and link traversal."""
    if not isinstance(relative, str) or "\\" in relative or ":" in relative:
        raise ValueError("Unsafe relative path")
    rel = PurePosixPath(relative)
    if rel.is_absolute() or not rel.parts or any(part in (".", "..") for part in rel.parts):
        raise ValueError("Unsafe relative path")
    base = Path(root).resolve()
    candidate = base.joinpath(*rel.parts)
    if not candidate.resolve().is_relative_to(base):
        raise ValueError("Path escapes packet")
    current = base
    for part in rel.parts:
        current /= part
        if current.exists() or current.is_symlink():
            no_link(current)
    return candidate


def lock_files(lock):
    result = {}
    for entry in lock["families"].values():
        records = ([{"relative_path": entry["snapshot_path"], "sha256": entry["sha256"]}]
                   if "sha256" in entry else entry["files"])
        for item in records:
            relative = item["relative_path"]
            if relative in result:
                raise ValueError(f"Duplicate snapshot path: {relative}")
            result[relative] = item["sha256"]
    return result


def verify_frameworks(framework_root, lock):
    expected = lock_files(lock)
    for relative, expected_hash in expected.items():
        if file_hash(within(framework_root, relative)) != expected_hash:
            raise ValueError(f"Framework hash mismatch: {relative}")
    profile = load_json(within(framework_root, "CASEWORK/compatibility.json"))
    for entry in profile["dependencies"]:
        actual = lock["families"].get(entry["family"])
        if not actual or actual["version"] != entry["version"]:
            raise ValueError(f"Unreviewed dependency version: {entry['family']}")
        actual_hash = actual.get("sha256", actual.get("package_digest"))
        if actual_hash != entry["digest"]:
            raise ValueError(f"Unreviewed dependency content: {entry['family']}")
    # Executing code must be the frozen/reviewed code, not an unrelated script.
    for name in ("casework.py", "casework_schema.py"):
        if file_hash(Path(__file__).parent / name) != expected.get(f"CASEWORK/runtime/{name}"):
            raise ValueError("Executing runtime differs from snapshot")
    return expected


def blank_case(manifest, manifest_hash):
    areas = AUDIT_AREAS if manifest["mode"] == "audit" else INVESTIGATION_AREAS
    return {"runtime_version": VERSION, "case_id": manifest["case_id"], "manifest_sha256": manifest_hash,
        "wave1_complete": False,
        "documents": [{"id": d["id"], "reading": "pending", "reading_note": "", "reviewer": "",
            "relevance": "deferred", "relevance_reason": "", "exclusion_recheck": "",
            "source_group": d["sha256"], "group_reason": "Initial byte-origin grouping; semantic independence unreviewed."}
            for d in manifest["documents"]],
        "derivatives": [], "evidence": [], "gaps": [], "legal_references": [],
        "analysis": {"complete": False, "summary": "", "limitations": []},
        "audit": {"complete": False, "findings": [], "checks": [
            {"id": f"CHECK-{index}", "area": area, "status": "pending", "procedure": "",
             "population_and_scope": "", "result_note": "", "result": "pending", "evidence_ids": [], "finding_ids": []}
            for index, area in enumerate(areas, 1)]},
        "hypotheses": [], "chronology": [], "relationships": []}


def prepare(source, destination, frameworks, lock_path, **metadata):
    source, destination, frameworks = Path(source), Path(destination), Path(frameworks)
    if destination.exists():
        raise ValueError("Destination exists; use a new run directory")
    no_link(source)
    if not source.is_dir():
        raise ValueError("Source must be an authorized directory")
    if destination.resolve().is_relative_to(source.resolve()):
        raise ValueError("Run directory cannot be inside source")
    for parent in (source, *source.parents, destination.parent, *destination.parent.parents):
        if parent.exists():
            no_link(parent)
    inventory = source_inventory(source)
    if not inventory:
        raise ValueError("Empty source inventory")
    lock = load_json(lock_path)
    expected = verify_frameworks(frameworks, lock)
    records = [{"id": f"DOC-{index:05}", "original_relative_path": p.relative_to(source).as_posix(),
                "path": f"originals/DOC-{index:05}.bin", "sha256": file_hash(p), "size": p.stat().st_size}
               for index, p in enumerate(inventory, 1)]
    manifest = {"runtime_version": VERSION, "created_at": now(), "tool_versions": tool_versions(), "source_directory": str(source.resolve()),
                "documents": records, "lock_sha256": file_hash(lock_path),
                "framework_files": [{"path": p, "sha256": h} for p, h in sorted(expected.items())], **metadata}
    check_schema(manifest, manifest_contract())
    if metadata["mode"] == "investigation" and not all(str(metadata[k]).strip() for k in
            ("investigation_mandate_ref", "supervising_role")):
        raise ValueError("Explicit investigative mandate and supervising role required")
    destination.mkdir(parents=True)
    (destination / "originals").mkdir()
    (destination / "derived").mkdir()
    for path, record in zip(inventory, records):
        copied = within(destination, record["path"])
        shutil.copyfile(path, copied)
        if file_hash(copied) != record["sha256"] or file_hash(path) != record["sha256"]:
            raise ValueError("Source changed during acquisition; incomplete packet retained")
    for relative in expected:
        target = within(destination / "frameworks", relative)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(within(frameworks, relative), target)
    shutil.copyfile(lock_path, destination / "te_frameworks.lock.json")
    if file_hash(destination / "te_frameworks.lock.json") != manifest["lock_sha256"]:
        raise ValueError("Lock changed during preparation")
    verify_frameworks(destination / "frameworks", lock)
    if source_inventory(source) != inventory or any(file_hash(path) != record["sha256"] for path, record in zip(inventory, records)):
        raise ValueError("Source inventory/content changed during acquisition; incomplete packet retained")
    # Completion marker is written only after successful copies and checks.
    write_new(destination / "manifest.json", manifest)
    write_new(destination / "case.json", blank_case(manifest, file_hash(destination / "manifest.json")))
    return destination


def indexed(records):
    result = {item["id"]: item for item in records}
    if len(result) != len(records):
        raise ValueError("Duplicate record ID")
    return result


def review_template(run):
    run = Path(run)
    return {"case_sha256": file_hash(run / "case.json"), "manifest_sha256": file_hash(run / "manifest.json"),
        "reviewer": "", "reviewer_role": "", "decision": "pending", "rationale": "", "reviewed_at": None,
        "checks": {name: "pending" for name in ("coverage", "anchors_and_interpretation", "source_independence",
                                                "alternatives", "bounded_conclusions")},
        "legal_use": "not_authorized_by_runtime"}


def validate(run, review_path=None):
    run = Path(run)
    manifest = load_json(run / "manifest.json")
    data = load_json(run / "case.json")
    check_schema(manifest, manifest_contract())
    check_schema(data, contract())
    if manifest["tool_versions"] != tool_versions():
        raise ValueError("Recorded Python/jsonschema environment differs; reproduce it or prepare a reviewed new run")
    if data["manifest_sha256"] != file_hash(run / "manifest.json") or data["case_id"] != manifest["case_id"]:
        raise ValueError("Case/manifest binding changed")
    if manifest["mode"] == "investigation" and not (manifest["investigation_mandate_ref"].strip() and manifest["supervising_role"].strip()):
        raise ValueError("Missing investigative mandate/role")
    if file_hash(run / "te_frameworks.lock.json") != manifest["lock_sha256"]:
        raise ValueError("Frozen lock changed")
    expected = verify_frameworks(run / "frameworks", load_json(run / "te_frameworks.lock.json"))
    if len({i["path"] for i in manifest["framework_files"]}) != len(manifest["framework_files"]) or {
            i["path"]: i["sha256"] for i in manifest["framework_files"]} != expected:
        raise ValueError("Framework inventory differs from lock")
    docs = indexed(manifest["documents"])
    states = indexed(data["documents"])
    if docs.keys() != states.keys():
        raise ValueError("Coverage inventory missing or adds documents")
    if len({d["path"] for d in docs.values()}) != len(docs):
        raise ValueError("Two acquired objects share a storage path")
    original_paths = {p.relative_to(run).as_posix() for p in (run / "originals").rglob("*") if p.is_file()}
    if original_paths != {d["path"] for d in docs.values()}:
        raise ValueError("Original directory inventory differs from manifest")
    hash_groups = {}
    for doc_id, doc in docs.items():
        if not doc["path"].startswith("originals/"):
            raise ValueError("Original path outside originals")
        path = within(run, doc["path"])
        if file_hash(path) != doc["sha256"] or path.stat().st_size != doc["size"]:
            raise ValueError(f"Original changed: {doc_id}")
        state = states[doc_id]
        previous = hash_groups.setdefault(doc["sha256"], state["source_group"])
        if previous != state["source_group"]:
            raise ValueError("Identical bytes cannot count as independent source groups")
        if data["wave1_complete"] and state["reading"] == "pending":
            raise ValueError("Wave 1 incomplete")
        if state["reading"] != "pending" and not (state["reading_note"].strip() and state["reviewer"].strip()):
            raise ValueError("Reading or limitation needs reviewer and rationale")
        if not data["wave1_complete"] and state["relevance"] != "deferred":
            raise ValueError("Relevance judgment before first-wave boundary")
        if state["relevance"] != "deferred" and not state["relevance_reason"].strip():
            raise ValueError("Relevance rationale missing")
        if state["relevance"] == "exclude_provisional" and state["reading"] != "read":
            raise ValueError("Unread/restricted material cannot be irrelevant")
        if data["audit"]["complete"] and state["relevance"] == "exclude_provisional" and not state["exclusion_recheck"].strip():
            raise ValueError("Audit must reconsider exclusions")
    derivatives = indexed(data["derivatives"])
    if len({d["path"] for d in derivatives.values()}) != len(derivatives):
        raise ValueError("Duplicate derivative path")
    for derivative in derivatives.values():
        if derivative["document_id"] not in docs or not derivative["path"].startswith("derived/"):
            raise ValueError("Invalid derivative parent/path")
        if file_hash(within(run, derivative["path"])) != derivative["sha256"]:
            raise ValueError("Derivative changed")
    evidence = indexed(data["evidence"])
    for item in evidence.values():
        if item["document_id"] not in docs:
            raise ValueError("Unknown evidence document")
        doc = docs[item["document_id"]]
        if item["derivative_id"] is not None:
            doc = derivatives.get(item["derivative_id"])
            if not doc or doc["document_id"] != item["document_id"]:
                raise ValueError("Evidence derivative parent mismatch")
        text = within(run, doc["path"]).read_text(encoding="utf-8-sig")
        if item["quote"] not in text:
            raise ValueError(f"Quotation not found: {item['id']}")
    def refs(values, target=evidence):
        if any(value not in target for value in values):
            raise ValueError("Unresolved evidence/record reference")
    def confidence(value, supports):
        if supports and int(value[1]) < max(int(evidence[x]["confidence"][1]) for x in supports):
            raise ValueError("Confidence inflated beyond supporting premise")
    legal = indexed(data["legal_references"])
    indexed(data["gaps"])
    findings = indexed(data["audit"]["findings"])
    for finding in findings.values():
        supports = finding["supporting_evidence"]
        refs(supports)
        refs(finding["opposing_evidence"])
        refs(finding["criterion"]["evidence_ids"])
        refs(finding["criterion"]["legal_reference_ids"], legal)
        if not supports:
            raise ValueError("Finding requires documentary support; use a gap or hypothesis instead")
        if finding["criterion"]["kind"] in ("policy", "contract") and not finding["criterion"]["evidence_ids"]:
            raise ValueError("Contract/policy criterion needs an anchor")
        if finding["criterion"]["kind"] == "legal_question" and not finding["criterion"]["legal_reference_ids"]:
            raise ValueError("Legal question requires a reference, not an assumed rule")
        confidence(finding["confidence"], supports)
        if finding["confidence"] == "S1" and len({states[evidence[x]["document_id"]]["source_group"] for x in supports}) < 2:
            raise ValueError("Triangulation requires at least two declared origin groups")
        for alt in finding["alternatives"]:
            refs(alt["evidence_ids"])
            if alt["outcome"] in ("supported", "refuted") and not alt["evidence_ids"]:
                raise ValueError("Resolved alternative needs evidence")
    checks = indexed(data["audit"]["checks"])
    required = set(AUDIT_AREAS if manifest["mode"] == "audit" else INVESTIGATION_AREAS)
    counts = Counter(check["area"] for check in checks.values())
    if any(counts[area] != 1 for area in required):
        raise ValueError("Mandatory audit/check area missing or duplicated")
    for check in checks.values():
        refs(check["evidence_ids"])
        refs(check["finding_ids"], findings)
        if check["status"] != "pending" and not all(check[x].strip() for x in ("procedure", "population_and_scope", "result_note")):
            raise ValueError("Check requires procedure, scope and result rationale")
        expected_results = {"pending": {"pending"}, "tested": {"no_exception", "exception", "inconclusive"},
                            "not_testable": {"inconclusive"}, "not_applicable": {"not_applicable"}}
        if check["result"] not in expected_results[check["status"]]:
            raise ValueError("Check status/result mismatch")
        if check["status"] == "tested" and not check["evidence_ids"]:
            raise ValueError("A performed test needs evidence")
        if check["result"] == "exception" and not check["finding_ids"]:
            raise ValueError("Exception must reference a finding")
        if data["audit"]["complete"] and check["status"] == "pending":
            raise ValueError("Mandatory audit pass incomplete")
    if data["analysis"]["complete"] and (not data["wave1_complete"] or not data["analysis"]["summary"].strip()
            or any(d["relevance"] == "deferred" for d in states.values())):
        raise ValueError("Analysis completion requires first-wave and relevance gates")
    if data["audit"]["complete"] and not data["analysis"]["complete"]:
        raise ValueError("Audit cannot close before analysis")
    hypotheses = indexed(data["hypotheses"])
    for hypothesis in hypotheses.values():
        refs(hypothesis["supporting_evidence"])
        refs(hypothesis["opposing_evidence"])
        if hypothesis["status"] == "supported" and not hypothesis["supporting_evidence"]:
            raise ValueError("Supported hypothesis needs evidence")
        if hypothesis["status"] == "disfavored" and not hypothesis["opposing_evidence"]:
            raise ValueError("Disfavored hypothesis needs contrary evidence")
    if manifest["mode"] == "investigation" and data["audit"]["complete"]:
        if len(hypotheses) < 2 or not any(h["kind"] in ("non_criminal", "exculpatory") for h in hypotheses.values()):
            raise ValueError("Investigation requires competing and non-criminal/exculpatory hypotheses")
    for records in (data["chronology"], data["relationships"]):
        for item in indexed(records).values():
            refs(item["evidence_ids"])
            if not item["evidence_ids"]:
                raise ValueError("Chronology/relationship needs anchors")
            confidence(item["confidence"], item["evidence_ids"])
    review_status = "not_recorded"
    if review_path:
        review = load_json(review_path)
        check_schema(review, review_contract())
        if review["case_sha256"] != file_hash(run / "case.json") or review["manifest_sha256"] != file_hash(run / "manifest.json"):
            raise ValueError("Review invalidated by changed case/manifest")
        if review["decision"] != "pending":
            if not all(str(review[k] or "").strip() for k in ("reviewer", "reviewer_role", "rationale", "reviewed_at")):
                raise ValueError("Completed review needs identity, role, date and rationale")
            if review["reviewer"].strip().casefold() == manifest["analyst"].strip().casefold():
                raise ValueError("Reviewer must be declared distinct from analyst")
        if review["decision"] == "accept" and (not data["audit"]["complete"] or any(v != "accept" for v in review["checks"].values())):
            raise ValueError("Acceptance requires completed pass and all review checks")
        review_status = "accept_recorded_identity_unverified" if review["decision"] == "accept" else review["decision"]
    partial = any(d["reading"] != "read" for d in states.values()) or any(
        c["status"] in ("pending", "not_testable") or c["result"] == "inconclusive" for c in checks.values()) or bool(data["analysis"]["limitations"]) or any(
        gap["status"] != "resolved" for gap in data["gaps"])
    if not data["wave1_complete"]:
        phase = "wave1"
    elif not data["analysis"]["complete"]:
        phase = "relevance_and_analysis"
    elif not data["audit"]["complete"]:
        phase = "audit_required"
    elif review_status == "accept_recorded_identity_unverified":
        phase = "documentary_pass_review_recorded"
    else:
        phase = "independent_review_required"
    return {"technical_status": "TECHNICALLY_CHECKED", "phase": phase,
        "coverage": "limited_or_pending" if partial else "declared_accessible_pass_only",
        "document_count": len(docs), "finding_count": len(findings), "review": review_status,
        "case_sha256": file_hash(run / "case.json"), "manifest_sha256": file_hash(run / "manifest.json"),
        "empirical_performance": "not_assessed", "legal_use": "not_authorized_by_runtime",
        "limits": ["Checks validate declared records, not truth, actual reading, independent origin or lawful authority.",
                   "No immutable custody log, trusted timestamp, encryption or access control is implemented.",
                   "No automated OCR, fraud detection, professional opinion or absence-of-wrongdoing verdict."]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    prep = commands.add_parser("prepare")
    for name in ("source-dir", "run-dir", "framework-root", "lock"):
        prep.add_argument("--" + name, type=Path, required=True)
    for name in ("case-id", "purpose", "scope", "owner", "analyst", "acquisition-authority-ref", "jurisdiction"):
        prep.add_argument("--" + name, required=True)
    prep.add_argument("--mode", choices=["audit", "investigation"], required=True)
    prep.add_argument("--investigation-mandate-ref", default="")
    prep.add_argument("--supervising-role", default="")
    prep.add_argument("--synthetic", action="store_true")
    for command in ("validate", "review-request"):
        p = commands.add_parser(command)
        p.add_argument("--run-dir", type=Path, required=True)
        if command == "validate":
            p.add_argument("--review", type=Path)
    args = vars(parser.parse_args())
    command = args.pop("command")
    try:
        if command == "prepare":
            source, dest, frameworks, lock = (args.pop(k) for k in ("source_dir", "run_dir", "framework_root", "lock"))
            result = {"prepared": str(prepare(source, dest, frameworks, lock, **args)), "analysis": "not_started"}
        elif command == "review-request":
            validate(args["run_dir"])
            target = args["run_dir"] / "review_request.json"
            write_new(target, review_template(args["run_dir"]))
            result = {"review_request": str(target), "status": "pending"}
        else:
            result = validate(args["run_dir"], args["review"])
        print(json.dumps(result, ensure_ascii=False, indent=2))
    except (OSError, ValueError, KeyError, TypeError) as exc:
        parser.exit(1, f"Casework blocked: {exc}\n")


if __name__ == "__main__":
    main()
