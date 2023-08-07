import bibtexparser

archivo_bib = 'C:\\Investigación\\Trabajo_2023\\Codificaciones\\archivo_unic.bib'

with open(archivo_bib, 'r', encoding='utf-8') as archivo:
    bib_database = bibtexparser.load(archivo)

numero_de_articulos = len(bib_database.entries)

print(f"El número total de artículos en el archivo es {numero_de_articulos}.")
