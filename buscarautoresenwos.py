import pandas as pd
import numpy as np

# Cargar los archivos
df_wos = pd.read_excel('C:\\Investigación\\Trabajo_2023\\Codificaciones\\data_2023.xlsx')

# Lista de afiliaciones para buscar
affiliations_to_search = [
    'UNIVERSIDAD ESTATAL DE MILAGRO',
    'UNIV ESTATAL MILAGRO',
    'UNIV ESTATAL MILAGROS',
    'UNEMI',
    'MILAGRO',
    'STATE UNIV MILAGRO',
    'UNIV ESTALAL MILAGRO UNEMI'
]

def extract_author_from_affiliation(affiliation):
    if "]" in affiliation:
        return affiliation.split("]")[0].replace("[", "").strip()
    return None

# Función para verificar si alguna afiliación de interés está en la lista de afiliaciones de un registro
def find_affiliation(record):
    affiliations = record.split(';')
    authors_found = []
    for affiliation in affiliations:
        if any(search in affiliation.upper() for search in affiliations_to_search):
            author = extract_author_from_affiliation(affiliation)
            if author:
                authors_found.append(author)
    if authors_found:
        return "; ".join(authors_found)  # Cambio el separador a ";"
    return np.nan  # Devuelve NaN si no hay coincidencia

# Aplicar la función a las columnas 'Addresses' para obtener los autores coincidentes
df_wos['AutorFound'] = df_wos['Addresses'].astype(str).apply(find_affiliation)

# Filtrar el DataFrame usando la nueva columna 'AutorFound' para obtener registros que tienen una coincidencia
df_filtered = df_wos.dropna(subset=['AutorFound'])

# Guardar el DataFrame filtrado en un nuevo archivo
output_path = 'C:\\Investigación\\Trabajo_2023\\Codificaciones\\filtered_autoresfinaless.xlsx'
df_filtered.to_excel(output_path, index=False)

print(f"Se guardó la información en {output_path}")
