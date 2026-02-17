import csv
import json
import os

path = r"c:\Users\rafae\Downloads\Google_AI_Pruebas\acordes_rafa_web\Cancionero Popular\Lista de canciones.csv"
output_json = r"c:\Users\rafae\Downloads\Google_AI_Pruebas\acordes_rafa_web\songs_data.json"

def detect_delimiter(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        head = f.readline()
        if ';' in head: return ';'
        if ',' in head: return ','
        return ','

delim = detect_delimiter(path)

results = []
try:
    with open(path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=delim)
        header = next(reader)
        for row in reader:
            if len(row) > 5:
                # User's columns: C=2 (Tutorial), E=4 (Name), F=5 (Cover)
                name = row[4].strip()
                tutorial = row[2].strip()
                cover = row[5].strip()
                if name:
                    results.append({
                        "name": name,
                        "tutorial": tutorial,
                        "cover": cover
                    })
    
    with open(output_json, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=4)
        
    print(f"SUCCESS: Saved {len(results)} songs to {output_json}")
except Exception as e:
    with open(output_json, 'w', encoding='utf-8') as f:
        f.write(f"ERROR: {str(e)}")
    print(f"FAILED: {str(e)}")
