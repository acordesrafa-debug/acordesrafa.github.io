import pandas as pd
import json

try:
    df = pd.read_excel('Lista de canciones.xlsx')
    # Assuming columns might be 'Nombre', 'Tutorial', 'Cover' or similar
    # Let's just print the columns first to be sure
    print("COLUMNS:", df.columns.tolist())
    # Convert to list of dicts
    data = df.to_dict(orient='records')
    print("DATA_START")
    print(json.dumps(data))
    print("DATA_END")
except Exception as e:
    print("ERROR:", e)
