import csv
from bibtexparser.bibdatabase import BibDatabase

archivo_csv = 'C:\\Investigación\\Trabajo_2023\\Codificaciones\\archivocsvfinal.csv'
archivo_bib = 'C:\\Investigación\\Trabajo_2023\\Codificaciones\\archivofinal.bib'

# Leer el archivo CSV
entradas = []
with open(archivo_csv, 'r', encoding='utf-8') as archivo:
    reader = csv.DictReader(archivo)
    for fila in reader:
        # Convertir cada fila en una entrada BibTeX
        entrada = {'ENTRYTYPE': 'article'}  # Ajusta esto según el tipo de entrada
        for campo, valor in fila.items():
            if campo != 'ID':  # La clave 'ID' se manejará por separado
                entrada[campo.lower()] = valor  # Convertir los nombres de los campos a minúsculas
        entrada['ID'] = fila['ID']
        entradas.append(entrada)

# Crear un objeto BibDatabase con las entradas
bib_database = BibDatabase()
bib_database.entries = entradas

# Guardar las entradas en un archivo BibTeX
with open(archivo_bib, 'w', encoding='utf-8') as archivo:
    bibtexparser.dump(bib_database, archivo)

print(f"El archivo BibTeX ha sido guardado en {archivo_bib}.")
