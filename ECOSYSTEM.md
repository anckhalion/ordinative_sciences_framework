# Ordinative Sciences Ecosystem Map

This file explains how the three public repositories connect.

## Three Repositories, Three Roles

| Repository | Role | Function |
| --- | --- | --- |
| `ordinative_sciences_framework` | Theory | Defines TE foundations, ontology, and full module architecture. |
| `te-ordinative-lora` | Practice | Implements TE principles in model fine-tuning workflows. |
| `te-oct-framework-en` | Validation | Publishes the English OCT corpus with reproducibility assets and benchmarks. |

## Conceptual Flow

1. Theory (`ordinative_sciences_framework`) defines the principles.
2. Practice (`te-ordinative-lora`) applies the principles in training pipelines.
3. Validation (`te-oct-framework-en`) documents and tests formal/empirical consistency.

## ASCII Map

```text
                ORDINATIVE SCIENCES ECOSYSTEM
                          |
      -----------------------------------------------
      |                     |                       |
      v                     v                       v
  THEORY                PRACTICE                VALIDATION
  ordinative_           te-ordinative-          te-oct-
  sciences_framework    lora                    framework-en
      |                     |                       |
      |---- provides -----> |                       |
      |                     | ---- tested by -----> |
      | <------- informs refinements ------------- |
```

## Suggested Reading Order

1. `ordinative_sciences_framework`
2. `te-ordinative-lora`
3. `te-oct-framework-en`
