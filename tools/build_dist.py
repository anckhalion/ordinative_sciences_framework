#!/usr/bin/env python3
"""Build the derived distribution layer of the Ordinative Sciences Framework.

Inputs, canonical and never modified by this script:

  FRAMEWORKS/                          the published framework corpus (byte-exact)
  FRAMEWORKS/te_frameworks.lock.json   family versions and hashes: the authority for versions
  CITATION.cff                         release version and date
  tools/loading_set.json               loading order, roles, triggers, profiles, reference table

Outputs, derived and deterministic (committed, rebuilt after any change to the inputs):

  dist/catalog.json                    machine-readable catalog of the loading set
  dist/TE_LOADING_SET_FULL.md          the twelve active documents in loading order, one file
  dist/TE_LOADING_SET_MINIMAL.md       Bootloader + Protocols + Core + SVP
  dist/TE_LEXX_METHOD.md               LEXX method documents in reading order
  dist/TE_CASEWORK_METHOD.md           CASEWORK method documents in reading order
  dist/README.md                       what each file is and how to verify it
  dist/SHA256SUMS.txt                  hashes of the files above
  llms.txt                             index for LLM tools (llmstxt.org convention)

The documents inside the bundles are reproduced byte for byte between delimiter lines that
carry the document's SHA-256; the derived layer never restates the doctrine, it indexes it.

Usage:
  python3 tools/build_dist.py                 write the outputs
  python3 tools/build_dist.py --check         rebuild in memory, compare with the committed outputs
  python3 tools/build_dist.py --write-manifest  regenerate FRAMEWORKS/MANIFEST_SHA256.txt
  python3 tools/build_dist.py --zip [PATH]    also write the download package (not committed)
"""
import argparse
import hashlib
import json
import math
import re
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FRAMEWORKS = ROOT / "FRAMEWORKS"
DIST = ROOT / "dist"
CONFIG_PATH = ROOT / "tools" / "loading_set.json"
LOCK_PATH = FRAMEWORKS / "te_frameworks.lock.json"
MANIFEST_PATH = FRAMEWORKS / "MANIFEST_SHA256.txt"
CITATION_PATH = ROOT / "CITATION.cff"
LLMS_PATH = ROOT / "llms.txt"
EXCLUDED_DIR_NAMES = {"__pycache__", ".git", ".venv", "venv"}
CATALOG_FORMAT = "te_frameworks.catalog/1"
BYTES_PER_TOKEN = 4
TOKEN_NOTE = ("approx_tokens = ceil(bytes / 4). A rough estimate for context-window planning; "
              "real counts depend on the tokenizer and run higher for symbol-dense text.")
OPEN_MARK = "▶"
CLOSE_MARK = "◀"


# --------------------------------------------------------------------------- helpers

