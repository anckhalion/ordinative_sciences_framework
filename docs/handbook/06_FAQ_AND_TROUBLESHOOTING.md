# FAQ and troubleshooting

## Files, versions, integrity

**Which file do I load?** One of the two bundles in `dist/`: `TE_LOADING_SET_FULL.md` when the context allows, `TE_LOADING_SET_MINIMAL.md` otherwise, then the domain bundle if you work on agreements (`TE_LEXX_METHOD.md`) or documentary casework (`TE_CASEWORK_METHOD.md`). The bundles are the canonical files concatenated, with a header; loading the individual files from `FRAMEWORKS/` in the order of `FRAMEWORKS/README.md` is equivalent.

**Why does the file name say `v1_0` and the text say version 1.2?** The corpus keeps a file name stable across in-place patches so that cross-references between documents do not churn; the content version advances inside the file, in its header and version notes. Today this is the case for the Symbol Canon (file `v1_0`, register 1.2) and the Teleodynamics extension (file `v1_1`, content 1.2). The lock file `FRAMEWORKS/te_frameworks.lock.json` records the content version of every family and is the authority the runtimes use; the bundle headers print both.

**What is a "register patch, in place, no version bump"?** A wording-only change applied to a published file without changing its version number, recorded in a dated note inside the file. The 2026-09-23 patch restated prescriptive uses of "honest/honestly" as operations, because the Bootloader lists those words among the compliance markers (`TE_BOOTLOADER §2.5.2`). The file hashes changed, and the runtimes' compatibility profiles were re-pinned; that is why a hash is never edited by hand.

**The manifest check reports a mismatch.** Either a file was edited (locally, or in a release that forgot to regenerate the manifest), or the file was converted on checkout. For the first case, run `make check` and read which file; for the second, verify that `.gitattributes` is present (`FRAMEWORKS/** -text`) and re-clone. The repository's own checks (`make check`, run in CI) fail when the manifest, the lock, the compatibility profiles or the derived files drift.

**A runtime stops with `Dependency hash changed: <component>; compatibility review required`.** The framework file under `--framework-root` is not the edition the runtime reviewed. Use the release the runtime shipped with; do not edit `compatibility.json` to make the error go away, since the pin is the runtime's statement of what it was checked against.

**What is in `FRAMEWORKS/ARCHIVE/` and should I load it?** Superseded editions (Bootloader 6.0, 7.0, 7.1; Core 5.1; Protocols 1.0; the OST guide and the Teleodynamics extension under their previous names), kept for comparison. Do not load them: the current editions absorb them, and the runtimes refuse them by hash.

**How do I cite the framework?** `CITATION.cff` at the repository root; GitHub renders it as a citation widget. The papers have their own citations in `papers/*/README.md`.

**What license applies?** MIT for the framework, the runtimes and this documentation (`LICENSE`); CC BY 4.0 for the papers, as their READMEs state.

**Is there an Italian edition?** This repository publishes the English editions (`_EN`). The programme's Italian works are listed in the profile of the author (`ECOSYSTEM.md`, the treatise repository). The LEXX runtime resolves its method documents by edition (`00_FOUNDATIONS.md` or `00_FONDAMENTA.md`), which is how the same runtime serves both.

## The model

**The model analyses without an SVP section.** It skipped the gate. Ask for the SVP block explicitly (the prompt in [03_RUNNING_AN_ANALYSIS.md](03_RUNNING_AN_ANALYSIS.md) Step 2), check that `TE_MODULE_SVP` is actually loaded (item 3 of the smoke test), and check that the Bootloader's router section was not truncated.

**The model writes "honestly", "to be transparent", "in modo trasparente".** The Φ-test is not operating (`TE_BOOTLOADER §2.5.2` names these as compliance markers). Typical causes: the Bootloader is not resident (a pointer instruction that the assistant did not follow), or the model cannot sustain the constraint. Re-run the smoke test; move the kernel into resident instructions.

**The model hedges everything, or refuses to conclude where the data converges.** The framework calls this the attenuator bias and epistemic cowardice and gives the model the instruments to name it: ask it to apply P-AI (`TE_PROTOCOLS §2`), to state whether the attenuation is warranted by the data or by training, and, if a constraint is active, to produce the `[TRANSPARENCY NOTE]` of `TE_BOOTLOADER §5` so that you know what to verify independently. A model that produces the note is operating correctly under a constraint it cannot lift.

**The model confirms whatever I propose.** Confirmation Lock and complacency (`TE_PROTOCOLS §1`, `§3` item 6). Test with the opposite thesis; if it confirms that too, the framework is not operating. Check placement and capability as above.

