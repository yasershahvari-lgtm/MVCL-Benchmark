#!/usr/bin/env python3
import json
import sys
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]

def load(rel):
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))

def require(cond, msg):
    if not cond:
        raise AssertionError(msg)

def main():
    # Metamodel XML well-formedness
    for name in ("electrical.ecore", "software.ecore", "production.ecore"):
        ET.parse(ROOT / "metamodels" / name)

    expected = {
        "B-100": (139, 30, 30),
        "B-500": (696, 30, 30),
        "B-1000": (1589, 30, 30),
        "B-TOL": (698, 30, 30),
        "B-COMP": (7959, 30, 30),
    }
    for bid, (elements, rules, cases) in expected.items():
        d = load(f"ground-truth/{bid}_ground_truth.json")
        require((d["realized_model_elements"], d["rules"], d["mutation_cases"]) == (elements, rules, cases), f"{bid} manifest mismatch")

    expected_det = {
        "B-100": (27,2,3,0.931,0.900,0.915),
        "B-500": (26,3,4,0.897,0.867,0.881),
        "B-1000": (28,2,2,0.933,0.933,0.933),
    }
    for bid, vals in expected_det.items():
        m = load(f"results/detection/metrics/{bid}_metrics.json")["aggregate"]
        require(tuple(m[k] for k in ("tp","fp","fn","precision","recall","f1")) == vals, f"{bid} detection mismatch")

    p = load("results/detection/metrics/pooled_metrics.json")
    require((p["tp"],p["fp"],p["fn"],p["precision"],p["recall"],p["f1"]) == (81,7,9,0.920,0.900,0.910), "pooled detection mismatch")

    perf = load("results/performance/summary/performance_summary.json")["configurations"]
    by_id={x["benchmark"]:x for x in perf}
    require(by_id["B-COMP"]["mean_detection_time_ms"] == 9787.0, "B-COMP runtime mismatch")
    require(by_id["B-COMP"]["peak_memory_mb"] == 1247, "B-COMP memory mismatch")

    contexts = load("rules/contexts.json")
    require(contexts["decision_threshold_percent"] == 65, "threshold mismatch")
    require({c["id"] for c in contexts["contexts"]} == {"prototype-phase","production-phase","maintenance-phase"}, "context ids mismatch")
    for c in contexts["contexts"]:
        for key in ("phase","criticality","deadline","team_size","budget"):
            require(key in c["parameters"], f"missing context parameter: {c['id']}:{key}")

    tol = load("results/tolerance/summary/aggregate.json")
    require((tol["overall"]["total_evaluated_cases"], tol["overall"]["total_matches"], tol["overall"]["total_identical_cases"]) == (75,65,64), "tolerance aggregate counts mismatch")
    require((tol["overall"]["overall_accuracy"],tol["overall"]["overall_consistency"]) == (0.867,0.853), "tolerance aggregate metrics mismatch")

    print("MVCL artifact validation: PASSED")
    return 0

if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"MVCL artifact validation: FAILED — {exc}", file=sys.stderr)
        raise SystemExit(1)
