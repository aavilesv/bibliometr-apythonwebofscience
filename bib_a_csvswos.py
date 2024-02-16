import bibtexparser
from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bibdatabase import BibDatabase
 

archivo_bib = 'G:\\Mi unidad\\2024\\Msc. Jorge Vinueza\\final833savedrecsalid.bib'
archivo_csv = 'G:\\Mi unidad\\2024\\Msc. Jorge Vinueza\\final833savedrecsalid.csv'

with open(archivo_bib, 'r', encoding='utf-8') as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file)

# Obtener todos los campos posibles de las entradas para asegurarse de que el CSV tenga todas las columnas necesarias
campos = set()
for entrada in bib_database.entries:
    campos.update(entrada.keys())
campos.discard('ID')  # No necesitamos 'ID' porque lo manejaremos aparte

# Preparar el archivo CSV para la escritura
with open(archivo_csv, 'w', newline='', encoding='utf-8') as archivo_csv:
    writer = csv.DictWriter(archivo_csv, fieldnames=['ID'] + sorted(list(campos)), quoting=csv.QUOTE_ALL)
    writer.writeheader()  # Escribir la fila de encabezado
    
    for entrada in bib_database.entries:
        # Procesar el ID para eliminar el prefijo 'WOS:'
        entrada['ID'] = entrada['ID'].replace('WOS:', '')
        # Reemplazar saltos de línea dentro de los valores de los campos
        for campo, valor in entrada.items():
            if isinstance(valor, str):
                entrada[campo] = valor.replace('\n', ' ').replace('\r', ' ')
        writer.writerow(entrada)

print(f"El archivo CSV ha sido guardado en {archivo_csv}")
