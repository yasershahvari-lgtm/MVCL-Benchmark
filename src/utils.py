import json
from pathlib import Path

def load_json(path: str):
    return json.loads(Path(path).read_text(encoding="utf-8"))

def save_json(path: str, data):
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, indent=2), encoding="utf-8")
