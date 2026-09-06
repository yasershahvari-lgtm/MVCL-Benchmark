import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def test_detection_metrics_all_primary_benchmarks():
    expected={
      "B-100":(27,2,3,0.931,0.900,0.915),
      "B-500":(26,3,4,0.897,0.867,0.881),
      "B-1000":(28,2,2,0.933,0.933,0.933),
    }
    for bid, exp in expected.items():
        d=json.loads((ROOT/"results"/"detection"/"metrics"/f"{bid}_metrics.json").read_text())
        a=d["aggregate"]
        assert tuple(a[k] for k in ("tp","fp","fn","precision","recall","f1"))==exp

def test_pooled_metrics():
    d=json.loads((ROOT/"results"/"detection"/"metrics"/"pooled_metrics.json").read_text())
    assert (d["tp"],d["fp"],d["fn"],d["precision"],d["recall"],d["f1"])==(81,7,9,0.920,0.900,0.910)
