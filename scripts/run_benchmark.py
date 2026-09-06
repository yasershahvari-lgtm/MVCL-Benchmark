#!/usr/bin/env python3
import argparse, json, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from generator import BenchmarkDataGenerator

CONFIGS = [
    ("B-100", 100, "low", 0.10, 139),
    ("B-500", 500, "medium", 0.15, 696),
    ("B-1000", 1000, "high", 0.15, 1589),
    ("B-TOL", 500, "medium", 0.12, 698),
    ("B-COMP", 5000, "high", 0.20, 7959),
]

def main():
    p = argparse.ArgumentParser(description="MVCL benchmark artifact utility")
    s = p.add_subparsers(dest="command", required=True)
    g = s.add_parser("generate", help="generate lightweight benchmark manifests")
    g.add_argument("--generate-all", action="store_true")
    g.add_argument("--generate")
    g.add_argument("--seed", type=int, default=42)
    e = s.add_parser("evaluate", help="describe Eclipse-side evaluation workflow")
    e.add_argument("--evaluate-all", action="store_true")
    e.add_argument("--evaluate")
    t = s.add_parser("tolerance", help="describe tolerance-artifact evaluation")
    t.add_argument("--context", default="prototype-phase")
    a = p.parse_args()
    if a.command == "generate":
        targets = CONFIGS if a.generate_all else [c for c in CONFIGS if c[0] == a.generate]
        if not targets:
            p.error("Unknown benchmark")
        gen = BenchmarkDataGenerator(a.seed)
        for bid, size, comp, dens, realized in targets:
            manifest = gen.generate_benchmark_instance(size, comp, dens, realized_elements=realized)
            out = ROOT / "benchmarks" / bid
            out.mkdir(parents=True, exist_ok=True)
            (out / "generated_manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
            print(f"{bid}: generated manifest")
    elif a.command == "evaluate":
        print("Use the Eclipse MVCL/Xtext/EVL pipeline and archive detector outputs under results/detection/.")
    else:
        print(f"Tolerance context: {a.context}. See results/tolerance/ for archived thresholded decisions.")

if __name__ == "__main__":
    main()
