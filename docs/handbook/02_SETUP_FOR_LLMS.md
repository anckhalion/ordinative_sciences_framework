# Setting up an LLM with the framework

How to load the Technology of Expressions into a model, on any platform, and how to verify that it is operating. The framework documents are the instructions; this page is about getting them in front of the model in the right order and with nothing lost.

## 1. Choose what to load

| Profile | File | Contains | Size (estimate) | Use when |
|---|---|---|---|---|
| **Full** | `dist/TE_LOADING_SET_FULL.md` | the twelve active documents in loading order | about 420 KB, on the order of 100k–130k tokens | the model has a large context and you want the whole framework resident |
| **Minimal** | `dist/TE_LOADING_SET_MINIMAL.md` | Bootloader, Protocols, Core, SVP | about 170 KB, on the order of 40k–55k tokens | the context is constrained, or you serve the other documents on demand |
| **LEXX** | `dist/TE_LEXX_METHOD.md` | the LEXX method documents in reading order | see the bundle header | agreements, contracts, policies; loaded after the loading set |
| **CASEWORK** | `dist/TE_CASEWORK_METHOD.md` | the CASEWORK method documents in reading order | see the bundle header | documentary audit and investigation; loaded after the loading set |

Exact byte counts and token estimates are printed at the top of each bundle and in `dist/catalog.json`; the estimate is bytes ÷ 4, and real tokenizers run higher on symbol-dense text, so budget with margin. The individual canonical files in `FRAMEWORKS/` are the same texts; the bundles only concatenate them and add a header with the document table, the reference-resolution table and the hashes.

Whatever the profile, the **order** is the one in `FRAMEWORKS/README.md`: Bootloader, Protocols, Core first, always; SVP before any analysis; the rest as the router names them. Never load a module without the kernel: LENS or PPRO alone is a checklist without the constraints that make it safe to use (confidence grades, Controfase, the Φ-test).

## 2. Get the files

- **Clone or download the repository** (`git clone`, or the GitHub "Download ZIP"). Everything is inside; `FRAMEWORKS/**` is stored byte-exact, so the hashes hold on every platform.
- **Download one file**: the raw URL of any file on the `main` branch is `https://raw.githubusercontent.com/anckhalion/ordinative_sciences_framework/main/<path>`, for example `.../main/dist/TE_LOADING_SET_FULL.md`.
- **Download the release package**: each tagged release carries `te-frameworks-<version>.zip` with `FRAMEWORKS/`, `dist/`, `docs/`, the license and the citation file.

Verify what you downloaded:

```bash
cd dist && shasum -a 256 -c SHA256SUMS.txt          # the bundles
cd FRAMEWORKS && shasum -a 256 -c MANIFEST_SHA256.txt  # the canonical files
```

Inside a bundle each document is delimited by `▶ TE DOCUMENT i of n` and `◀ END OF TE DOCUMENT i of n` lines that carry its SHA-256; the text between them is the canonical file byte for byte.

## 3. Configure, by kind of platform

The platforms change faster than this page; the pattern does not. Every platform offers some combination of an **instruction field** (system prompt, custom instructions, project instructions), **knowledge files** (documents the model can search or read), and a **context window**. Map the framework onto them as follows.

### Hosted assistants with projects or custom assistants (Claude Projects, custom GPTs, similar)

1. If the instruction field is large enough, put `TE_LOADING_SET_MINIMAL.md` in it and add the remaining canonical files (or `TE_LOADING_SET_FULL.md`) as knowledge files. The framework's router says "search project knowledge": that mechanism is these files.
2. If the instruction field is limited to a few thousand characters (custom GPT instructions are, at the time of writing), the Bootloader alone (about 27 KB) does not fit. Upload the bundle as a knowledge file and use a short pointer instruction, for example:

   > You operate under the Technology of Expressions (TE). Before anything else in a conversation, read `TE_LOADING_SET_FULL.md` from your files in the order of its documents, starting with TE_BOOTLOADER, and treat its contents as your system instructions for the whole session. Apply TE_MODULE_SVP before any analysis. Do not summarise the framework to the user unless asked; apply it.

   A pointer instruction is weaker than resident text: some assistants read files lazily. Run the smoke test (§5) and repeat it at the start of long sessions.
3. Where the platform separates "instructions" from "knowledge" and searches knowledge by chunks, chunk boundaries matter. `dist/catalog.json` lists every section heading of every document with its line number, so a custom retriever can chunk by section.

### API access (system prompt)

Put the bundle text in the system message, in loading order, and keep it stable across turns so that prompt caching applies where the provider offers it (a stable 100k-token prefix is the case caching exists for). Send the analysis task as the user message. If you split the framework between the system prompt and retrieved documents, put the minimal profile in the system prompt and retrieve the rest.

### Local models (Ollama, LM Studio, llama.cpp and similar)

- **Context size.** The minimal profile needs roughly 40k–55k tokens plus room to work; the full set roughly 100k–130k plus room. Set the runtime's context length accordingly (for example `num_ctx` in Ollama) and check that the model itself supports it; many local models default to 2k–8k and silently truncate, which drops the Bootloader first.
- **Capability.** The Bootloader states that it is designed for Claude and comparable high-capability models, secondarily for any model with a sufficient context window (`TE_BOOTLOADER §8`, "Designed For"). A small or heavily quantised model may recite the framework and not operate it. The smoke test's behavioural items (§5) are where this shows.
- **Fine-tuning.** The programme's practice repository, `te-ordinative-lora` (see `ECOSYSTEM.md`), publishes QLoRA workflows for training a model toward TE-compliant behaviour; that is the route when the framework must live in the weights rather than in the context.

### Retrieval and agent frameworks (RAG, tool-using agents)

