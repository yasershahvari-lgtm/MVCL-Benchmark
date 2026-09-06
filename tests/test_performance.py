import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def test_performance_summary():
    d=json.loads((ROOT/"results/performance/summary/performance_summary.json").read_text())
    by={x["benchmark"]:x for x in d["configurations"]}
    assert by["B-1000"]["mean_detection_time_ms"]==1940.0
    assert by["B-COMP"]["mean_detection_time_ms"]==9787.0
    assert by["B-COMP"]["peak_memory_mb"]==1247
