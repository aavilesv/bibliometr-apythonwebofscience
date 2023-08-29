import openpyxl
from bibtexparser.bibdatabase import BibDatabase
from bibtexparser import dump

archivo_excel = 'C:\\Investigación\\Trabajo_2023\\Codificaciones\\archivo_unidoprivadaspublicas.xlsx'
archivo_bib = 'C:\\Investigación\\Trabajo_2023\\Codificaciones\\archivofinalprivadas.bib'

# Leer el archivo Excel
entradas = []
wb = openpyxl.load_workbook(archivo_excel)
hoja = wb.active
filas = list(hoja.iter_rows(values_only=True))

# Obtener los encabezados (nombres de las columnas) del archivo Excel
encabezados = [campo.strip() for campo in filas[0]]

for index, fila in enumerate(filas[1:], start=1):
    datos = dict(zip(encabezados, fila))
    # Convertir cada fila en una entrada BibTeX
    entrada = {'ENTRYTYPE': datos.get('ENTRYTYPE', 'article')}  # Ajusta esto según el tipo de entrada
    for campo, valor in datos.items():
        if valor:  # Solo agregar campos que no estén vacíos
            entrada[campo.lower()] = str(valor)  # Convertir todos los valores a cadenas
    entrada['ID'] = datos.get('ID', f"entry{index}")  # Usar el ID del archivo Excel o generar uno basado en el número de fila
    entradas.append(entrada)

# Crear un objeto BibDatabase con las entradas
bib_database = BibDatabase()
bib_database.entries = entradas

# Guardar las entradas en un archivo BibTeX
with open(archivo_bib, 'w', encoding='utf-8') as archivo:
    dump(bib_database, archivo)

print(f"El archivo BibTeX ha sido guardado en {archivo_bib}.")
