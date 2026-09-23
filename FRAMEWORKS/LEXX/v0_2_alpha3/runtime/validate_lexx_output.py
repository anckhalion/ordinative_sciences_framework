"""External technical verification; never an empirical or legal certification."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import unicodedata
from datetime import datetime, timezone
from decimal import Decimal, localcontext
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VERSION = "0.2.0-alpha.3"
EMPTY_METRICS = {"anchors_checked": 0, "literal_quotes": 0, "structural_absences": 0}


def sha256_bytes(value):
    return hashlib.sha256(value).hexdigest()


def normalize_text(value):
    # Case and compatibility characters are significant. Normalize only NFC/whitespace.
    return re.sub(r"\s+", " ", unicodedata.normalize("NFC", value)).strip()


def reject_constant(value):
    raise ValueError(f"Non-finite JSON number: {value}")


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"Duplicate JSON key: {key}")
        result[key] = value
    return result


def load_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8-sig"),
                      parse_constant=reject_constant, object_pairs_hook=unique_object)


def add(errors, code, path, message):
    errors.append({"code": code, "path": path, "message": message})


def dependency_ledger(framework_root, profile_path=None):
    """Read, hash and pin actual files; availability is not proof of LLM comprehension."""
    profile = load_json(profile_path or ROOT / "compatibility.json")
    root = Path(framework_root).resolve()
    entries = []
    for item in profile["dependencies"]:
        path = (root / item["file"]).resolve()
        if not path.is_relative_to(root):
            raise ValueError("Dependency path escapes framework root")
        raw = path.read_bytes()
        actual = sha256_bytes(raw)
        if actual != item["sha256"]:
            raise ValueError(f"Dependency hash changed: {item['component']}; compatibility review required")
        entries.append({"component": item["component"], "version": item["version"],
                        "status": "available_verified", "source_file": item["file"], "sha256": actual})
    return entries


def evidence_entries(node, path="$"):
    if isinstance(node, dict):
        if "anchor_type" in node:
            yield path, node
        else:
            for key, value in node.items():
                yield from evidence_entries(value, f"{path}.{key}")
    elif isinstance(node, list):
        for index, value in enumerate(node):
            yield from evidence_entries(value, f"{path}[{index}]")


def check_evidence(data, source, errors):
    metrics = dict(EMPTY_METRICS)
    normalized = normalize_text(source)
    for path, entry in evidence_entries(data):
        metrics["anchors_checked"] += 1
        if entry["anchor_type"] == "literal_quote":
            metrics["literal_quotes"] += 1
            if normalize_text(entry["quote"]) not in normalized:
                add(errors, "ANCHOR_NOT_FOUND", path, "Quote not found; case is significant.")
        else:
            metrics["structural_absences"] += 1
            before = normalize_text(entry["context_before"])
            after = normalize_text(entry["context_after"])
            start = normalized.find(before)
            end = normalized.find(after, start + len(before)) if start >= 0 else -1
            if start < 0 or end < 0:
                add(errors, "ABSENCE_CONTEXT_ORDER", path, "Context anchors must exist in the stated order without overlap.")
    return metrics


def check_semantics(data, errors):
    states = set(data["run_states"])
    if not {"DOCUMENT_ONLY", "LLM_ONLY_UNVERIFIED"}.issubset(states):
        add(errors, "REQUIRED_STATES", "$.run_states", "Input must declare DOCUMENT_ONLY and LLM_ONLY_UNVERIFIED.")
    if states & {"INCOMPATIBLE_STOP", "INVALID_OUTPUT"}:
        add(errors, "STOP_STATE", "$.run_states", "A stopped or invalid analysis cannot pass technical verification.")
    strip = data["strip"]
    ids = [entry["clausola"] for entry in strip]
    if len(ids) != len(set(ids)):
        add(errors, "CLAUSE_DUPLICATE", "$.strip", "Clause IDs must be unique.")
    by_id = {item["clausola"]: item for item in strip}
    cover = data["insed"]["copertura"]
    inventory = set(cover["clausole_totali"])
    excluded = set(cover["clausole_non_esaminate"])
    examined = set(ids)
    if examined & excluded or examined | excluded != inventory:
        add(errors, "COVERAGE_PARTITION", "$.insed.copertura", "Examined and excluded clauses must partition the declared inventory.")
    if cover["stato"] == "completa" and (excluded or not examined):
        add(errors, "COVERAGE_COMPLETE", "$.insed.copertura", "Complete coverage cannot exclude clauses or be empty.")
    if cover["stato"] == "non_eseguita" and examined:
        add(errors, "COVERAGE_STATE", "$.insed.copertura", "Non-executed coverage conflicts with STRIP entries.")
    if cover["stato"] != "completa" and data["verdetto_generale"] in {"accordo_solido", "fortezza_valida"}:
        add(errors, "PARTIAL_POSITIVE_VERDICT", "$.verdetto_generale", "Partial analysis cannot certify absence of flaws in the whole agreement.")
    if data["verdetto_generale"] != data["verdetti"]["testo"]["esito"]:
        add(errors, "VERDICT_MISMATCH", "$.verdetti", "Text verdict must match the general verdict.")
    if not examined and data["verdetto_generale"] != "non_valutabile":
        add(errors, "EMPTY_ANALYSIS", "$.strip", "An empty analysis must remain non_valutabile.")

    def known(values, path):
        for value in values:
            if value not in examined:
                add(errors, "UNKNOWN_CLAUSE", path, f"Unknown/unexamined clause: {value}")

    for index, relation in enumerate(data["campo_relazionale_R"]):
        known(relation["clausole_in_intersezione"], f"$.campo_relazionale_R[{index}]")
    for collection in ("non_falle_verificate", "note_negoziali"):
        for index, item in enumerate(data[collection]):
            known([item["clausola"]], f"$.{collection}[{index}]")
    vector = data["vettore_intenzione"]
    tomography_ids = [item["clausola"] for item in vector["tomografia"]]
    known(tomography_ids, "$.vettore_intenzione.tomografia")
    if len(tomography_ids) != len(set(tomography_ids)):
        add(errors, "TOMOGRAPHY_DUPLICATE", "$.vettore_intenzione", "Repeating one clause is not independent convergence.")
    for item in vector["tomografia"]:
        clause = by_id.get(item["clausola"])
        if clause and item["payload"] not in clause["payload"]:
            add(errors, "TOMOGRAPHY_PAYLOAD", "$.vettore_intenzione.tomografia", "Tomographic payload must be present in the referenced STRIP.")
        if item["direzione"] != vector["effettivo"]:
            add(errors, "TOMOGRAPHY_DIRECTION", "$.vettore_intenzione.tomografia", "Convergence must name the same structural vector.")
    if vector["confidence"] == "S1" and (len(set(tomography_ids)) < 3 or not vector["effettivo"].strip()):
        add(errors, "S1_CONVERGENCE", "$.vettore_intenzione", "S1 requires at least three distinct anchored clauses converging on a nonempty vector.")

    flaw_ids = [item["id"] for item in data["falle"]]
    if len(flaw_ids) != len(set(flaw_ids)):
        add(errors, "FLAW_DUPLICATE", "$.falle", "Flaw IDs must be unique.")
    for index, flaw in enumerate(data["falle"]):
        path = f"$.falle[{index}]"
        known(flaw["clausole"], path)
        if flaw["vettore_primario"] == "V-IN" and len(flaw["clausole"]) < 2:
            add(errors, "INTERSECTION_ARITY", path, "An intersection flaw requires at least two clauses.")
        if flaw["test_contrario"]["esito"] == "declassata" and flaw["confidence"] in {"S0", "S1"}:
            add(errors, "DOWNGRADED_CONFIDENCE", path, "A downgraded hypothesis must be S2/S3.")
        if flaw["classe_oct"] == "D":
            add(errors, "LEGAL_CLASS_UNVERIFIED", path, "In DOCUMENT_ONLY, legal invalidity cannot be established; use non_valutabile with a reason.")
        proposal = flaw["controproposta"]
        if (proposal["status"] == "not_proposed" and data["prospettiva"] != "neutra"
                and flaw["test_contrario"]["esito"] != "scartata"):
            add(errors, "COUNTERPROPOSAL_REQUIRED", path, "Non-neutral retained flaws require a counterproposal.")
        if proposal["status"] == "proposed":
            invariants = {by_id[c]["iota"] for c in flaw["clausole"] if c in by_id}
            if proposal["iota_originale"] not in invariants:
                add(errors, "ORIGINAL_INVARIANT", path, "Original invariant must come from a referenced clause.")
            if proposal["ri_strip"]["payload_primo"] or proposal["lambda_post"] != "neg":
                add(errors, "COUNTERPROPOSAL_UNRESOLVED", path, "Residual payload or unstabilized trajectory requires a new draft before acceptance.")

    retained = [f for f in data["falle"] if f["test_contrario"]["esito"] != "scartata"]
    if retained and data["verdetto_generale"] in {"accordo_solido", "fortezza_valida"}:
        add(errors, "POSITIVE_WITH_FLAWS", "$.verdetto_generale", "A positive verdict conflicts with retained flaws.")
    if not retained and data["verdetto_generale"] in {"falle_puntuali", "falle_strutturali", "device", "degenerato"}:
        add(errors, "NEGATIVE_WITHOUT_FLAWS", "$.verdetto_generale", "An adverse verdict requires retained findings.")
    grades = [data["phi_accordo"]["confidence"]] + [f["confidence"] for f in retained]
    if vector["effettivo"].strip():
        grades.append(vector["confidence"])
    worst = max(int(value[1]) for value in grades)
    if int(data["verdetti"]["testo"]["confidence"][1]) < worst:
        add(errors, "CONFIDENCE_INFLATION", "$.verdetti.testo.confidence", "Verdict cannot exceed the weakest contributing confidence.")

    for index, check in enumerate(data["consistenza"]["aritmetica"]):
        with localcontext() as context:
            context.prec = 2000
            values = [Decimal(value) for value in check["operandi"]]
            if check["operazione"] == "sum":
                result = sum(values)
            elif check["operazione"] == "product":
                result = Decimal(1)
                for value in values:
                    result *= value
            elif len(values) == 2:
                result = values[0] * values[1] / 100
            else:
                add(errors, "ARITHMETIC_ARITY", f"$.consistenza.aritmetica[{index}]", "Percentage expects base and percent.")
                continue
            expected = "coerente" if result == Decimal(check["risultato_dichiarato"]) else "incoerente"
            if check["esito"] != expected:
                add(errors, "ARITHMETIC_RESULT", f"$.consistenza.aritmetica[{index}]", f"Recomputed {result}; expected {expected}.")


def check_review(data, source_hash, output_hash, review, errors):
    """Bind a separately supplied review to exact bytes; do not certify independence."""
    proposals = {f["id"]: f["controproposta"] for f in data["falle"]
                 if f["controproposta"]["status"] == "proposed"}
    if not proposals:
        return "not_applicable"
    if review is None:
        return "pending_independent_review"
    initial_errors = len(errors)
    if not isinstance(review, dict):
        add(errors, "REVIEW_FORMAT", "review", "Expected a separate review object.")
        return "rejected"
    for key, expected in (("source_sha256", source_hash), ("output_sha256", output_hash)):
        if review.get(key) != expected:
            add(errors, "REVIEW_BINDING", f"review.{key}", "Review belongs to different source/output bytes.")
    if (not isinstance(review.get("reviewer_id"), str) or not review["reviewer_id"].strip()
            or not isinstance(review.get("review_run_id"), str) or not review["review_run_id"].strip()
            or review.get("review_run_id") == data["run_id"] or review.get("independent_declared") is not True):
        add(errors, "REVIEW_INDEPENDENCE", "review", "A distinct identified review session and independence declaration are required.")
    items = review.get("items")
    if not isinstance(items, list) or any(not isinstance(item, dict) for item in items):
        add(errors, "REVIEW_FORMAT", "review.items", "Expected an array of review items.")
        return "rejected"
    reviewed = [item.get("flaw_id") for item in items]
    if any(not isinstance(value, str) for value in reviewed) or sorted(reviewed) != sorted(proposals):
        add(errors, "REVIEW_COVERAGE", "review.items", "Every proposed counterproposal must be reviewed exactly once.")
    all_pass = True
    for item in items:
        flaw_id = item.get("flaw_id")
        if not isinstance(flaw_id, str) or flaw_id not in proposals:
            continue
        proposal = proposals[flaw_id]
        if item.get("proposal_sha256") != sha256_bytes(proposal["forma_equa"].encode("utf-8")):
            add(errors, "REVIEW_BINDING", "review.items", "Counterproposal changed after review.")
        strip = item.get("independent_restrip")
        if (not isinstance(strip, dict) or not isinstance(strip.get("iota_primo"), str)
                or not strip["iota_primo"].strip() or not isinstance(strip.get("payload_primo"), list)
                or any(not isinstance(p, str) or not p.strip() for p in strip.get("payload_primo", []))
                or not isinstance(item.get("reason"), str) or not item["reason"].strip()
                or not isinstance(item.get("invariant_preserved"), bool)
                or item.get("lambda_post") not in {"neg", "pos", "vuoto"}):
            add(errors, "REVIEW_RESTRIP", "review.items", "Independent re-strip, reasoning and decision are required.")
            all_pass = False
        elif not item["invariant_preserved"] or strip["payload_primo"] or item["lambda_post"] != "neg":
            all_pass = False
    if not all_pass:
        add(errors, "ROUND_TRIP_FAILED", "review", "Reviewer did not confirm preservation, empty payload and stabilizing trajectory.")
    return "recorded_pass" if all_pass and len(errors) == initial_errors else "recorded_fail"


def check_run_manifest(manifest_path, source_hash, run_id, errors):
    manifest_path = Path(manifest_path)
    manifest = load_json(manifest_path)
    if manifest.get("source_sha256") != source_hash or manifest.get("run_id") != run_id:
        add(errors, "RUN_BINDING", "run_manifest", "Run ID/source hash do not match the frozen packet.")
    root = manifest_path.parent.resolve()
    files = manifest.get("frozen_files")
    if not isinstance(files, dict) or not files:
        raise ValueError("Frozen file inventory is missing")
    for relative, expected in files.items():
        path = (root / relative).resolve()
        if not path.is_relative_to(root):
            raise ValueError("Frozen path escapes the run directory")
        if sha256_bytes(path.read_bytes()) != expected:
            add(errors, "FROZEN_FILE_CHANGED", relative, "Frozen dependency or executable contract was modified.")


def validate(source_path, output_path, schema_path=None, framework_root=None, review_path=None, manifest_path=None):
    errors = []
    report = {"validator_version": VERSION, "checked_at_utc": datetime.now(timezone.utc).isoformat(),
              "valid": False, "technical_status": "INVALID_OUTPUT", "empirical_validation": False,
              "metrics": dict(EMPTY_METRICS), "errors": errors,
              "limits": ["Technical checks do not establish diagnostic correctness or legal validity.",
                         "Context anchors do not prove a semantic absence.",
                         "Dependency availability does not prove that an executor read or understood them.",
                         "Review identity and independence are recorded declarations, not authenticated facts."]}
    try:
        source_bytes = Path(source_path).read_bytes()
        source = source_bytes.decode("utf-8-sig")
        if not source.strip():
            raise ValueError("Empty source")
        output_bytes = Path(output_path).read_bytes()
        data = load_json(output_path)
        schema_path = Path(schema_path or ROOT / "schemas" / "lexx_output.schema.json")
        schema = load_json(schema_path)
        report.update(source_sha256=sha256_bytes(source_bytes), output_sha256=sha256_bytes(output_bytes),
                      schema_sha256=sha256_bytes(schema_path.read_bytes()))
        from jsonschema import Draft202012Validator, FormatChecker
        from referencing import Registry
        Draft202012Validator.check_schema(schema)
        validator = Draft202012Validator(schema, format_checker=FormatChecker(), registry=Registry())
        for failure in sorted(validator.iter_errors(data), key=lambda e: str(list(e.path))):
            path = "$" + "".join(f"[{key}]" if isinstance(key, int) else f".{key}" for key in failure.path)
            add(errors, "SCHEMA", path, failure.message)
        if errors:
            return report
        if data["source_sha256"] != report["source_sha256"]:
            add(errors, "SOURCE_HASH", "$.source_sha256", "Source changed or wrong document was supplied.")
        if manifest_path:
            check_run_manifest(manifest_path, report["source_sha256"], data["run_id"], errors)
            report["run_manifest_sha256"] = sha256_bytes(Path(manifest_path).read_bytes())
        if framework_root is None:
            add(errors, "DEPENDENCY_ROOT", "framework_root", "Explicit framework root is required.")
        else:
            expected = dependency_ledger(framework_root)
            actual = data["dependency_ledger"]
            if sorted(actual, key=lambda d: d["component"]) != sorted(expected, key=lambda d: d["component"]):
                add(errors, "DEPENDENCY_LEDGER", "$.dependency_ledger", "Ledger must exactly match independently hashed files and reviewed profile.")
            report["verified_dependencies"] = expected
        report["metrics"] = check_evidence(data, source, errors)
        check_semantics(data, errors)
        review = load_json(review_path) if review_path else None
        report["round_trip"] = check_review(data, report["source_sha256"], report["output_sha256"], review, errors)
        report["valid"] = not errors
        report["technical_status"] = "TECHNICALLY_CHECKED" if not errors else "INVALID_OUTPUT"
        report["analysis_status"] = "not_assessed" if data["verdetto_generale"] == "non_valutabile" else "document_only_unvalidated"
        report["ready_for_independent_review"] = not errors and data["verdetto_generale"] != "non_valutabile"
    except ImportError as exc:
        add(errors, "VALIDATOR_DEPENDENCY", "runtime", f"Install requirements.txt: {exc}")
    except Exception as exc:
        # Malformed inputs and unavailable files must return a failed report, not success or a traceback.
        add(errors, "INPUT_OR_CONFIGURATION", "runtime", f"{type(exc).__name__}: {exc}")
        report["valid"] = False
        report["technical_status"] = "INVALID_OUTPUT"
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--framework-root", required=True, type=Path)
    parser.add_argument("--review", type=Path)
    parser.add_argument("--run-manifest", type=Path)
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    inputs = [args.source, args.output, args.review, args.run_manifest]
    if args.report and any(p and args.report.resolve() == p.resolve() for p in inputs):
        parser.error("Report cannot overwrite an input file")
    result = validate(args.source, args.output, framework_root=args.framework_root, review_path=args.review,
                      manifest_path=args.run_manifest)
    rendered = json.dumps(result, ensure_ascii=False, indent=2)
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(rendered + "\n", encoding="utf-8")
    print(rendered)
    return 0 if result["valid"] else 1


if __name__ == "__main__":
    sys.exit(main())