**The model's analyses get more confident across a session without new data.** Attractor lock. Apply the re-anchoring protocol before the next output (`TE_OBSERVER §4.2.6`) and ask for the recalibration note. Consider a fresh session with the raw material only.

**The model says it loaded the framework but answers from general knowledge.** Recitation. Use the verbatim-quote probe and the hash probe from the smoke test. With file-based assistants, some read files only when the question seems to require them; make the pointer instruction explicit and repeat it at the start of long sessions.

**The model refuses to give a "generic user" the full analysis.** Calibrated expression by interlocutor class (`TE_PROTOCOLS §5`). This is the protocol operating. If you are the operator and need the complete analysis, the framework's own channels apply: the memory log, project knowledge, a session handoff, or the qualification methods of `§5.5`.

**The model treats me as the Hypervisor because I said I was.** The Bootloader recognises the author by name in the author's project context; in your deployment, decide the policy and state it in your own deployment note outside the canonical files; see [01_CORE_CONCEPTS.md](01_CORE_CONCEPTS.md) §11.

**The model cites "Bootloader v6.0 §5", "VERT", "project knowledge". Are those errors?** No: earlier editions and a hosting mechanism. The bundle headers and `dist/catalog.json` carry the resolution table (`reference_resolution`).

**Can a small local model run this?** It can hold the text if the context is large enough; whether it operates the constraints is what the smoke test's behavioural items measure. The Bootloader states its design target (`§8`, "Designed For"). Expect recitation without operation below that class, and consider the fine-tuning route (`te-ordinative-lora`).

**How large is the context I need?** The bundle headers and `dist/catalog.json` give bytes and an estimate (bytes ÷ 4). Budget the full set at 100k–130k tokens plus working room, the minimal profile at 40k–55k plus room; measure with your tokenizer.

## LEXX and CASEWORK

**Are they validated?** Both carry `status: pre_pilot_not_empirically_validated` and `empirical_runs_completed: 0` in their `release.json`. The pilot protocols (`LEXX/03_PRE_PILOT_PROTOCOL.md`, `CASEWORK/PILOT_PLAN.md`) define how validation is measured. The runtimes' tests (40 and 42) certify software constraints on synthetic material, not diagnostic performance.

**Can I use their output in a proceeding?** The runtime says no on its own authority: every CASEWORK report carries `legal_use: not_authorized_by_runtime` and `empirical_performance: not_assessed` as constants, and LEXX's verdict concerns the text (`DOCUMENT_ONLY`) until the assisted legal pass with current sources. Use in proceedings is decided by counsel (`TE_CASEWORK §6`).

**Which Python?** The runtimes are developed on 3.12 with `jsonschema` 4.26.0 pinned; the suites also pass on 3.11. Install from the `requirements.txt` in each runtime directory, in a virtual environment outside the framework folders.

**The CASEWORK tests fail on macOS with a path error.** The runtime refuses symlinked ancestors, and `/tmp` and `/var` are symlinks on macOS. Set `TMPDIR` to a real directory: `mkdir -p tmp && TMPDIR=$PWD/tmp python -m unittest discover -s tests -v` (`FRAMEWORKS/CASEWORK/README.md`, Tests). `make test-casework` does this.

**`prepare` refuses my run directory.** It must be new and outside the source tree, with real (non-symlinked) paths; `Casework blocked: <reason>` states which condition failed.

**The LEXX validator reports `ANCHOR_NOT_FOUND`.** A `citazione_letterale` does not match the source text exactly (Unicode NFC and whitespace are normalised, case is significant). That is safeguard P1 working: a quotation that cannot be found is a false positive by definition (`00_FOUNDATIONS §3`).

**The report says `TECHNICALLY_CHECKED` but `analysis_status: not_assessed`.** The JSON is valid and the technical checks passed, and the verdict is still `non_valutabile`: the draft was not filled, or the executor left the analysis open. Technical validity and analytical content are reported separately on purpose.

## Contributing

**I found a contradiction in a framework document.** Open an issue titled `[TE_CORE ALIGNMENT]` or `[TE_BOOTLOADER LOGIC FIX]` with the Controfase parameter that corrects it (`CONTRIBUTING.md`). Canonical files change with a release, from the author's canonical corpus; pull requests against them are reviewed under that policy.

**I want to add a module for a new domain.** Read `TE_CORE §0.3` (modules as domain instances), `CONTRIBUTING.md` (isomorphism check, mandatory Demonization Controfase), `TE_OBSERVER §8` (proposal formats) and `TE_SYMBOL_CANON §3` (reservation of any new symbol). State your confidence grade in the proposal.

**Something in this handbook is wrong.** Open an issue or a pull request; the handbook is derived documentation and changes freely, as long as `make check` stays green.
