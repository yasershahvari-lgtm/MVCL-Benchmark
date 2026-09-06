import json
from pathlib import Path

class ToleranceEvaluator:
    @staticmethod
    def evaluate_file(path: str):
        data = json.loads(Path(path).read_text(encoding="utf-8"))
        cases = data["cases"]
        matches = sum(bool(c["accuracy_match"]) for c in cases)
        identical = sum(bool(c["identical_across_all_runs"]) for c in cases)
        total = len(cases)
        return {
            "accuracy": matches/total if total else 0.0,
            "consistency": identical/total if total else 0.0,
            "matches": matches,
            "mismatches": total-matches,
            "identical_cases": identical,
            "non_identical_cases": total-identical,
        }
