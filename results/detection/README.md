# Detection Results

The JSON files in this directory are the publication-level result summaries corresponding to Table 3 of the manuscript.

- `B-100_*`, `B-500_*`, and `B-1000_*` report family-level and aggregate detection results.
- `metrics/pooled_metrics.json` reports the micro/count-based aggregation across the three detection-oriented configurations (90 ground-truth cases).
- B-COMP is used for execution-cost characterization and is therefore represented under `results/performance/` rather than as a separate accuracy table.

The detector outputs summarize the recorded TP/FP/FN counts; the package does not claim to reconstruct unavailable case-level Eclipse execution traces from these summaries.
