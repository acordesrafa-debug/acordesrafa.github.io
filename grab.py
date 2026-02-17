import zipfile
import xml.etree.ElementTree as ET
import os

path = r"c:\Users\rafae\Downloads\Google_AI_Pruebas\acordes_rafa_web\Cancionero Popular\Lista de canciones.xlsx"
out_path = r"c:\Users\rafae\Downloads\Google_AI_Pruebas\acordes_rafa_web\result.txt"

try:
    with zipfile.ZipFile(path, 'r') as z:
        ss = [t.text for t in ET.fromstring(z.read('xl/sharedStrings.xml')).iter('{http://schemas.openxmlformats.org/spreadsheetml/2006/main}t')]
        root = ET.fromstring(z.read('xl/worksheets/sheet1.xml'))
        ns = {'ns': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
        
        with open(out_path, 'w', encoding='utf-8') as f:
            for row in root.findall('.//ns:row', ns):
                cells = {}
                for cell in row.findall('ns:c', ns):
                    r = cell.get('r')
                    col = "".join(x for x in r if x.isalpha())
                    v_node = cell.find('ns:v', ns)
                    val = ""
                    if v_node is not None:
                        val = v_node.text
                        if cell.get('t') == 's':
                            val = ss[int(val)]
                    cells[col] = val
                
                name = cells.get('E', '')
                tutorial = cells.get('C', '')
                cover = cells.get('F', '')
                if name:
                    f.write(f"{name}|{tutorial}|{cover}\n")
    print("DONE_WRITING")
except Exception as e:
    with open(out_path, 'w') as f: f.write(str(e))
