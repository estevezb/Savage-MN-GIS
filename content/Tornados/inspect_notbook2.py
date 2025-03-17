import json

filename = "US_tornados_analysis.ipynb"

with open(filename, "r", encoding="utf-8", errors="replace") as f:
    nb = json.load(f)

with open(filename, "w", encoding="utf-8") as f:
    json.dump(nb, f, indent=2)