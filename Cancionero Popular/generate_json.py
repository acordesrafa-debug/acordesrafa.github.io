import csv
import json

path = r"c:\Users\rafae\Downloads\Google_AI_Pruebas\acordes_rafa_web\Cancionero Popular\Lista de canciones.csv"

# Mapping PDF files
pdf_files = [
    "A Mi Manera(Vicente Fernandez)10051.pdf", "Aint No Sunshine(Bill Withers)10009.pdf",
    "Almohada(José José)10007.pdf", "Amigo(Roberto Carlos)10024.pdf",
    "Amor Eterno(Juan Gabriel)10014.pdf", "Amor del Bueno(Reyli Barba)10042.pdf",
    "Arrullo de Estrellas(Zoé)10030.pdf", "Cama y Mesa(Roberto Carlos)10004.pdf",
    "Canción Para Tí(Frank Quintero)10056.pdf", "Canción de Otoño(José Luis Perales)10001.pdf",
    "Chasing Cars(Snow Patrol)10046.pdf", "Cielo(Benny Ibarra)10035.pdf",
    "Como Dueles en los Labios(Maná)10058.pdf", "Costumbres(Roberto Carlos)10071.pdf",
    "Counting Blue Cars(Dishwalla)10019.pdf", "Creo en Ti(Reik)10040.pdf",
    "Cuando Nadie Me Ve(Alejandro Sanz)10031.pdf", "De Corazón a Corazón(Roberto Carlos)10002.pdf",
    "Demons(Imagine Dragons)10044.pdf", "Días de Junio(Yordano)10057.pdf",
    "Eden(Hooverphonic)10016.pdf", "El día que me quieras(Roberto Carlos)10037.pdf",
    "Eres(Alejandro Fernández)10045.pdf", "Fantasmas(Humbe)10072.pdf",
    "Feel(Robbie Williams)10017.pdf", "Fluorescent Adolescent(Arctic Monkeys)10012.pdf",
    "Fotografía(Juanes)10039.pdf", "Gotas de Fuego(José José)10008.pdf",
    "Hoy Tengo Ganas de Tí(Miguel Gallardo)10052.pdf", "La Condena(Elefante)10034.pdf",
    "La Mujer que Amo(Roberto Carlos)10029.pdf", "La Puerta Azul(Maná)10025.pdf",
    "La Que Me Gusta(Los Amigos Invisibles)10018.pdf", "Labios Rotos(Zoé)10049.pdf",
    "Llorona(Angela Aguilar)10021.pdf", "Mariposa Traicionera(Maná)10041.pdf",
    "Mi Novia Se Me Está Poniendo Vieja(Ricardo Arjona)10048.pdf", "Mi Verdad (Maná &Shakira)10003.pdf",
    "Nada(Zoé)10050.pdf", "Never Tear Us Apart(INXS)10032.pdf",
    "No Me Destruyas(Zoé)10028.pdf", "No Te Apartes de Mí(Vicentico)10047.pdf",
    "Para Empezar(Leonel García)10043.pdf", "Para Que Tú No Llores(Antonio Carmona)10023.pdf",
    "Perdón(Vicente&Alejandro Fernandez)10010.pdf", "Piel Canela(CUCO)10026.pdf",
    "Piensa en Mí(Liran Roll)10013.pdf", "Por Amor(Roberto Carlos)10000.pdf",
    "Pupilas Lejanas(Los Pericos)10062.pdf", "Que Lloro(Sin Bandera)10054.pdf",
    "Rayando el Sol(Maná)10060.pdf", "Recuerdas(Leonel García)10063.pdf",
    "Reloj Cucú(Maná)10059.pdf", "Rock and Roll(La Gusana CIega)10064.pdf",
    "San Miguel(La Gusana Ciega)10006.pdf", "Siempre Me Quedará(BEBE)10011.pdf",
    "Sin Cadenas(Los Pericos)10038.pdf", "Sin Ti(Benny Ibarra)10036.pdf",
    "Stop Crying Your Heart Out(Oasis)10015.pdf", "Tabaco y Chanel(Bacilos)10055.pdf",
    "Te Quiero(Hombres G)10033.pdf", "Un Día Normal(Juanes)10053.pdf",
    "Un Gato en la Obscuridad(Roberto Carlos)10027.pdf", "Vamos a darnos tiempo(José José)10020.pdf",
    "Yo Nací Para Amarte(Alejandro Fernández)10005.pdf", "Yo Te Propongo(Roberto Carlos)10061.pdf",
    "You have been loved(George Michael)10073.pdf"
]

def clean_song_name(name):
    # Remove things in parenthesis like (Vicente Fernandez) and the number at the end
    import re
    cleaned = re.sub(r'\(.*?\)', '', name)
    cleaned = re.sub(r'\d+$', '', cleaned)
    return cleaned.strip()

populares = {}

with open(path, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)
    for row in reader:
        if len(row) < 6: continue
        titulo = row[1].strip()
        pdf_name_part = row[4].strip()
        tutorial = row[2].strip()
        cover = row[5].strip()
        
        if not pdf_name_part: continue
        
        # Match with actual PDF file
        matching_pdf = None
        for p in pdf_files:
            if pdf_name_part in p:
                matching_pdf = p
                break
        
        if matching_pdf:
            # Display name without the ID number for cleaner list
            display_name = titulo if titulo else clean_song_name(pdf_name_part)
            populares[display_name] = {
                "pdf": matching_pdf,
                "tutorial": tutorial,
                "cover": cover
            }

print(json.dumps(populares, indent=4))
