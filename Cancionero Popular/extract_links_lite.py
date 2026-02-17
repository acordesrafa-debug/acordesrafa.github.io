import zipfile
import xml.etree.ElementTree as ET
import json
import os

def get_links():
    try:
        if not os.path.exists('Lista de canciones.xlsx'):
            print("ERROR: File not found")
            return
            
        with zipfile.ZipFile('Lista de canciones.xlsx', 'r') as zip_ref:
            # Shared strings are usually in xl/sharedStrings.xml
            with zip_ref.open('xl/sharedStrings.xml') as f:
                tree = ET.parse(f)
                root = tree.getroot()
                # Shared strings are in <t> elements
                strings = [t.text for t in root.iter('{http://schemas.openxmlformats.org/spreadsheetml/2006/main}t')]
                
            # Now we need to find which string is what. 
            # This is hard without parsing the sheets, but let's just print all links found.
            links = [s for s in strings if s and ('http' in s or 'youtu' in s)]
            print("LINKS_FOUND:")
            print(json.dumps(links, indent=2))
            
            # Let's try to find potential song titles too (strings that are not links)
            # This is too much fuzzy logic, better to just show the links to the agent.
    except Exception as e:
        print("ERROR:", e)

get_links()
