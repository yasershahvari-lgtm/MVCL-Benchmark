# Ground-Truth and Reference Manifests

The `*_ground_truth.json` files provide the benchmark-level reference configuration used to index each experiment: realized model size, number of rules, and mutation-case count.

The detection result summaries under `results/detection/metrics/` provide the archived TP/FP/FN aggregates used in the manuscript. The tolerance reference labels are preserved at case level under `results/tolerance/raw/` and are generated from the policy-based tolerance oracle described in the manuscript.
