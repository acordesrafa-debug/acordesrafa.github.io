import csv
import json

path = r"c:\Users\rafae\Downloads\Google_AI_Pruebas\acordes_rafa_web\Cancionero Popular\Lista de canciones.csv"

# Actual PDF files in the folder (as seen in list_dir)
pdf_files = [
    "A Mi Manera(Vicente Fernandez)10051.pdf", "Aint No Sunshine(Bill Withers)10009.pdf",
    "Almohada(José José)10007.pdf", "Amigo(Roberto Carlos)10024.pdf",
    "Amor Eterno(Juan Gabriel)10014.pdf", "Amor del Bueno(Reyli Barba)10042.pdf",
    "Amores Lejanos(Enanitos Verdes)10068.pdf", "Anhelante(Gualberto Ibarreto)10069.pdf",
    "Arrullo de Estrellas(Zoé)10030.pdf", "Baby Can I Hold You(Tracy Chapman)10065.pdf",
    "Cama y Mesa(Roberto Carlos)10004.pdf", "Canción de Otoño(José Luis Perales)10001.pdf",
    "Canción Para Tí(Frank Quintero)10056.pdf", "Chasing Cars(Snow Patrol)10046.pdf",
    "Cielo(Benny Ibarra)10035.pdf", "Como Dueles en los Labios(Maná)10058.pdf",
    "Costumbres(Roberto Carlos)10071.pdf", "Counting Blue Cars(Dishwalla)10019.pdf",
    "Creo en Ti(Reik)10040.pdf", "Cuando Nadie Me Ve(Alejandro Sanz)10031.pdf",
    "De Corazón a Corazón(Roberto Carlos)10002.pdf", "Demons(Imagine Dragons)10044.pdf",
    "Desde que llegaste(Reyli Barba)10067.pdf", "Días de Junio(Yordano)10057.pdf",
    "Eden(Hooverphonic)10016.pdf", "El día que me quieras(Roberto Carlos)10037.pdf",
    "Eres(Alejandro Fernández)10045.pdf", "Fantasmas(Humbe)10072.pdf",
    "Feel(Robbie Williams)10017.pdf", "Fluorescent Adolescent(Arctic Monkeys)10012.pdf",
    "Fotografía(Juanes)10039.pdf", "Gotas de Fuego(José José)10008.pdf",
    "Hoy Tengo Ganas de Tí(Miguel Gallardo)10052.pdf", "La Condena(Elefante)10034.pdf",
    "La Mujer que Amo(Roberto Carlos)10029.pdf", "La Puerta Azul(Maná)10025.pdf",
    "La Que Me Gusta(Los Amigos Invisibles)10018.pdf", "Labios Rotos(Zoé)10049.pdf",
    "Llorona(Angela Aguilar)10021.pdf", "Luz de Día(Enanitos Verdes)10066.pdf",
    "Mariposa Traicionera(Maná)10041.pdf", "Mi Novia Se Me Está Poniendo Vieja(Ricardo Arjona)10048.pdf",
    "Mi Verdad (Maná &Shakira)10003.pdf", "Nada(Zoé)10050.pdf", "Never Tear Us Apart(INXS)10032.pdf",
    "No Me Destruyas(Zoé)10028.pdf", "No Te Apartes de Mí(Vicentico)10047.pdf",
    "Para Empezar(Leonel García)10043.pdf", "Para Que Tú No Llores(Antonio Carmona)10023.pdf",
    "Perdón(Vicente&Alejandro Fernandez)10010.pdf", "Piel Canela(CUCO)10026.pdf",
    "Piensa en Mí(Liran Roll)10013.pdf", "Por Amor(Roberto Carlos)10000.pdf",
    "Pupilas Lejanas(Los Pericos)10062.pdf", "Que Lloro(Sin Bandera)10054.pdf",
    "Rayando el Sol(Maná)10060.pdf", "Recuerdas(Leonel García)10063.pdf",
    "Reloj Cucú(Maná)10059.pdf", "Rock and Roll(La Gusana CIega)10064.pdf",
    "Rue Vieille Du Temple (León Larregui)10070.pdf", "San Miguel(La Gusana Ciega)10006.pdf",
    "Siempre Me Quedará(BEBE)10011.pdf", "Sin Cadenas(Los Pericos)10038.pdf",
    "Sin Ti(Benny Ibarra)10036.pdf", "Stop Crying Your Heart Out(Oasis)10015.pdf",
    "Tabaco y Chanel(Bacilos)10055.pdf", "Te Quiero(Hombres G)10033.pdf",
    "Un Día Normal(Juanes)10053.pdf", "Un Gato en la Obscuridad(Roberto Carlos)10027.pdf",
    "Vamos a darnos tiempo(José José)10020.pdf", "Yo Nací Para Amarte(Alejandro Fernández)10005.pdf",
    "Yo Te Propongo(Roberto Carlos)10061.pdf", "You have been loved(George Michael)10073.pdf"
]

populares = {}

with open(path, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)
    for row in reader:
        if len(row) < 6: continue
        titulo = row[1].strip()
        pdf_base = row[4].strip()
        tutorial = row[2].strip()
        cover = row[5].strip()
        
        if not pdf_base: continue
        
        # Find actual PDF file name
        full_pdf = None
        for p in pdf_files:
            if pdf_base in p:
                full_pdf = p
                break
        
        if full_pdf:
            # Clean display name: remove (Vicente Fernandez) etc for the list
            import re
            display_name = re.sub(r'\(.*?\)', '', titulo).strip()
            # If after removal it's empty or the same, use titulo
            if not display_name: display_name = titulo
            
            populares[display_name] = {
                "pdf": full_pdf,
                "tutorial": tutorial,
                "cover": cover
            }

# Sort by name
populares = dict(sorted(populares.items()))

# Generate the JS code
js_lines = []
for name, data in populares.items():
    line = f'                "{name}": {{ pdf: "{data["pdf"]}", tutorial: "{data["tutorial"]}", cover: "{data["cover"]}" }},'
    js_lines.append(line)

print("\n".join(js_lines))
