#!/usr/bin/env python3
"""Summarize the publication-level MVCL result artifacts."""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    parser = argparse.ArgumentParser(description="Summarize archived MVCL results")
    parser.add_argument("--json", action="store_true", help="emit JSON")
    args = parser.parse_args()

    det = {
        bid: read_json(ROOT / "results" / "detection" / "metrics" / f"{bid}_metrics.json")["aggregate"]
        for bid in ("B-100", "B-500", "B-1000")
    }
    pooled = read_json(ROOT / "results" / "detection" / "metrics" / "pooled_metrics.json")
    perf = read_json(ROOT / "results" / "performance" / "summary" / "performance_summary.json")["configurations"]
    tol = read_json(ROOT / "results" / "tolerance" / "summary" / "aggregate.json")["overall"]

    report = {"detection": det, "pooled": pooled, "performance": perf, "tolerance": tol}
    if args.json:
        print(json.dumps(report, indent=2))
    else:
        print("MVCL detection results")
        for bid, a in det.items():
            print(f"{bid}: P={a['precision']:.3f}, R={a['recall']:.3f}, F1={a['f1']:.3f}")
        print(f"Pooled: P={pooled['precision']:.3f}, R={pooled['recall']:.3f}, F1={pooled['f1']:.3f}")
        print("\nPerformance")
        for row in perf:
            print(f"{row['benchmark']}: {row['mean_detection_time_ms']:.1f} ms, {row['peak_memory_mb']} MB")
        print(f"\nTolerance: accuracy={tol['overall_accuracy']:.3f}, consistency={tol['overall_consistency']:.3f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
