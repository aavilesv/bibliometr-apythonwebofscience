
import pandas as pd

# Constantes
RUTA_ARCHIVO_SCOPUS = 'C:\\Investigación\\Trabajo_2023\\Msc. Isabel Leal\\Búsqueda 1\\bibliometriascopusnew1csv.xlsx'
RUTA_ARCHIVO_FILTRADO = 'df_scopus_filtrado.xlsx'
#COLUMNAS_BUSQUEDA = ['abstract', 'affiliations', 'author_keywords', 'keywords', 'title']
COLUMNAS_BUSQUEDA = ['affiliations', 'author_keywords', 'keywords', 'title']
# Cargar el archivo de Scopus
df_scopus = pd.read_excel(RUTA_ARCHIVO_SCOPUS)

# Filtrar las columnas que realmente existen en el DataFrame
columnas_existentes = [col for col in COLUMNAS_BUSQUEDA if col in df_scopus.columns]

# Palabras clave para buscar en Scopus
palabras_scopus = [
    'bibliometrics', 'Bibliometric', 'Scopus', 'Visual analysis', 'Systematic literature review',
    'bibliometrix', 'biblioshby', 'Citation analysis', 'Content analysis', 'Publication trend',
    'Scientometrics', 'Informetrics', 'Heuristic evaluation', 'Heuristic analysis', 'Bibliometric mapping',
    'Co-citation analysis', 'Authorship pattern', 'heuristic method', 'heuristic approach', 'heuristic technique'
]


# Función de búsqueda
def search_for_word(word):
    def contains_word(text): 
        text = '' if pd.isnull(text) else text
        return word in text
    mask = df_scopus[columnas_existentes].applymap(contains_word).any(axis=1)
    return df_scopus[mask]

# Buscar cada palabra y concatenar los resultados
dfs_filtrados = [search_for_word(word) for word in palabras_scopus]
df_filtrado_scopus = pd.concat(dfs_filtrados).drop_duplicates()

# Extraer el número de citas y asignarlo a una nueva columna
df_filtrado_scopus['Cited_by'] = df_filtrado_scopus['note'].str.extract(r'Cited by: (\d+)').astype(float)

# Extraer la información de acceso abierto y asignarla a una nueva columna
df_filtrado_scopus['open_access'] = df_filtrado_scopus['note'].str.extract(r'(All Open Access, Gold Open Access, Green Open Access)')

# Guardar el DataFrame filtrado
df_filtrado_scopus.to_excel(RUTA_ARCHIVO_FILTRADO, index=False)
