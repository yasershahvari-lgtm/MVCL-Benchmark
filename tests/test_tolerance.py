import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def test_aggregate():
    d=json.loads((ROOT/"results/tolerance/summary/aggregate.json").read_text())
    assert d["overall"]["total_evaluated_cases"]==75
    assert d["overall"]["total_matches"]==65
    assert d["overall"]["total_identical_cases"]==64
    assert d["overall"]["overall_accuracy"]==0.867
    assert d["overall"]["overall_consistency"]==0.853

def test_raw_context_files_match_summary():
    expected={"prototype_decisions.json":(25,19,19),"production_decisions.json":(25,23,22),"maintenance_decisions.json":(25,23,23)}
    for fn,(total,matches,identical) in expected.items():
        d=json.loads((ROOT/"results/tolerance/raw"/fn).read_text())
        cases=d["cases"]
        assert len(cases)==total
        assert sum(bool(c["accuracy_match"]) for c in cases)==matches
        assert sum(bool(c["identical_across_all_runs"]) for c in cases)==identical
        assert all(len(c["runs"])==10 for c in cases)
