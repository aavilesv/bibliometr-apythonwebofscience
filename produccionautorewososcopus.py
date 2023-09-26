import pandas as pd

# Cargar los datos
df_wos = pd.read_excel('C:\\Investigación\\Trabajo_2023\\Codificaciones\\filtered_autoresfinaless.xlsx')

# Separar los autores en una lista
df_wos['AutorList'] = df_wos['AutorFound'].str.split(';')

# Expandir la lista de autores en filas separadas
df_expanded = df_wos.explode('AutorList')
df_expanded['AutorList'] = df_expanded['AutorList'].str.strip()

# 1. Autores con más referencias
authors_references = df_expanded.groupby('AutorList')['Cited Reference Count'].sum().sort_values(ascending=False)
print("Autores con más referencias:")
print(authors_references.head(10))

# 2. Autores más relevantes (promedio de referencias por artículo)
authors_relevance = df_expanded.groupby('AutorList')['Cited Reference Count'].mean().sort_values(ascending=False)
print("\nAutores más relevantes:")
print(authors_relevance.head(10))

# 4. Producción de los autores a lo largo del tiempo
authors_production = df_expanded.groupby(['AutorList', 'Publication Year']).size().unstack().fillna(0)
print("\nProducción de los autores a lo largo del tiempo:")
print(authors_production.head(10))

# Total de artículos por autor
total_articles_by_author = df_expanded.groupby('AutorList')['Article Title'].nunique()
print("\nTotal de artículos por autor:")
print(total_articles_by_author.sort_values(ascending=False).head(10))

# Total de participaciones por autor
total_participations_by_author = df_expanded['AutorList'].value_counts()
print("\nTotal de participaciones por autor:")
print(total_participations_by_author.head(10))


# ... [tu código anterior]

# Guardar "total_participations_by_author" en un archivo Excel
output_path_participations = 'C:\\Investigación\\Trabajo_2023\\Codificaciones\\total_participaciones_unemiifinal.xlsx'
df_expanded.to_excel(output_path_participations)
