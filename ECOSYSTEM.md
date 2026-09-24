# Ordinative Sciences Ecosystem Map

This file explains how the five public repositories connect.

## Five Repositories, Five Roles

| Repository | Role | Function |
| --- | --- | --- |
| `ordinative_sciences_framework` | Theory | Defines TE foundations, ontology, and full module architecture; hosts the domain frameworks LEXX (agreements) and CASEWORK (documentary audit and investigation) with their runtimes, under `FRAMEWORKS/`. |
| `te-ordinative-lora` | Practice | Implements TE principles in model fine-tuning workflows. |
| `te-oct-framework-en` | Validation | Publishes the English OCT corpus with reproducibility assets and benchmarks. |
| `te-ordinative-algebras-en` | Algebras | Publishes the SA (Semantic Algebra) and PA (Proportional Algebra) frameworks — the analytical operators and the proportional space they live in. |
| `te-controfase` | Treatise | Publishes *The Technology of Counter-phase, Vol. 1: Fondamenti* — the founding treatise of the Controfase operator — with its bilingual LoRA dataset. DOI [10.5281/zenodo.22542621](https://doi.org/10.5281/zenodo.22542621). |

## Conceptual Flow

1. Theory (`ordinative_sciences_framework`) defines the principles.
2. Practice (`te-ordinative-lora`) applies the principles in training pipelines.
3. Validation (`te-oct-framework-en`) documents and tests formal/empirical consistency.
4. Algebras (`te-ordinative-algebras-en`) provides the analytical operator-level grammar that connects theory, practice, and validation.
5. Treatise (`te-controfase`) publishes the founding text of the Controfase operator, which the always-active protocols implement.

## ASCII Map

```text
                         ORDINATIVE SCIENCES ECOSYSTEM
                                     |
      -------------------------------------------------------------------------
      |                |                  |                    |              |
      v                v                  v                    v              v
   THEORY           PRACTICE          VALIDATION             ALGEBRAS       TREATISE
   ordinative_      te-ordinative-    te-oct-                te-ordinative-  te-
   sciences_        lora              framework-en           algebras-en     controfase
   framework
      |                |                  |                    |              |
      |                | <---- trains --- |                    |              |
      | <--- defines - |                  |                    |              |
      |                |                  | <--- formalises -- |              |
      | ----- provides invariants ------> |                    |              |
      |                                                        |              |
      | ---------------- analytical grammar --------------- >  |              |
      | <---------------- founds the Controfase operator ---------------------|
```

## Suggested Reading Order

1. `ordinative_sciences_framework`
2. `te-ordinative-algebras-en`
3. `te-oct-framework-en`
4. `te-ordinative-lora`
5. `te-controfase`

## Note

The five repositories form one system: read them together. The order above is the sequence for a new reader: foundations first, then formal operators, then validation cycles, then practical implementation, then the treatise that founds the operator the protocols implement.
