from dataclasses import dataclass
from typing import Dict, List, Tuple
import random

@dataclass
class Violation:
    violation_id: str
    rule_id: str
    family: str
    element_ids: List[str]
    message: str

class BenchmarkDataGenerator:
    def __init__(self, seed: int = 42) -> None:
        self.seed = seed
        self.rng = random.Random(seed)

    def generate_benchmark_instance(
        self, size: int, complexity: str, inconsistency_density: float, realized_elements: int | None = None
    ) -> Dict:
        """Create a lightweight, deterministic benchmark manifest.

        This helper intentionally does not claim to recreate the Eclipse model instances or
        detector measurements used in the manuscript; those publication-level summaries are
        archived under results/.
        """
        if realized_elements is None:
            realized_elements = size
        elements = [
            {"id": f"element-{i:05d}", "kind": "synthetic", "active": True}
            for i in range(1, realized_elements + 1)
        ]
        return {
            "seed": self.seed,
            "requested_size": size,
            "realized_model_elements": realized_elements,
            "complexity": complexity,
            "inconsistency_density": inconsistency_density,
            "model_instances": elements,
            "rule_cases": [f"case-{i:02d}" for i in range(1, 31)],
        }
