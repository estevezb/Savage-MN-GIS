# read_notebook.py
import json

filename = "US_tornados_analysis.ipynb"
with open(filename, encoding="utf-8", errors="replace") as f:
    nb = json.load(f)

# Print out the cell sources for inspection
for i, cell in enumerate(nb.get("cells", [])):
    if cell.get("cell_type") == "code":
        print(f"Cell {i} source:")
        print("".join(cell.get("source", [])))
        print("-" * 40)