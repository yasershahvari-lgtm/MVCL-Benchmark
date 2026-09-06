#!/usr/bin/env python3
"""Generate a compact JSON report from the bundled artifact summaries."""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load(rel):
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate an MVCL artifact summary report")
    parser.add_argument("-o", "--output", default="report.json", help="output path, relative to repository root unless absolute")
    args = parser.parse_args()
    out = Path(args.output)
    if not out.is_absolute():
        out = ROOT / out

    report = {
        "artifact_manifest": load("artifact_manifest.json"),
        "detection": load("results/detection/metrics/pooled_metrics.json"),
        "performance": load("results/performance/summary/performance_summary.json"),
        "tolerance": load("results/tolerance/summary/aggregate.json"),
    }
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
