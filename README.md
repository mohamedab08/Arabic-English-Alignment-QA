# Arabic-English Technical Translation & Localization Benchmark

An evaluation framework designed to audit dual-language Large Language Model (LLM) outputs for scientific accuracy, terminology consistency, and semantic fidelity between English and Modern Standard Arabic (MSA).

## Overview
- **Cross-Linguistic QA:** Evaluates AI translations of complex technical, biomedical, and scientific concepts to eliminate literal mistranslations.
- **MSA Terminology Validation:** Ensures proper usage of formal Arabic scientific nomenclature.
- **Automated Verification:** Features a Python validation script (`bilingual_validator.py`) to audit dataset schema and text encoding integrity.

## File Structure
- `translation_evals.json`: Bilingual prompt-response alignment records with expert linguistic audits.
- `bilingual_validator.py`: Automated Python verification tool for dataset structure checking.
