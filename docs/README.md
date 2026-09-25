# Documentation

Two audiences use this repository, and the material is split accordingly.

| Audience | Start from | What it is |
|---|---|---|
| An AI agent (system prompt, project knowledge, retrieval) | [`dist/TE_LOADING_SET_FULL.md`](../dist/TE_LOADING_SET_FULL.md) or [`FRAMEWORKS/`](../FRAMEWORKS/README.md) | the framework itself: the canonical texts, written as instructions to an AI, in loading order |
| A human learning to use the framework | [`handbook/00_START_HERE.md`](handbook/00_START_HERE.md) | the handbook: orientation, concepts, setup, workflow, training path, module guides |
| A maintainer or contributor | [`handbook/07_MAINTAINERS_GUIDE.md`](handbook/07_MAINTAINERS_GUIDE.md) | how the repository is built, checked and released |

## The handbook

| File | Read it when |
|---|---|
| [00_START_HERE.md](handbook/00_START_HERE.md) | you meet the framework for the first time |
| [01_CORE_CONCEPTS.md](handbook/01_CORE_CONCEPTS.md) | you need the ideas an operator must hold: ordinative set, coherence against frequency, confidence grades, source levels, Controfase, the Φ-test |
| [02_SETUP_FOR_LLMS.md](handbook/02_SETUP_FOR_LLMS.md) | you are configuring a model (hosted, API, local, retrieval) and want to verify that it loaded the framework |
| [03_RUNNING_AN_ANALYSIS.md](handbook/03_RUNNING_AN_ANALYSIS.md) | you are running an analysis with a configured model and want a workflow, prompts and a reading checklist |
| [04_TRAINING_PATH.md](handbook/04_TRAINING_PATH.md) | you want a curriculum: four levels with readings, exercises and self-checks |
| [05_GLOSSARY.md](handbook/05_GLOSSARY.md) | a term stops you |
| [06_FAQ_AND_TROUBLESHOOTING.md](handbook/06_FAQ_AND_TROUBLESHOOTING.md) | something does not work: versions, hashes, context size, a model that skips the gate |
| [07_MAINTAINERS_GUIDE.md](handbook/07_MAINTAINERS_GUIDE.md) | you change a file in the repository |
| [modules/](handbook/modules/README.md) | you need one framework document explained: purpose, when it applies, procedure, output, pitfalls |

## Other material

- [`ArXiv_Abstract_TE.md`](ArXiv_Abstract_TE.md): the abstract of the framework paper.
- [`../papers/`](../papers/collapse_equation/README.md): *The Collapse Equation* and *The Direction Problem*.
- [`../ECOSYSTEM.md`](../ECOSYSTEM.md): the five repositories of the programme and how they connect.

## Conventions

The handbook is a guide to the canonical texts, not a substitute for them: where the handbook and a framework document differ, the framework document is right and the handbook has a defect (open an issue). A reference such as `TE_BOOTLOADER §2.5` points to a numbered section of a canonical file in `FRAMEWORKS/`. Grades are written S₀–S₃ as in the texts; on a plain keyboard S0–S3 means the same thing.
