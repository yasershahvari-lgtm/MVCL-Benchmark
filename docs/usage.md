# Usage Guide

## Installation

```bash
python -m venv venv
venv\Scripts\activate
# Linux/macOS: source venv/bin/activate
pip install -r requirements.txt
pip install -e .
```

## Validate the bundled artifacts

```bash
python scripts/validate_artifacts.py
python -m pytest tests/
```

## Benchmark metadata generation

```bash
python scripts/run_benchmark.py generate --generate-all
```

The Python generator creates lightweight benchmark manifest files for the declared configurations. These manifests are not a replacement for the Eclipse MVCL/Xtext/EVL execution pipeline used to obtain the manuscript's detector results.

## Detection artifact workflow

The intended research workflow is:

`Ecore → Xtext scope/linking → MVCL validation → EVL execution → JSON violation adapter → metric computation`

The publication-level detection summaries are stored under `results/detection/`.

## Tolerance evaluation

```bash
python scripts/run_benchmark.py tolerance --context prototype-phase
python scripts/run_benchmark.py tolerance --context production-phase
python scripts/run_benchmark.py tolerance --context maintenance-phase
```

The representative decision is taken from `run_index=0`. Consistency is evaluated at case level over all 10 thresholded runs. The fixed operational threshold is 65%.

## Tolerance contexts

The context definitions are stored in `rules/contexts.json`. They include phase, criticality, deadline, team size, and budget for the three evaluated lifecycle contexts.

## Eclipse integration

Import the standard `.ecore` metamodels from `metamodels/`. Configure the MVCL/Xtext project with the compact rule specifications under `rules/`, resolve cross-model references through the scope/linking layer, execute the EVL validation pipeline, and serialize typed violations into the JSON representation used by the result artifacts.
