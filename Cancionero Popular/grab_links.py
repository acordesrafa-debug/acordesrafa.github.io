import zipfile
import xml.etree.ElementTree as ET
import os

def run():
    path = "Lista de canciones.xlsx"
    output_file = "links_found.txt"
    
    if not os.path.exists(path):
        with open(output_file, 'w') as f: f.write("FILE_NOT_FOUND")
        return

    try:
        with zipfile.ZipFile(path, 'r') as zf:
            # Shared Strings
            strings = []
            try:
                with zf.open('xl/sharedStrings.xml') as f:
                    root = ET.parse(f).getroot()
                    for t in root.iter('{http://schemas.openxmlformats.org/spreadsheetml/2006/main}t'):
                        strings.append(t.text if t.text else "")
            except: pass

            # Sheet 1
            with zf.open('xl/worksheets/sheet1.xml') as f:
                root = ET.parse(f).getroot()
                
            with open(output_file, 'w', encoding='utf-8') as out:
                for row in root.iter('{http://schemas.openxmlformats.org/spreadsheetml/2006/main}row'):
                    cells = {}
                    for c in row.iter('{http://schemas.openxmlformats.org/spreadsheetml/2006/main}c'):
                        ref = c.get('r')
                        if not ref: continue
                        col = "".join(x for x in ref if x.isalpha())
                        
                        val = ""
                        v = c.find('{http://schemas.openxmlformats.org/spreadsheetml/2006/main}v')
                        if v is not None:
                            val = v.text
                            if c.get('t') == 's':
                                val = strings[int(val)]
                        cells[col] = val
                    
                    name = cells.get('E', '').strip()
                    tutorial = cells.get('C', '').strip()
                    cover = cells.get('F', '').strip()
                    
                    if name and (tutorial or cover):
                        out.write(f"{name}|{tutorial}|{cover}\n")
    except Exception as e:
        with open(output_file, 'w') as f: f.write(f"ERROR: {str(e)}")

run()
