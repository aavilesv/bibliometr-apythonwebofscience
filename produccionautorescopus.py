import pandas as pd

# Cargar los datos
df_wos = pd.read_excel('C:\\Investigación\\Trabajo_2023\\Codificaciones\\filtered_authors_scopus_final.xlsx')

# Separar los autores en una lista
df_wos['AutorList'] = df_wos['AutorFound'].str.split(';')

# Expandir la lista de autores en filas separadas
df_expanded = df_wos.explode('AutorList')
df_expanded['AutorList'] = df_expanded['AutorList'].str.strip()

# Contar cuántas veces aparece cada autor en el conjunto de datos
total_participations_by_author = df_expanded['AutorList'].value_counts()

# Guardar "df_expanded" en un archivo Excel
output_path_expanded = 'C:\\Investigación\\Trabajo_2023\\Codificaciones\\expanded_data_unemiscopus.xlsx'
df_expanded.to_excel(output_path_expanded, index=False)

# Guardar "total_participations_by_author" en otro archivo Excel
output_path_participations = 'C:\\Investigación\\Trabajo_2023\\Codificaciones\\total_participaciones_unemiscopus.xlsx'
total_participations_by_author.to_excel(output_path_participations, header=['Total Participations'])

print(f"Se guardó la información expandida en {output_path_expanded}")
print(f"Se guardó el conteo de participaciones en {output_path_participations}")
