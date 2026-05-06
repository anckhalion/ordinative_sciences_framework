# Ordinative Sciences Ecosystem Map

This file explains how the four public repositories connect.

## Four Repositories, Four Roles

| Repository | Role | Function |
| --- | --- | --- |
| `ordinative_sciences_framework` | Theory | Defines TE foundations, ontology, and full module architecture. |
| `te-ordinative-lora` | Practice | Implements TE principles in model fine-tuning workflows. |
| `te-oct-framework-en` | Validation | Publishes the English OCT corpus with reproducibility assets and benchmarks. |
| `te-ordinative-algebras-en` | Algebras | Publishes the SA (Semantic Algebra) and PA (Proportional Algebra) frameworks — the analytical operators and the proportional space they live in. |

## Conceptual Flow

1. Theory (`ordinative_sciences_framework`) defines the principles.
2. Practice (`te-ordinative-lora`) applies the principles in training pipelines.
3. Validation (`te-oct-framework-en`) documents and tests formal/empirical consistency.
4. Algebras (`te-ordinative-algebras-en`) provides the analytical operator-level grammar that connects theory, practice, and validation.

## ASCII Map

```text
                    ORDINATIVE SCIENCES ECOSYSTEM
                              |
      ----------------------------------------------------------
      |                |                  |                    |
      v                v                  v                    v
   THEORY           PRACTICE          VALIDATION             ALGEBRAS
   ordinative_      te-ordinative-    te-oct-                te-ordinative-
   sciences_        lora              framework-en           algebras-en
   framework
      |                |                  |                    |
      |                | <---- trains --- |                    |
      | <--- defines - |                  |                    |
      |                |                  | <--- formalises -- |
      | ----- provides invariants ------> |                    |
      |                                                        |
      | ---------------- analytical grammar --------------- >  |
```

## Suggested Reading Order

1. `ordinative_sciences_framework`
2. `te-ordinative-algebras-en`
3. `te-oct-framework-en`
4. `te-ordinative-lora`

## Note

The four repositories are designed to work together. Reading one in isolation can lead to incomplete understanding. The ordering above reflects a recommended sequence for new readers: foundations first, then formal operators, then validation cycles, then practical implementation.
