import bibtexparser

archivo_bib = 'C:\\Investigación\\Trabajo_2023\\Codificaciones\\archivo_unico.bib'

with open(archivo_bib, 'r', encoding='utf-8') as archivo:
    bib_database = bibtexparser.load(archivo)

claves_vistas = set()
claves_duplicadas = set()

for entrada in bib_database.entries:
    clave = entrada['ID']
    if clave in claves_vistas:
        claves_duplicadas.add(clave)
    claves_vistas.add(clave)

print(f"Se encontraron {len(claves_duplicadas)} entradas duplicadas:")
for clave in claves_duplicadas:
    print(f"Clave duplicada: {clave}")