def sha256_of(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def approx_tokens(n_bytes: int) -> int:
    return math.ceil(n_bytes / BYTES_PER_TOKEN)


def fmt_int(n: int) -> str:
    return f"{n:,}"


def release_info() -> dict:
    text = CITATION_PATH.read_text(encoding="utf-8")
    version = re.search(r'^version:\s*"?([^"\n]+?)"?\s*$', text, re.M)
    date = re.search(r'^date-released:\s*"?([^"\n]+?)"?\s*$', text, re.M)
    if not version or not date:
        raise SystemExit("CITATION.cff: version or date-released not found")
    return {"version": version.group(1), "date": date.group(1)}


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def outline(text: str) -> list:
    """Markdown headings outside fenced code blocks, with their line numbers."""
    sections = []
    in_fence = False
    for number, line in enumerate(text.splitlines(), 1):
        stripped = line.strip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        match = re.match(r"^(#{1,6})\s+(.*\S)\s*$", line)
        if match:
            sections.append({"level": len(match.group(1)), "title": match.group(2).strip(), "line": number})
    return sections


def file_name_version(file_name: str):
    match = re.search(r"_v(\d+(?:_\d+)*)_EN\.md$", file_name)
    return match.group(1).replace("_", ".") if match else None


def framework_files():
    """Every file under FRAMEWORKS/ except the manifest itself and excluded directories."""
    records = []
    for path in sorted(FRAMEWORKS.rglob("*")):
        if not path.is_file():
            continue
        relative = path.relative_to(FRAMEWORKS)
        if any(part in EXCLUDED_DIR_NAMES for part in relative.parts):
            continue
        if relative.as_posix() == MANIFEST_PATH.name:
            continue
        records.append(relative.as_posix())
    records.sort(key=lambda item: item.encode("utf-8"))
    return records


def manifest_text() -> str:
    lines = []
    for relative in framework_files():
        lines.append(f"{sha256_of((FRAMEWORKS / relative).read_bytes())}  {relative}\n")
    return "".join(lines)


# --------------------------------------------------------------------------- records

def document_records(config: dict, lock: dict) -> list:
    records = []
    for order, entry in enumerate(config["documents"], 1):
        family = lock["families"].get(entry["id"])
        if family is None or "snapshot_path" not in family:
            raise SystemExit(f"{entry['id']}: not a single-file family in {LOCK_PATH.name}")
        file_name = family["snapshot_path"]
        path = FRAMEWORKS / file_name
        data = path.read_bytes()
        sha = sha256_of(data)
        if sha != family["sha256"]:
            raise SystemExit(f"{file_name}: SHA-256 differs from the lock; regenerate the lock first (make lock)")
        text = data.decode("utf-8")
        record = {
            "id": entry["id"],
            "title": entry["title"],
            "file": file_name,
            "path": f"FRAMEWORKS/{file_name}",
            "version": family["version"],
            "file_name_version": file_name_version(file_name),
            "load_order": order,
            "readme_order": entry["readme_order"],
            "tier": entry["tier"],
            "load_mode": entry["load_mode"],
            "when": entry["when"],
            "role": entry["role"],
            "prerequisites": entry.get("prerequisites", []),
            "triggers": entry.get("triggers", []),
            "sha256": sha,
            "bytes": len(data),
            "lines": text.count("\n"),
            "approx_tokens": approx_tokens(len(data)),
            "sections": outline(text),
        }
        if entry.get("version_note"):
            record["version_note"] = entry["version_note"]
        records.append(record)
    return records


def domain_records(config: dict, lock: dict) -> list:
    records = []
    for entry in config["domain_frameworks"]:
        base = FRAMEWORKS / entry["dir"]
        release = load_json(base / "release.json")
        family = lock["families"][entry["lock_family"]]
        docs = []
        for number, doc in enumerate(entry["documents"], 1):
            path = base / doc["file"]
            data = path.read_bytes()
            text = data.decode("utf-8")
            docs.append({
                "order": number,
                "file": doc["file"],
                "path": f"FRAMEWORKS/{entry['dir']}/{doc['file']}",
                "role": doc["role"],
                "sha256": sha256_of(data),
                "bytes": len(data),
                "lines": text.count("\n"),
                "approx_tokens": approx_tokens(len(data)),
                "sections": outline(text),
            })
        records.append({
            "id": entry["id"],
            "title": entry["title"],
            "summary": entry["summary"],
            "entry_point": f"FRAMEWORKS/{entry['dir']}/README.md",
            "bundle": f"dist/{entry['file']}",
            "method_version": release.get("methodology_version"),
            "runtime_version": release.get("runtime_version"),
            "release_date": release.get("release_date"),
            "status": release.get("status"),
            "empirical_runs_completed": release.get("empirical_runs_completed"),
            "runtime": {
                "directory": f"FRAMEWORKS/{entry['runtime_dir']}",
                "lock_family": entry["lock_family"],
                "version": family["version"],
                "package_digest": family["package_digest"],
                "files": [item["relative_path"] for item in family["files"]],
            },
            "machine_files": [f"FRAMEWORKS/{entry['dir']}/{name}" for name in entry["machine_files"]],
            "documents": docs,
        })
    return records


def archive_records() -> list:
    records = []
    archive = FRAMEWORKS / "ARCHIVE"
    for path in sorted(archive.glob("*")):
        if path.is_file():
            data = path.read_bytes()
            records.append({"file": path.name, "path": f"FRAMEWORKS/ARCHIVE/{path.name}",
                            "sha256": sha256_of(data), "bytes": len(data)})
    return records


def build_catalog(config: dict, lock: dict, release: dict) -> dict:
    documents = document_records(config, lock)
    by_id = {doc["id"]: doc for doc in documents}
    profiles = {}
    for key, profile in config["profiles"].items():
        docs = [by_id[doc_id] for doc_id in profile["documents"]]
        profiles[key] = {
            "title": profile["title"],
            "file": f"dist/{profile['file']}",
            "description": profile["description"],
            "documents": profile["documents"],
            "bytes": sum(doc["bytes"] for doc in docs),
            "approx_tokens": sum(doc["approx_tokens"] for doc in docs),
        }
    return {
        "catalog_format": CATALOG_FORMAT,
        "repository": config["repository_url"],
        "release": {"version": release["version"], "date": release["date"]},
        "sources": {
            "framework_root": "FRAMEWORKS",
            "manifest": "FRAMEWORKS/MANIFEST_SHA256.txt",
            "lock": "FRAMEWORKS/te_frameworks.lock.json",
            "loading_table": "FRAMEWORKS/README.md",
            "config": "tools/loading_set.json",
        },
        "token_estimate": TOKEN_NOTE,
        "loading_rules": [
            "Load the documents of a profile in load_order.",
            "Documents with load_mode 'always' are loaded at session start; 'gate' is applied before any analysis; 'foundation', 'on-demand' and 'on-demand-mandatory' documents are loaded when their triggers or the Router (TE_BOOTLOADER §6, TE_CORE §8) name them.",
            "Analysis sequence: SVP → domain framework (LEXX / LENS / VERI / SCIMS / CASEWORK) → OBSERVER when integration or trajectory is required → PPRO when control patterns are implicated → P-AI self-verification (always active).",
            "Read references to earlier editions and to moved sections through reference_resolution.",
        ],
        "profiles": profiles,
        "documents": documents,
        "domain_frameworks": domain_records(config, lock),
        "reference_resolution": config["reference_resolution"],
        "archive": archive_records(),
        "human_documentation": config["human_docs"],
    }


# --------------------------------------------------------------------------- bundles

def delimited(number: int, total: int, label: str, file_name: str, sha: str, role: str, data: bytes) -> str:
    body = data.decode("utf-8")
    if not body.endswith("\n"):
        body += "\n"
    return (
        "---\n\n"
        f"**{OPEN_MARK} TE DOCUMENT {number} of {total} — {label}** · file `{file_name}` · SHA-256 `{sha}` · {role}\n\n"
        "---\n\n"
        f"{body}\n"
        f"**{CLOSE_MARK} END OF TE DOCUMENT {number} of {total} — {label}**\n\n"
    )


def integrity_section() -> str:
    return (
        "## Integrity\n\n"
        f"Each document opens with a line `{OPEN_MARK} TE DOCUMENT i of n` that carries its SHA-256 and closes with "
        f"`{CLOSE_MARK} END OF TE DOCUMENT i of n`. Between the blank line that follows the opening block and the "
        "blank line that precedes the closing line, the text is the canonical file byte for byte, so the hash can be "
        "recomputed from this file or checked against `FRAMEWORKS/MANIFEST_SHA256.txt` "
        "(`cd FRAMEWORKS && shasum -a 256 -c MANIFEST_SHA256.txt`). The same hashes are pinned by the compatibility "
        "profiles of the LEXX and CASEWORK runtimes.\n"
    )


def resolution_table(config: dict) -> str:
    lines = ["| Cited as | Read as |", "|---|---|"]
    for item in config["reference_resolution"]:
        lines.append(f"| {item['cited']} | {item['read_as']} |")
    return "\n".join(lines) + "\n"


def render_loading_set(profile_key: str, config: dict, catalog: dict) -> str:
    profile = config["profiles"][profile_key]
    by_id = {doc["id"]: doc for doc in catalog["documents"]}
    docs = [by_id[doc_id] for doc_id in profile["documents"]]
    total = len(docs)
    release = catalog["release"]
    all_docs = catalog["documents"]
    svp_position = next(i for i, doc in enumerate(docs, 1) if doc["id"] == "TE_MODULE_SVP")

    out = [f"# {profile['title']}\n\n"]
    out.append(
        f"Ordinative Sciences Framework, release {release['version']} ({release['date']}). "
        f"Derived file: {total} framework documents of `FRAMEWORKS/` reproduced byte for byte, in loading order, in one file. "
        "Generated by `tools/build_dist.py` from the canonical files; to change anything, edit the canonical files and rebuild.\n\n"
    )
    out.append("## How to use this file\n\n")
    if profile_key == "full":
        out.append(
            "1. Give the whole file to the agent as system context or project knowledge. The documents appear in the order "
            "in which they are loaded (`FRAMEWORKS/README.md`, \"Active loading set\").\n"
            "2. Documents 1–3 (Bootloader, Protocols, Core) are always active. Document "
            f"{svp_position} (SVP) is the mandatory gate before any analysis. The others are loaded when the Router "
            "(document 1 §6, document 3 §8) names them; when this file is loaded whole they are all present and the Router "
            "selects which one applies.\n"
            "3. If the context window cannot hold this file, use `TE_LOADING_SET_MINIMAL.md` (documents 1, 2, 3 and SVP) and "
            "make the remaining documents available on demand (project files, retrieval or tool access); `catalog.json` "
            "lists each document with its triggers and section outline.\n"
            "4. The two domain frameworks with runtimes, LEXX (agreements) and CASEWORK (documentary audit and investigation), "
            "are not in this file. Their method documents are in `TE_LEXX_METHOD.md` and `TE_CASEWORK_METHOD.md`; both run on "
            "this loading set, after the SVP gate.\n\n"
        )
    else:
        others = [doc for doc in all_docs if doc["id"] not in profile["documents"]]
        out.append(
            "1. Give the whole file to the agent as system context or project knowledge. The documents appear in the order "
            "in which they are loaded (`FRAMEWORKS/README.md`, \"Minimal profile for a constrained context\": entries 1, 2, 3, 6).\n"
            "2. Documents 1–3 (Bootloader, Protocols, Core) are always active. Document 4 (SVP) is the mandatory gate before "
            "any analysis.\n"
            "3. The remaining documents of the full loading set are loaded on demand when the Router (document 1 §6, "
            "document 3 §8) names them. Make them available to the agent (project files, retrieval or tool access) or load "
            "`TE_LOADING_SET_FULL.md` instead. They are:\n\n"
        )
        out.append("| Document | Version | Load when | Canonical file |\n|---|---|---|---|\n")
        for doc in others:
            out.append(f"| {doc['id']} | {doc['version']} | {doc['when']} | `{doc['file']}` |\n")
        out.append(
            "\n4. The domain frameworks LEXX and CASEWORK (`TE_LEXX_METHOD.md`, `TE_CASEWORK_METHOD.md`) run on this "
            "loading set after the SVP gate and name the modules their stages require.\n\n"
        )
    out.append("## Documents in this file\n\n")
    out.append("| # | Document | Version | Load | Role | SHA-256 | ~Tokens |\n|---|---|---|---|---|---|---|\n")
    for number, doc in enumerate(docs, 1):
        out.append(
            f"| {number} | {doc['id']} (`{doc['file']}`) | {doc['version']} | {doc['load_mode']} | {doc['role']} | "
            f"`{doc['sha256'][:16]}…` | {fmt_int(doc['approx_tokens'])} |\n"
        )
    total_bytes = sum(doc["bytes"] for doc in docs)
    total_tokens = sum(doc["approx_tokens"] for doc in docs)
    out.append(f"\nTotal: {fmt_int(total_bytes)} bytes, about {fmt_int(total_tokens)} tokens ({TOKEN_NOTE})\n\n")
    out.append("## How the documents refer to one another\n\n")
    out.append(
        "The documents cite one another by family name and, in places, by the number of an earlier edition or of a "
        "section that has since moved. Read every such reference as pointing to the edition in this loading set:\n\n"
    )
    out.append(resolution_table(config))
    out.append("\n")
    out.append(integrity_section())
    out.append("\n")
    for number, doc in enumerate(docs, 1):
        data = (FRAMEWORKS / doc["file"]).read_bytes()
        out.append(delimited(number, total, f"{doc['id']} {doc['version']}", doc["file"], doc["sha256"], doc["role"], data))
    return "".join(out)


def render_domain_bundle(domain: dict, catalog: dict) -> str:
    release = catalog["release"]
    docs = domain["documents"]
    total = len(docs)
    out = [f"# {domain['title']}\n\n"]
    out.append(
        f"Ordinative Sciences Framework, release {release['version']} ({release['date']}). "
        f"Method {domain['method_version']}, runtime {domain['runtime_version']} "
        f"(status: `{domain['status']}`; empirical runs completed: {domain['empirical_runs_completed']}). "
        f"Derived file: the method documents of `{domain['entry_point'].rsplit('/', 1)[0]}/` reproduced byte for byte, "
        "in the reading order given by its README. Generated by `tools/build_dist.py`; edit the canonical files and rebuild.\n\n"
    )
    out.append(f"{domain['summary']}\n\n")
    out.append(
        "## How to use this file\n\n"
        "1. Load the TE loading set first (`TE_LOADING_SET_FULL.md`, or `TE_LOADING_SET_MINIMAL.md` plus the modules the "
        "stages name); apply the SVP gate; then load this file.\n"
        f"2. The runtime is not reproduced here: `{domain['runtime']['directory']}/` holds the code, schemas and tests "
        f"(lock family `{domain['runtime']['lock_family']}` {domain['runtime']['version']}, package digest "
        f"`{domain['runtime']['package_digest'][:16]}…`). The machine-readable profiles are "
        + ", ".join(f"`{path}`" for path in domain["machine_files"]) + ".\n"
        "3. The runtime performs the technical checks its compatibility profile lists; legal and investigative judgement "
        "stays with the professional who signs the report (README.md of the framework, status line).\n\n"
    )
    out.append("## Documents in this file\n\n| # | Document | Role | SHA-256 | ~Tokens |\n|---|---|---|---|---|\n")
    for doc in docs:
        out.append(f"| {doc['order']} | `{doc['file']}` | {doc['role']} | `{doc['sha256'][:16]}…` | {fmt_int(doc['approx_tokens'])} |\n")
    total_bytes = sum(doc["bytes"] for doc in docs)
    total_tokens = sum(doc["approx_tokens"] for doc in docs)
    out.append(f"\nTotal: {fmt_int(total_bytes)} bytes, about {fmt_int(total_tokens)} tokens ({TOKEN_NOTE})\n\n")
    out.append(integrity_section())
    out.append("\n")
    for doc in docs:
        data = (ROOT / doc["path"]).read_bytes()
        out.append(delimited(doc["order"], total, f"{domain['id']} · {doc['file']}", doc["file"], doc["sha256"], doc["role"], data))
    return "".join(out)


# --------------------------------------------------------------------------- indexes

def render_llms_txt(config: dict, catalog: dict) -> str:
    release = catalog["release"]
    profiles = catalog["profiles"]
    out = ["# Ordinative Sciences Framework — Technology of Expressions (TE)\n\n"]
    out.append(
        "> An open-source analytical operating system for AI agents and human analysts, based on Ordinative Set Theory (OST): "
        "structural coherence instead of statistical frequency, an always-active anti-bias protocol (Controfase), a mandatory "
        "source-verification gate (SVP), and domain modules for human figures, manipulation, complex systems, participant "
        f"impact, agreements and documentary casework. Release {release['version']} ({release['date']}).\n\n"
    )
    out.append(
        "The canonical texts live in `FRAMEWORKS/` (byte-exact, SHA-256 pinned). The files under `dist/` are derived "
        "single-file bundles for loading into an LLM. The files under `docs/handbook/` are for humans learning to use the "
        "framework. Author: Fabio Ghioni, Ordinative Sciences Foundation. License: MIT (papers: CC BY 4.0).\n\n"
    )
    out.append("## Load into an LLM\n\n")
    for key in ("minimal", "full"):
        profile = profiles[key]
        out.append(f"- [{profile['file'].rsplit('/', 1)[1]}]({profile['file']}): {profile['description']} About {fmt_int(profile['approx_tokens'])} tokens.\n")
    for domain in catalog["domain_frameworks"]:
        tokens = sum(doc["approx_tokens"] for doc in domain["documents"])
        out.append(f"- [{domain['bundle'].rsplit('/', 1)[1]}]({domain['bundle']}): {domain['id']} method documents, in reading order (method {domain['method_version']}, runtime {domain['runtime_version']}). About {fmt_int(tokens)} tokens.\n")
    out.append("- [catalog.json](dist/catalog.json): machine-readable catalog: documents, versions, roles, triggers, section outlines, hashes, token estimates, reference resolution.\n")
    out.append("- [dist/README.md](dist/README.md): what each derived file is and how to verify a download.\n\n")
    out.append("## Canonical documents (loading order)\n\n")
    for doc in catalog["documents"]:
        out.append(f"- [{doc['id']} {doc['version']}]({doc['path']}): {doc['role']}.\n")
    out.append("- [FRAMEWORKS/README.md](FRAMEWORKS/README.md): the loading table, the minimal profile, the integrity check, the archive policy.\n\n")
    out.append("## Domain frameworks with runtimes\n\n")
    for domain in catalog["domain_frameworks"]:
        out.append(f"- [{domain['id']}]({domain['entry_point']}): {domain['summary']}\n")
    out.append("\n## Documentation for humans\n\n")
    for doc in config["human_docs"]:
        out.append(f"- [{doc['title']}]({doc['path']}): {doc['description']}.\n")
    out.append("\n## Optional\n\n")
    out.append("- [README.md](README.md): repository overview.\n")
    out.append("- [ECOSYSTEM.md](ECOSYSTEM.md): the five repositories of the programme and how they connect.\n")
    out.append("- [CHANGELOG.md](CHANGELOG.md): release history.\n")
    out.append("- [The Collapse Equation](papers/collapse_equation/README.md): paper, v1.3, with the v1.2 set archived under its DOI.\n")
    out.append("- [The Direction Problem](papers/direction_problem/README.md): preprint v1.1, the causal argument behind g_j.\n")
    out.append("- [FRAMEWORKS/ARCHIVE/](FRAMEWORKS/ARCHIVE/): superseded editions, reference only.\n")
    return "".join(out)


def render_dist_readme(config: dict, catalog: dict, files: dict) -> str:
    release = catalog["release"]
    raw = config["raw_base_url"]
    out = ["# dist/ — download and load\n\n"]
    out.append(
        f"Derived files built by `tools/build_dist.py` from the canonical corpus in `../FRAMEWORKS/` "
        f"(release {release['version']}, {release['date']}). Nothing here is authoritative: the canonical files are. "
        "These files exist so that the framework can be downloaded as one file and loaded into an LLM without assembling "
        "it by hand. Rebuild with `make dist` (or `python3 tools/build_dist.py`) after any change under `FRAMEWORKS/`; "
        "`make check` fails when they drift.\n\n"
    )
    out.append("## Files\n\n| File | Contents | Bytes | ~Tokens | SHA-256 |\n|---|---|---|---|---|\n")
    descriptions = {
        "TE_LOADING_SET_MINIMAL.md": catalog["profiles"]["minimal"]["description"],
        "TE_LOADING_SET_FULL.md": catalog["profiles"]["full"]["description"],
        "catalog.json": "machine-readable catalog of the loading set: documents, versions, roles, triggers, section outlines, hashes, token estimates, reference resolution",
    }
    for domain in catalog["domain_frameworks"]:
        descriptions[domain["bundle"].rsplit("/", 1)[1]] = f"{domain['id']} method documents in reading order (method {domain['method_version']}, runtime {domain['runtime_version']})"
    for name in ("TE_LOADING_SET_MINIMAL.md", "TE_LOADING_SET_FULL.md", "TE_LEXX_METHOD.md", "TE_CASEWORK_METHOD.md", "catalog.json"):
        data = files[name]
        out.append(f"| [`{name}`]({name}) | {descriptions[name]} | {fmt_int(len(data))} | {fmt_int(approx_tokens(len(data)))} | `{sha256_of(data)[:16]}…` |\n")
    out.append("| `SHA256SUMS.txt` | hashes of the files above and of this README | | | |\n\n")
    out.append(f"Token figures: {TOKEN_NOTE}\n\n")
    out.append("## Which file to load\n\n")
    out.append(
        "- **A model with a large context (the whole framework at once):** `TE_LOADING_SET_FULL.md`.\n"
        "- **A constrained context, or a retrieval setup:** `TE_LOADING_SET_MINIMAL.md` as the always-loaded core, plus the "
        "individual canonical files from `../FRAMEWORKS/` as retrievable documents; `catalog.json` gives the triggers and "
        "section outlines a retriever or a router can use.\n"
        "- **Agreements:** the loading set, then `TE_LEXX_METHOD.md`. **Documentary audit or investigation:** the loading "
        "set, then `TE_CASEWORK_METHOD.md`. The runtimes stay in `../FRAMEWORKS/LEXX/v0_2_alpha3/` and `../FRAMEWORKS/CASEWORK/`.\n"
        "- **A human learning the framework:** start from `../docs/handbook/00_START_HERE.md`.\n\n"
    )
    out.append("## Verify a download\n\n")
    out.append(
        "```bash\ncd dist && shasum -a 256 -c SHA256SUMS.txt\n```\n\n"
        "Inside each bundle every document is delimited by lines carrying its SHA-256; the hashes are those of "
        "`../FRAMEWORKS/MANIFEST_SHA256.txt`.\n\n"
    )
    out.append("## Direct links\n\n")
    out.append(f"Raw files of the `main` branch: `{raw}/dist/<file>` and `{raw}/FRAMEWORKS/<file>`. ")
    out.append(f"For example `{raw}/dist/TE_LOADING_SET_FULL.md`.\n\n")
    out.append("## Release package\n\n")
    out.append(
        f"`te-frameworks-{release['version']}.zip`, built by `make package` and attached to the GitHub release, contains "
        "`FRAMEWORKS/`, `dist/`, `docs/`, `llms.txt`, `README.md`, `LICENSE`, `CITATION.cff`, `CHANGELOG.md` and "
        "`ECOSYSTEM.md`. The archive is not committed.\n"
    )
    return "".join(out)


# --------------------------------------------------------------------------- generation

def generate() -> dict:
    """Return {absolute Path: bytes} for every derived output."""
    config = load_json(CONFIG_PATH)
    lock = load_json(LOCK_PATH)
    release = release_info()
    catalog = build_catalog(config, lock, release)

    files = {}
    files["catalog.json"] = (json.dumps(catalog, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    files["TE_LOADING_SET_MINIMAL.md"] = render_loading_set("minimal", config, catalog).encode("utf-8")
    files["TE_LOADING_SET_FULL.md"] = render_loading_set("full", config, catalog).encode("utf-8")
    for domain in catalog["domain_frameworks"]:
        files[domain["bundle"].rsplit("/", 1)[1]] = render_domain_bundle(domain, catalog).encode("utf-8")
    files["README.md"] = render_dist_readme(config, catalog, files).encode("utf-8")
    sums = "".join(f"{sha256_of(data)}  {name}\n" for name, data in sorted(files.items(), key=lambda item: item[0].encode("utf-8")))
    files["SHA256SUMS.txt"] = sums.encode("utf-8")

    outputs = {DIST / name: data for name, data in files.items()}
    outputs[LLMS_PATH] = render_llms_txt(config, catalog).encode("utf-8")
    return outputs


def write_outputs(outputs: dict) -> None:
    DIST.mkdir(exist_ok=True)
    for path, data in outputs.items():
        path.write_bytes(data)
        print(f"wrote {path.relative_to(ROOT).as_posix()} ({fmt_int(len(data))} bytes)")


def check_outputs(outputs: dict) -> list:
    """Return the list of derived files that differ from the committed ones."""
    drift = []
    for path, data in outputs.items():
        if not path.exists() or path.read_bytes() != data:
            drift.append(path.relative_to(ROOT).as_posix())
    return drift


def write_zip(target: Path, release: dict) -> None:
    prefix = f"te-frameworks-{release['version']}"
    include_roots = ["FRAMEWORKS", "dist", "docs"]
    include_files = ["llms.txt", "README.md", "LICENSE", "CITATION.cff", "CHANGELOG.md", "ECOSYSTEM.md", "CONTRIBUTING.md"]
    year, month, day = (int(part) for part in release["date"].split("-"))
    stamp = (year, month, day, 0, 0, 0)
    members = []
    for root_name in include_roots:
        for path in sorted((ROOT / root_name).rglob("*")):
            if not path.is_file():
                continue
            relative = path.relative_to(ROOT)
            if any(part in EXCLUDED_DIR_NAMES for part in relative.parts) or path.suffix == ".zip" or path.suffix == ".pyc":
                continue
            members.append(relative)
    for name in include_files:
        if (ROOT / name).is_file():
            members.append(Path(name))
    target.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(target, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for relative in sorted(members, key=lambda item: item.as_posix()):
            info = zipfile.ZipInfo(f"{prefix}/{relative.as_posix()}", date_time=stamp)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            archive.writestr(info, (ROOT / relative).read_bytes())
    print(f"wrote {target.relative_to(ROOT).as_posix()} ({len(members)} files)")


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Build the derived distribution layer (dist/, llms.txt).")
    parser.add_argument("--check", action="store_true", help="rebuild in memory and compare with the committed outputs")
    parser.add_argument("--write-manifest", action="store_true", help="regenerate FRAMEWORKS/MANIFEST_SHA256.txt")
    parser.add_argument("--zip", nargs="?", const="", metavar="PATH", help="also write the download package (default dist/te-frameworks-<version>.zip)")
    args = parser.parse_args(argv)

    if args.write_manifest:
        MANIFEST_PATH.write_text(manifest_text(), encoding="utf-8", newline="\n")
        print(f"wrote {MANIFEST_PATH.relative_to(ROOT).as_posix()}")

    outputs = generate()
    if args.check:
        drift = check_outputs(outputs)
        if drift:
            print("derived files differ from the build; run `make dist`:\n  " + "\n  ".join(drift))
            return 1
        print("derived files are up to date")
        return 0

    write_outputs(outputs)
    if args.zip is not None:
        release = release_info()
        target = Path(args.zip) if args.zip else DIST / f"te-frameworks-{release['version']}.zip"
        write_zip(target, release)
    return 0


if __name__ == "__main__":
    sys.exit(main())
