import json

def check_notebook_encoding(notebook_path):
    with open(notebook_path, 'r', encoding='utf-8', errors='replace') as f:
        try:
            notebook_content = json.load(f)
            print("Notebook loaded successfully.")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            return

        # Check each cell for non-UTF-8 characters
        for i, cell in enumerate(notebook_content.get('cells', [])):
            if cell['cell_type'] == 'code':
                source = ''.join(cell['source'])
                if not is_utf8(source):
                    print(f"Non-UTF-8 characters found in cell {i + 1}")

def is_utf8(text):
    try:
        text.encode('utf-8').decode('utf-8')
        return True
    except UnicodeDecodeError:
        return False

# Replace with the path to your notebook
notebook_path = r"C:\Projects\my_git_pages_website\Py-and-Sky-Labs\content\Tornados\US_tornados_analysis_v0.2.ipynb"
check_notebook_encoding(notebook_path)