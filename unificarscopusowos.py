import pandas as pd
import matplotlib.pyplot as plt
# Renombrar las columnas en df_wos para que coincidan con las de df_scopus
'''df_wos_renombrado = df_wos.rename(columns={
    'Article Title': 'Title',
    'Source Title': 'Source title',
    'Publication Year': 'Year',
    'Cited Reference Count': 'Cited by',
    'Keywords Plus': 'Index Keywords',
    'Addresses': 'Authors with affiliations',
    'DOI Link': 'Link'
})'''


# Rutas a los archivos de Excel
archivo_excel_scopus = 'G:\\Mi unidad\\2024\\Msc. Jorge Vinueza\\_1908scopusalid.xlsx'
archivo_excel_wos = 'G:\\Mi unidad\\2024\\Msc. Jorge Vinueza\\_final833savedrecsalid.xlsx'

# Cargar los archivos de Excel
df_scopus = pd.read_excel(archivo_excel_scopus)
df_wos = pd.read_excel(archivo_excel_wos)
# Conteos iniciales
total_scopus = df_scopus.shape[0]
total_wos = df_wos.shape[0]
# Extraer y limpiar el número de citas para Scopus y WOS
df_scopus['citations_scopus'] = df_scopus['note'].str.extract(r'Cited by: (\d+)')
df_scopus['citations'] = pd.to_numeric(df_scopus['citations_scopus'], errors='coerce').fillna(0).astype(int)
df_wos['citations_wos'] = pd.to_numeric(df_wos['number-of-cited-references'], errors='coerce').fillna(0).astype(int)

# Convertir el título a mayúsculas para ambos DataFrames
df_scopus['title'] = df_scopus['title'].str.upper()
df_wos['title'] = df_wos['title'].str.upper()
# Normalizar el título reemplazando comillas curvas con comillas simples y convertir a mayúsculas
df_scopus['title'] = df_scopus['title'].str.replace("’", "'").str.upper()
df_wos['title'] = df_wos['title'].str.replace("’", "'").str.upper()

# Limpiar el campo 'issn' quitando el guion
df_scopus['issn'] = df_scopus['issn'].str.replace('-', '', regex=False)
df_wos['issn'] = df_wos['issn'].str.replace('-', '', regex=False)

# Seleccionar las columnas relevantes para la comparación
columns_to_select = ['title', 'abstract', 'journal', 'year', 'doi', 'language', 'issn' ]

# Preparar los DataFrames
df_scopus_selected = df_scopus[columns_to_select + ['citations_scopus']]
df_wos_selected = df_wos[columns_to_select + ['citations_wos']]

# Unir ambos DataFrames
combined_df = pd.concat([df_scopus_selected, df_wos_selected], ignore_index=True)

# Ordenar por 'title' para que los duplicados estén uno al lado del otro
combined_df.sort_values(by='title', inplace=True)

# Total combinado antes de identificar duplicados
total_combinado = total_scopus + total_wos

# Total de registros eliminados (asumiendo que todos los duplicados se eliminan)

# Identificar duplicados basados en 'title' antes de la consolidación
duplicados_antes_consolidacion = combined_df.duplicated(subset=['title'], keep=False)
total_duplicados = duplicados_antes_consolidacion.sum()

# Función para consolidar la información de registros duplicados
def consolidate_duplicates(group):
    consolidated = group.iloc[0].copy()  # Empezar con la primera fila del grupo y hacer una copia para evitar SettingWithCopyWarning
    # Tomar el primer 'issn' no NaN si está disponible, de lo contrario None
    consolidated['issn'] = group['issn'].dropna().iloc[0] if group['issn'].notna().any() else None
    # Asegurar que todos los valores nulos sean tratados como 0 antes de la suma
    consolidated['citations_scopus'] = group['citations_scopus'].fillna(0).astype(int).sum()
    consolidated['citations_wos'] = group['citations_wos'].fillna(0).astype(int).sum()
    return consolidated

# Aplicar la consolidación a los registros duplicados basados en 'title'
df_consolidado = combined_df.groupby('title', as_index=False).apply(consolidate_duplicates).reset_index(drop=True)
total_final = df_consolidado.shape[0]

# Esto asume que cada título duplicado se contó dos veces en total_duplicados
total_eliminados = (total_scopus + total_wos) - total_final - (total_duplicados)
total_eliminados= total_eliminados*-1
# Total final después de consolidar duplicados
total_final = df_consolidado.shape[0]
# Añadir una columna para comparar el número de citas de Scopus y WOS
df_consolidado['most_cited'] = df_consolidado.apply(
    lambda row: 'Scopus' if row['citations_scopus'] > row['citations_wos'] else ('WOS' if row['citations_wos'] > row['citations_scopus'] else 'Equal'),
    axis=1
)


# Datos para el gráfico
conteos = [total_scopus,total_wos, total_duplicados,total_eliminados, total_final]
etiquetas = ['total_scopus','total_wos', 'Duplicados','Eliminados', 'Total Final']

# Crear el gráfico de barras
plt.figure(figsize=(10, 6))
plt.bar(etiquetas, conteos, color=['blue', 'orange', 'green'])

# Añadir título y etiquetas para el eje Y
plt.title('Conteo de Artículos a lo largo de la Consolidación')
plt.ylabel('Número de Artículos')

# Mostrar valores en las barras
for i, valor in enumerate(conteos):
    plt.text(i, valor, str(valor), ha='center', va='bottom')

# Mostrar el gráfico
plt.tight_layout()
plt.show()
# Guardar el DataFrame consolidado en un nuevo archivo Excel
output_file = 'G:\\Mi unidad\\2024\\Msc. Jorge Vinueza\\consolidadofinal.xlsx'
df_consolidado.to_excel(output_file, index=False)

print(f"El archivo consolidado ha sido guardado como {output_file}.")