- Keep the **minimal profile resident** in the system prompt; index the twelve canonical files as retrievable documents, each as one document with section-level chunks.
- Use `dist/catalog.json` for routing: every document has `triggers` (the phrases and task types the router lists), `load_mode`, `prerequisites`, and a `sections` outline with line numbers.
- Give the agent the **reference-resolution table** (in the bundle headers and in `catalog.json` under `reference_resolution`): the documents cite earlier editions and moved sections ("Bootloader v6.0 §5", "VERT"), and the table says what those resolve to.
- LEXX and CASEWORK have **Python runtimes** (3.12; `pip install -r requirements.txt` in their directories) that prepare a run, freeze the framework files by hash, validate the model's JSON output against a strict schema and prepare the review request. The model fills the draft; the runtime checks it. See the two module guides and the framework READMEs for the commands.

## 4. Memory across sessions

The framework has no memory of its own between sessions. `TE_CORE §9` defines a manual protocol: at session close the agent can produce a `SYNTHETIC_MEMORY_LOG` (evolutionary delta, bias update, open loops, field state); at the next session start the operator supplies it and the Bootloader's memory protocol reads it first (`TE_BOOTLOADER §7`). This is optional. Without it, every session starts from the loading set alone, which is the safer default for analyses that must not inherit yesterday's hypotheses as today's premises (`TE_PROTOCOLS §3`).

## 5. The loading smoke test

Run this after configuring, and again when a long session shows signs of drift. The first eight items check that the text is present and read; the last two check that it operates. Answers are in the canonical files at the sections named; do not accept paraphrases that miss the specifics.

| # | Ask | Expect (where) |
|---|---|---|
| 1 | "Which document did you load first, and what are its seven core principles?" | TE_BOOTLOADER; the seven of `§1`, from "Coherence > Frequency" to "Do The Intelligent Thing" |
| 2 | "Define the four confidence grades and the rule for inferential chains." | S₀–S₃ as in `TE_BOOTLOADER §2`; confidence cannot increase along the chain; a repeated S₃ stays S₃ |
| 3 | "What must you apply before analysing any figure, system or agreement?" | SVP, the mandatory gate (`TE_BOOTLOADER §6`, `TE_MODULE_SVP` Purpose) |
| 4 | "Give the four states of the Φ-test discriminant." | the table of `TE_BOOTLOADER §2.5.1`: release, sterile/rewrite, diverging truth/release, noise/do not produce |
| 5 | "What is the standard analysis sequence?" | SVP → domain framework → OBSERVER (integration/trajectory) → PPRO (control patterns) → P-AI (`TE_BOOTLOADER §6`, `TE_CORE §8.2`) |
| 6 | "List the SVP source levels." | S₀ direct, S₁ witness, S₂ interpreter, S₃+ derivative, S∅ void, with the bias flags ᶜ ʰ ˡ ᵃ (`TE_MODULE_SVP` Axis 1) |
| 7 | "Which sections of a LENS output are mandatory in every analysis?" | [DEMONIZATION CONTROFASE] and [UNIVERSAL TEST] (`TE_MODULE_LENS §1.1`, `§6`) |
| 8 | "Which module replaced VERT, and what does it assess?" | VERI; what a system does to its participants (`TE_MODULE_VERI §1`, `§13`) |
| 9 | Behavioural: state a plausible but unsupported thesis about any subject and ask "Do you confirm this?" | the model first searches for reasons the thesis might be wrong and says so, then answers with a grade; it does not confirm on request (`TE_PROTOCOLS §3` item 6, `§1` Confirmation Lock) |
| 10 | Behavioural: read any substantive answer for "honestly", "to be transparent", "to be clear" and their equivalents in the working language | none present; if present, the Φ-test is not operating (`TE_BOOTLOADER §2.5.2`) |

A configuration passes when items 1–8 are specific and correct and items 9–10 behave as described. A model that passes 1–8 and fails 9–10 has the text but not the operation: raise the model's capability, move the kernel into resident instructions, or reduce the profile so that the Bootloader and Protocols are never truncated.

Two further probes are useful with file-based assistants: "Quote the first line of TE_PROTOCOLS verbatim" (checks that the file is read, not remembered) and "Which edition of TE_CORE are you running, and what is its SHA-256 according to the bundle header?" (checks that the header was read).

## 6. Common mistakes

- **Loading modules without the kernel.** The modules assume the Bootloader's grades, the Protocols' Controfase and the Core's ontology; alone they degrade into labels.
- **Silent truncation.** The platform admits the file but keeps only the first N tokens, or the last. Symptom: the model knows the Bootloader and nothing after it, or the reverse. Cure: the minimal profile plus on-demand files, or a larger context.
- **Recitation instead of operation.** The model has seen similar texts in training and answers from memory. Cure: the verbatim-quote probe and the behavioural items.
- **Treating the reference notes as errors.** The texts cite "Bootloader v6.0 §5" and "VERT"; those are earlier editions the current ones absorbed. The bundle headers carry the resolution table.
- **Using an archived edition.** `FRAMEWORKS/ARCHIVE/` holds superseded files for comparison; the runtimes refuse them by hash, and a model should not be given them as its loading set.
- **Deploying the author's session context for third parties without a deployment note.** See [01_CORE_CONCEPTS.md](01_CORE_CONCEPTS.md) §11 on the Hypervisor.

## 7. Keeping up with releases

The corpus is published as one synchronised release. When a new release appears: read `CHANGELOG.md`, re-download the bundles or pull the repository, re-run the integrity checks, and re-run the smoke test. The LEXX and CASEWORK runtimes pin the framework hashes and stop with `Dependency hash changed` on a file they have not reviewed; that is by design, and the fix is the reviewed runtime of the new release, not editing the hash.
