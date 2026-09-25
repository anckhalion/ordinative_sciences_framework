# dist/ — download and load

Derived files built by `tools/build_dist.py` from the canonical corpus in `../FRAMEWORKS/` (release 2.0.0, 2026-09-23). Nothing here is authoritative: the canonical files are. These files exist so that the framework can be downloaded as one file and loaded into an LLM without assembling it by hand. Rebuild with `make dist` (or `python3 tools/build_dist.py`) after any change under `FRAMEWORKS/`; `make check` fails when they drift.

## Files

| File | Contents | Bytes | ~Tokens | SHA-256 |
|---|---|---|---|---|
| [`TE_LOADING_SET_MINIMAL.md`](TE_LOADING_SET_MINIMAL.md) | Bootloader, Protocols, Core and the SVP gate: the minimal profile for a constrained context (FRAMEWORKS/README.md, loading table entries 1, 2, 3, 6). The other documents are fetched on demand. | 172,662 | 43,166 | `80a0b36cdc9e7928…` |
| [`TE_LOADING_SET_FULL.md`](TE_LOADING_SET_FULL.md) | All twelve active framework documents in loading order: the complete TE loading set in one file. | 422,145 | 105,537 | `2b4f617e11d602ad…` |
| [`TE_LEXX_METHOD.md`](TE_LEXX_METHOD.md) | LEXX method documents in reading order (method 0.1, runtime 0.2.0-alpha.3) | 92,380 | 23,095 | `cfe2ac7414e886ca…` |
| [`TE_CASEWORK_METHOD.md`](TE_CASEWORK_METHOD.md) | CASEWORK method documents in reading order (method 0.1, runtime 0.1.0-alpha.1) | 43,683 | 10,921 | `3c91da1767a5ca98…` |
| [`catalog.json`](catalog.json) | machine-readable catalog of the loading set: documents, versions, roles, triggers, section outlines, hashes, token estimates, reference resolution | 129,466 | 32,367 | `e9c88290536fea46…` |
| `SHA256SUMS.txt` | hashes of the files above and of this README | | | |

Token figures: approx_tokens = ceil(bytes / 4). A rough estimate for context-window planning; real counts depend on the tokenizer and run higher for symbol-dense text.

## Which file to load

- **A model with a large context (the whole framework at once):** `TE_LOADING_SET_FULL.md`.
- **A constrained context, or a retrieval setup:** `TE_LOADING_SET_MINIMAL.md` as the always-loaded core, plus the individual canonical files from `../FRAMEWORKS/` as retrievable documents; `catalog.json` gives the triggers and section outlines a retriever or a router can use.
- **Agreements:** the loading set, then `TE_LEXX_METHOD.md`. **Documentary audit or investigation:** the loading set, then `TE_CASEWORK_METHOD.md`. The runtimes stay in `../FRAMEWORKS/LEXX/v0_2_alpha3/` and `../FRAMEWORKS/CASEWORK/`.
- **A human learning the framework:** start from `../docs/handbook/00_START_HERE.md`.

## Verify a download

```bash
cd dist && shasum -a 256 -c SHA256SUMS.txt
```

Inside each bundle every document is delimited by lines carrying its SHA-256; the hashes are those of `../FRAMEWORKS/MANIFEST_SHA256.txt`.

## Direct links

Raw files of the `main` branch: `https://raw.githubusercontent.com/anckhalion/ordinative_sciences_framework/main/dist/<file>` and `https://raw.githubusercontent.com/anckhalion/ordinative_sciences_framework/main/FRAMEWORKS/<file>`. For example `https://raw.githubusercontent.com/anckhalion/ordinative_sciences_framework/main/dist/TE_LOADING_SET_FULL.md`.

## Release package

`te-frameworks-2.0.0.zip`, built by `make package` and attached to the GitHub release, contains `FRAMEWORKS/`, `dist/`, `docs/`, `llms.txt`, `README.md`, `LICENSE`, `CITATION.cff`, `CHANGELOG.md` and `ECOSYSTEM.md`. The archive is not committed.
