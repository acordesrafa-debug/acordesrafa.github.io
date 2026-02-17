import zipfile
import xml.etree.ElementTree as ET
import os

def get_excel_data(file_path):
    if not os.path.exists(file_path):
        return "Error: File not found"

    try:
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            # 1. Load shared strings
            shared_strings = []
            try:
                with zip_ref.open('xl/sharedStrings.xml') as f:
                    tree = ET.parse(f)
                    root = tree.getroot()
                    for t in root.iter('{http://schemas.openxmlformats.org/spreadsheetml/2006/main}t'):
                        shared_strings.append(t.text if t.text else "")
            except KeyError:
                pass # No shared strings if all values are numeric or inline

            # 2. Load sheet1
            with zip_ref.open('xl/worksheets/sheet1.xml') as f:
                tree = ET.parse(f)
                root = tree.getroot()
                
                rows = []
                for row_elem in root.iter('{http://schemas.openxmlformats.org/spreadsheetml/2006/main}row'):
                    cells = {}
                    for cell_elem in row_elem.iter('{http://schemas.openxmlformats.org/spreadsheetml/2006/main}c'):
                        r = cell_elem.get('r') # e.g. "A1"
                        if not r: continue
                        col = ''.join([c for c in r if c.isalpha()])
                        
                        v_elem = cell_elem.find('{http://schemas.openxmlformats.org/spreadsheetml/2006/main}v')
                        if v_elem is not None:
                            val = v_elem.text
                            t = cell_elem.get('t')
                            if t == 's': # Shared string
                                val = shared_strings[int(val)]
                            cells[col] = val
                    rows.append(cells)
                return rows
    except Exception as e:
        return f"Error: {str(e)}"

# Path provided by user
path = r"c:\Users\rafae\Downloads\Google_AI_Pruebas\acordes_rafa_web\Cancionero Popular\Lista de canciones.xlsx"
data = get_excel_data(path)

if isinstance(data, list):
    print("EXTRACTED_START")
    for row in data:
        # User said: Col C (Tutorial), Col E (Name), Col F (Cover)
        name = row.get('E', '').strip()
        tutorial = row.get('C', '').strip()
        cover = row.get('F', '').strip()
        if name and (tutorial or cover):
            # Only print if we have a name and at least one link
            print(f"SONG|{name}|{tutorial}|{cover}")
    print("EXTRACTED_END")
else:
    print(data)
