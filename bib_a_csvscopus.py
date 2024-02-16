import bibtexparser
import csv
archivo_bib = 'G:\\Mi unidad\\2024\\Msc. Jorge Vinueza\\final833savedrecsalid.bib'
archivo_csv = 'G:\\Mi unidad\\2024\\Msc. Jorge Vinueza\\final833savedrecsalid.csv'
with open(archivo_bib, 'r', encoding='utf-8') as archivo:
    bib_database = bibtexparser.load(archivo)
# Obtener todos los campos posibles de las entradas para asegurarse de que el CSV tenga todas las columnas necesarias
campos = set()
for entrada in bib_database.entries:
    campos.update(entrada.keys())
campos.discard('ID')  # La clave 'ID' se manejará por separado
with open(archivo_csv, 'w', newline='', encoding='utf-8') as archivo:
    writer = csv.writer(archivo)
        # Escribir la fila de encabezado
    writer.writerow(['ID'] + sorted(list(campos)))
    # Escribir las entradas
    for entrada in bib_database.entries:
        fila = [entrada['ID']] + [entrada.get(campo, '') for campo in sorted(list(campos))]
        writer.writerow(fila)
print(f"El archivo CSV ha sido guardado en {archivo_csv}.")
