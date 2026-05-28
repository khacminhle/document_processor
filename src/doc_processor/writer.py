from pathlib import Path
import json

def save_json(data: dict, output_path: Path):
  output_file = f"{output_path}.json"
  with open(output_file, "w", encoding="utf-8") as file:
    json.dump(data, file)

