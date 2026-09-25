#!/usr/bin/env python3
"""Consistency checks for the repository. Exit status 1 when a check fails.

  manifest     every file under FRAMEWORKS/ is listed in MANIFEST_SHA256.txt with its current SHA-256
  lock         te_frameworks.lock.json equals what CASEWORK/runtime/make_lock.py builds from the files
  profiles     the hashes pinned by the LEXX and CASEWORK compatibility profiles match the files and the lock
  dist         dist/ and llms.txt equal what tools/build_dist.py builds (no drift)
  docs         every human document listed in tools/loading_set.json exists
  links        relative Markdown links resolve to existing files (a broken link inside FRAMEWORKS/ is
               reported as a warning, because those files are canonical and change only with a release)

Usage: python3 tools/check_repo.py [--no-links]
"""
import argparse
import hashlib
import importlib.util
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import build_dist  # noqa: E402

FRAMEWORKS = ROOT / "FRAMEWORKS"
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
SKIP_DIRS = {".git", "__pycache__", ".venv", "venv", "runs", "tmp"}


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_make_lock():
    path = FRAMEWORKS / "CASEWORK" / "runtime" / "make_lock.py"
    spec = importlib.util.spec_from_file_location("make_lock", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def check_manifest() -> list:
    problems = []
    listed = {}
    for line in build_dist.MANIFEST_PATH.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        digest, _, relative = line.partition("  ")
        listed[relative] = digest
    actual = {}
    for relative in build_dist.framework_files():
        actual[relative] = sha256_file(FRAMEWORKS / relative)
    for relative, digest in actual.items():
        if relative not in listed:
            problems.append(f"not in manifest: {relative}")
        elif listed[relative] != digest:
            problems.append(f"hash differs: {relative}")
    for relative in listed:
        if relative not in actual:
            problems.append(f"listed but missing: {relative}")
    return problems


def check_lock() -> list:
    make_lock = load_make_lock()
    built = make_lock.build_lock(FRAMEWORKS)
    built["framework_root"] = "FRAMEWORKS"
    committed = json.loads(build_dist.LOCK_PATH.read_text(encoding="utf-8"))
    problems = []
    for family, entry in built["families"].items():
        current = committed.get("families", {}).get(family)
        if current != entry:
            problems.append(f"lock family differs from the files: {family}")
    for family in committed.get("families", {}):
        if family not in built["families"]:
            problems.append(f"lock family without a mapping in make_lock.py: {family}")
    return problems


def check_profiles() -> list:
    problems = []
    lock = json.loads(build_dist.LOCK_PATH.read_text(encoding="utf-8"))["families"]
    lexx = json.loads((FRAMEWORKS / "LEXX" / "v0_2_alpha3" / "compatibility.json").read_text(encoding="utf-8"))
    for dep in lexx["dependencies"]:
        path = FRAMEWORKS / dep["file"]
        if not path.is_file():
            problems.append(f"LEXX profile: missing file {dep['file']}")
        elif sha256_file(path) != dep["sha256"]:
            problems.append(f"LEXX profile: hash differs for {dep['file']}")
    casework = json.loads((FRAMEWORKS / "CASEWORK" / "compatibility.json").read_text(encoding="utf-8"))
    for dep in casework["dependencies"]:
        family = lock.get(dep["family"])
        if family is None:
            problems.append(f"CASEWORK profile: family not in lock: {dep['family']}")
            continue
        digest = family.get("sha256") or family.get("package_digest")
        if family.get("version") != dep["version"]:
            problems.append(f"CASEWORK profile: version differs for {dep['family']}")
        if digest != dep["digest"]:
            problems.append(f"CASEWORK profile: digest differs for {dep['family']}")
    return problems


def check_dist() -> list:
    return [f"derived file differs from the build: {name}" for name in build_dist.check_outputs(build_dist.generate())]


def check_docs() -> list:
    config = json.loads(build_dist.CONFIG_PATH.read_text(encoding="utf-8"))
    return [f"human document listed in loading_set.json is missing: {doc['path']}"
            for doc in config["human_docs"] if not (ROOT / doc["path"]).is_file()]


def markdown_files():
    for path in sorted(ROOT.rglob("*.md")):
        if any(part in SKIP_DIRS for part in path.relative_to(ROOT).parts):
            continue
        yield path


def check_links() -> tuple:
    """Return (errors, warnings)."""
    errors, warnings = [], []
    for path in markdown_files():
        text = path.read_text(encoding="utf-8")
        in_fence = False
        for number, line in enumerate(text.splitlines(), 1):
            if line.strip().startswith("```"):
                in_fence = not in_fence
                continue
            if in_fence:
                continue
            for target in LINK_RE.findall(line):
                if re.match(r"^[a-z][a-z0-9+.-]*:", target) or target.startswith("#"):
                    continue
                target_path = target.split("#", 1)[0]
                if not target_path:
                    continue
                resolved = (path.parent / target_path).resolve()
                if not resolved.exists():
                    message = f"{path.relative_to(ROOT).as_posix()}:{number}: broken link {target}"
                    if FRAMEWORKS in path.parents:
                        warnings.append(message)
                    else:
                        errors.append(message)
    return errors, warnings


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Repository consistency checks.")
    parser.add_argument("--no-links", action="store_true", help="skip the Markdown link check")
    args = parser.parse_args(argv)

    failed = False
    checks = [("manifest", check_manifest), ("lock", check_lock), ("profiles", check_profiles),
              ("dist", check_dist), ("docs", check_docs)]
    for name, check in checks:
        problems = check()
        status = "ok" if not problems else "FAIL"
        print(f"[{status}] {name}")
        for problem in problems:
            print(f"       {problem}")
        failed = failed or bool(problems)
    if not args.no_links:
        errors, warnings = check_links()
        print(f"[{'ok' if not errors else 'FAIL'}] links ({len(warnings)} warning(s) in canonical files)")
        for problem in errors:
            print(f"       {problem}")
        for problem in warnings:
            print(f"       warning: {problem}")
        failed = failed or bool(errors)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
