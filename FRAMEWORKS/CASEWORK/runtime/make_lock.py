"""Build the framework lock consumed by ``casework.py prepare --lock``.

The lock freezes the exact framework files a case was prepared against. It has one
entry per *family*:

* single-file families (the TE documents) carry ``snapshot_path`` and ``sha256``;
* package families (``TE_CASEWORK``, ``TE_MODULE_LEXX``) carry the list of their
  ``files`` (``relative_path`` + ``sha256``) and a ``package_digest``. A package is the
  runtime: code, schemas, tests and configuration; Markdown documentation is excluded.

``package_digest`` is the SHA-256 of the UTF-8 text obtained by joining, in
byte-order of ``relative_path``, one line per file ``"<relative_path>  <sha256>"``,
each line terminated by ``\\n``. The algorithm is declared here so that anyone can
recompute the digest that ``CASEWORK/compatibility.json`` pins for a package family.

Family versions are read from ``CASEWORK/compatibility.json`` under the framework
root; the family -> path mapping below is the canonical file layout of
``FRAMEWORKS/``.

Usage::

    python runtime/make_lock.py --framework-root ../.. --out te_frameworks.lock.json

The script writes the lock only if the output path does not exist (use ``--force``
to overwrite) and refuses framework roots that contain symbolic links.
"""
import argparse
import hashlib
import json
import sys
from pathlib import Path

FAMILY_PATHS = {
    "TE_BOOTLOADER": "TE_BOOTLOADER_v7_1_1_EN.md",
    "TE_PROTOCOLS": "TE_PROTOCOLS_v1_1_EN.md",
    "TE_CORE": "TE_CORE_v5_2_1_EN.md",
    "TE_OST": "TE_OST_v2_1_EN.md",
    "TE_OST_TELEODYNAMICS": "TE_OST_Extension_Teleodynamics_v1_1_EN.md",
    "TE_SYMBOL_CANON": "TE_SYMBOL_CANON_v1_0_EN.md",
    "TE_MODULE_SVP": "TE_MODULE_SVP_v5_1_EN.md",
    "TE_MODULE_LENS": "TE_MODULE_LENS_v5_1_EN.md",
    "TE_MODULE_PPRO": "TE_MODULE_PPRO_v5_2_EN.md",
    "TE_MODULE_SCIMS": "TE_MODULE_SCIMS_v5_1_EN.md",
    "TE_MODULE_VERI": "TE_MODULE_VERI_v1_0_EN.md",
    "TE_OBSERVER": "TE_OBSERVER_v1_1_EN.md",
    # package families: a directory under the framework root
    # (the LEXX family is its runtime: identical bytes in the canonical corpus and here)
    "TE_MODULE_LEXX": "LEXX/v0_2_alpha3/",
    "TE_CASEWORK": "CASEWORK/",
}

EXCLUDED_DIR_NAMES = {"__pycache__", ".git", ".venv", "venv"}
# Package families cover code, schemas, tests and configuration. Markdown documentation is
# excluded on purpose: the same runtime ships with documentation in different languages
# (the canonical corpus and the public repository), and the pinned digest must be identical
# wherever the runtime bytes are identical.
EXCLUDED_SUFFIXES = {".md"}


def file_hash(path):
    digest = hashlib.sha256()
    with open(path, "rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def package_files(root, folder):
    base = root / folder
    if not base.is_dir():
        raise SystemExit(f"Package directory missing: {base}")
    records = []
    for path in sorted(base.rglob("*")):
        if not path.is_file():
            continue
        if any(part in EXCLUDED_DIR_NAMES for part in path.relative_to(root).parts):
            continue
        if path.suffix.lower() in EXCLUDED_SUFFIXES:
            continue
        if path.is_symlink():
            raise SystemExit(f"Symbolic link inside package: {path}")
        relative = path.relative_to(root).as_posix()
        records.append({"relative_path": relative, "sha256": file_hash(path)})
    records.sort(key=lambda item: item["relative_path"].encode("utf-8"))
    return records


def package_digest(records):
    text = "".join(f"{item['relative_path']}  {item['sha256']}\n" for item in records)
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def build_lock(root):
    # ``framework_root`` is recorded as given (the runtime never reads it back): a lock
    # built from the repository root with ``--framework-root FRAMEWORKS`` stays portable.
    label = Path(root).as_posix()
    root = Path(root).resolve()
    if root.is_symlink():
        raise SystemExit(f"Framework root is a symbolic link: {root}")
    profile_path = root / "CASEWORK" / "compatibility.json"
    profile = json.loads(profile_path.read_text(encoding="utf-8"))
    versions = {item["family"]: item["version"] for item in profile["dependencies"]}
    versions.setdefault("TE_CASEWORK", profile.get("runtime_version", "unknown"))
    families = {}
    for family, target in FAMILY_PATHS.items():
        version = versions.get(family)
        if version is None:
            raise SystemExit(f"No version for family {family} in {profile_path}")
        if target.endswith("/"):
            records = package_files(root, target)
            families[family] = {"version": version, "files": records,
                                "package_digest": package_digest(records)}
        else:
            path = root / target
            if not path.is_file():
                raise SystemExit(f"Framework file missing: {path}")
            families[family] = {"version": version, "snapshot_path": target,
                                "sha256": file_hash(path)}
    return {"lock_format": "te_frameworks.lock/1",
            "package_digest_algorithm": "sha256 over lines '<relative_path>  <sha256>\\n' sorted by relative_path (UTF-8 byte order)",
            "framework_root": label, "families": families}


def main(argv=None):
    parser = argparse.ArgumentParser(description="Build the TE framework lock for CASEWORK.")
    parser.add_argument("--framework-root", required=True, type=Path, help="directory holding the TE_*.md files, LEXX/ and CASEWORK/")
    parser.add_argument("--out", required=True, type=Path, help="lock file to write (JSON)")
    parser.add_argument("--force", action="store_true", help="overwrite an existing lock file")
    args = parser.parse_args(argv)
    if args.out.exists() and not args.force:
        raise SystemExit(f"Refusing to overwrite existing lock: {args.out} (use --force)")
    lock = build_lock(args.framework_root)
    args.out.write_text(json.dumps(lock, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    summary = {family: (entry.get("sha256") or entry.get("package_digest"))[:16] for family, entry in lock["families"].items()}
    print(json.dumps({"written": str(args.out), "families": summary}, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
