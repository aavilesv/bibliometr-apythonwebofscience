import pandas as pd
import numpy as np

# Cargar los archivos
df_scopus = pd.read_excel('C:\\Investigación\\Trabajo_2023\\Codificaciones\\data.xlsx')

# Lista de afiliaciones para buscar
affiliations_to_search = [
    'UNIVERSIDAD ESTATAL DE MILAGRO',
    'UNEMI'
]

# Función para verificar si alguna afiliación de interés está en la lista de afiliaciones de un registro
def find_affiliation(record, authors):
    affiliations = record.split(';')
    authors_list = authors.split(',')
    authors_found = []
    for idx, affiliation in enumerate(affiliations):
        if any(search in affiliation.upper() for search in affiliations_to_search):
            # Extraer el nombre del autor correspondiente de la columna "Authors"
            author = authors_list[idx].strip()
            authors_found.append(author)
    if authors_found:
        return "; ".join(authors_found)  # Cambio el separador a ";"
    return np.nan  # Devuelve NaN si no hay coincidencia

# Aplicar la función a las columnas 'Authors with affiliations' y 'Authors' para obtener los autores coincidentes
df_scopus['AutorFound'] = df_scopus.apply(lambda row: find_affiliation(row['Authors with affiliations'], row['Authors']), axis=1)

# Filtrar el DataFrame usando la nueva columna 'AutorFound' para obtener registros que tienen una coincidencia
df_filtered = df_scopus.dropna(subset=['AutorFound'])

# Guardar el DataFrame filtrado en un nuevo archivo
output_path = 'C:\\Investigación\\Trabajo_2023\\Codificaciones\\filtered_authors_scopus_final.xlsx'
df_filtered.to_excel(output_path, index=False)

