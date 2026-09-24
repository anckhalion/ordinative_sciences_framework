"""Prepare a local run packet: freeze the source, the dependencies and the methodology, and write the empty output draft."""
import argparse
import json
import shutil
import uuid
from pathlib import Path

from validate_lexx_output import ROOT, dependency_ledger, sha256_bytes

# The methodology documents frozen with every run, each under the names its edition
# carries: the canonical corpus and the public repository ship the same runtime with the
# documentation composed in different languages. Every edition present is frozen.
PACKAGE_DOCUMENTS = (
    ("README.md",),
    ("00_FONDAMENTA.md", "00_FOUNDATIONS.md"),
    ("TE_MODULE_LEXX_v0_1.md", "TE_MODULE_LEXX_v0_1_EN.md"),
    ("03_PRE_PILOT_PROTOCOL.md",),
    ("release.json",),
)


def package_documents(folder):
    """Return the methodology documents present in ``folder``, one group per PACKAGE_DOCUMENTS entry."""
    found = []
    for candidates in PACKAGE_DOCUMENTS:
        present = [folder / name for name in candidates if (folder / name).is_file()]
        if not present:
            raise FileNotFoundError(f"Package document required in {folder}: one of {', '.join(candidates)}")
        found.extend(present)
    return found


def template(source_hash, ledger, run_id=None):
    limit = "To be examined."
    return {
        "accordo": "To be identified", "versione_modulo": "LEXX v0.2-alpha.3",
        "methodology_version": "0.1", "run_id": run_id or str(uuid.uuid4()),
        "source_sha256": source_hash, "prospettiva": "neutra", "modalita": "diagnostica",
        "run_states": ["LLM_ONLY_UNVERIFIED", "DOCUMENT_ONLY"], "dependency_ledger": ledger,
        "jurisdiction_gate": {"jurisdiction": None, "choice_of_law": None, "document_type": "to be identified",
                              "sources_as_of_date": None, "external_sources_verified": False,
                              "limits": ["Documentary analysis of the supplied text."]},
        "insed": {"stato": "to be ascertained", "qualificazione_parti": "UNKNOWN", "perimetro_analisi": "documento_solo",
                  "limiti": [limit], "copertura": {"stato": "non_eseguita",
                  "clausole_totali": ["DOCUMENT_TO_BE_SEGMENTED"],
                  "clausole_non_esaminate": ["DOCUMENT_TO_BE_SEGMENTED"], "nota_limite": limit}},
        "strip": [], "campo_relazionale_R": [],
        "phi_accordo": {"dichiarata": "", "effettiva": "", "delta": "", "confidence": "S3"},
        "consistenza": {"aritmetica": [], "nota_aritmetica": limit, "temporale": [], "nota_temporale": limit},
        "falle": [],
        "vettore_intenzione": {"semantic_scope": "vettore_strutturalmente_abilitato_non_intenzione_soggettiva",
                               "dichiarato": "", "effettivo": "", "delta_vettore": "", "tomografia": [],
                               "lens": "", "confidence": "S3", "nota_limite": limit},
        "proporzione": {"mode": "qualitative", "band": "vuoto", "criterion": limit, "classe_equita": "non_valutabile"},
        "lyapunov_globale": {"mode": "qualitative", "lambda_segno": "vuoto", "argomento": limit},
        "non_falle_verificate": [], "note_negoziali": [], "verdetto_generale": "non_valutabile",
        "verdetti": {"testo": {"esito": "non_valutabile", "motivazione": limit, "confidence": "S3"},
                     "sistema": {"esito": "non_valutabile", "nota_limite": "System verdict follows external sources and legal review."}},
        "tre_mappe": {"cosa_dice": "", "cosa_non_dice": "", "cosa_dice_senza_dirlo": ""},
        "meta_pai": {"bias_rilevati": [], "note_trasparenza": limit,
                     "phi_test": {"funzione_attesa": "Examine the agreement and give reasons for the findings.",
                                  "riscontro": limit, "limiti_residui": [limit]}},
        "verification": {"executor": "llm_only", "anchors": "unverified", "schema": "unverified", "round_trip": "unverified"},
    }


def prepare(source, frameworks, destination):
    source, frameworks, destination = Path(source), Path(frameworks), Path(destination)
    raw = source.read_bytes()
    text = raw.decode("utf-8-sig")
    if not text.strip():
        raise ValueError("Empty source")
    ledger = dependency_ledger(frameworks)
    if destination.exists():
        raise ValueError("Run directory already exists; each attempt takes a new one")
    destination.mkdir(parents=True)
    (destination / "source.txt").write_bytes(raw)
    copied = destination / "frameworks"
    copied.mkdir()
    for item in ledger:
        shutil.copy2(frameworks / item["source_file"], copied / item["source_file"])
    # Freeze the methodology and executable contract alongside the actual dependencies.
    lexx = ROOT.parent
    package_files = package_documents(lexx)
    package_files += [path for path in ROOT.rglob("*") if path.is_file()
                      and "__pycache__" not in path.parts and path.suffix not in {".pyc", ".pyo"}]
    for path in package_files:
        target = copied / "LEXX" / path.relative_to(lexx)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, target)
    data = template(sha256_bytes(raw), ledger)
    (destination / "output_draft.json").write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    manifest = {"run_id": data["run_id"], "source_sha256": data["source_sha256"],
                "original_source": str(source.resolve()), "runtime_version": "0.2.0-alpha.3",
                "frozen_files": {path.relative_to(destination).as_posix(): sha256_bytes(path.read_bytes())
                                 for path in copied.rglob("*") if path.is_file()},
                "limits": ["output_draft.json is the template the executor fills."]}
    (destination / "run_manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    return destination


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", required=True, type=Path)
    parser.add_argument("--framework-root", required=True, type=Path)
    parser.add_argument("--run-dir", required=True, type=Path)
    args = parser.parse_args()
    try:
        print(prepare(args.source, args.framework_root, args.run_dir))
    except (OSError, ValueError) as exc:
        parser.exit(1, f"Run preparation failed: {exc}\n")
