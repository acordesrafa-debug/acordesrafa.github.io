import csv
import json

path = r"c:\Users\rafae\Downloads\Google_AI_Pruebas\acordes_rafa_web\Cancionero Popular\Lista de canciones.csv"

# Function to detect separator
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
        header = next(reader) # skip header
        for row in reader:
            if len(row) > 5:
                # E is index 4, C is index 2, F is index 5
                # Using indices based on user's column description (A=0, B=1, C=2, D=3, E=4, F=5)
                name = row[4].strip()
                tutorial = row[2].strip()
                cover = row[5].strip()
                if name:
                    results.append({
                        "name": name,
                        "tutorial": tutorial,
                        "cover": cover
                    })
    print("DATA_START")
    print(json.dumps(results))
    print("DATA_END")
except Exception as e:
    print(f"ERROR: {str(e)}")
