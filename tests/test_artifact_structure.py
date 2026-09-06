import json
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]


def test_context_definitions():
    d = json.loads((ROOT / "rules/contexts.json").read_text(encoding="utf-8"))
    assert d["decision_threshold_percent"] == 65
    assert len(d["contexts"]) == 3
    for c in d["contexts"]:
        assert set(c["parameters"]) == {"phase", "criticality", "deadline", "team_size", "budget"}


def test_ecore_files_are_well_formed_xml():
    for name in ("electrical.ecore", "software.ecore", "production.ecore"):
        ET.parse(ROOT / "metamodels" / name)
