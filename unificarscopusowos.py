import pandas as pd
import re
# Cargar los archivos
df_scopus = pd.read_csv('C:\\Investigación\\Trabajo_2023\\Codificaciones\\batallasleon843scopuscsv.csv')
df_wos = pd.read_excel('C:\\Investigación\\Trabajo_2023\\Codificaciones\\batallasleonwos580.xlsx')
# Función para limpiar texto: convertir a mayúsculas, eliminar caracteres especiales y espacios adicionales

# Seleccionar las columnas relevantes
columnascopus = ['Authors', 'Title', 'Source title', 'Year', 'Cited by', 'Affiliations', 'Abstract', 'Author Keywords', 'Index Keywords','Document Type','Authors with affiliations','DOI','Link']
columnaswebofscience = ['Authors', 'Article Title', 'Source Title', 'Publication Year', 'Cited Reference Count', 'Affiliations', 'Abstract', 'Author Keywords', 'Keywords Plus','Document Type','Addresses','DOI','DOI Link']
df_scopus = df_scopus[columnascopus]
df_wos = df_wos[columnaswebofscience]

# Renombrar las columnas en df_wos para que coincidan con las de df_scopus
df_wos_renombrado = df_wos.rename(columns={
    'Article Title': 'Title',
    'Source Title': 'Source title',
    'Publication Year': 'Year',
    'Cited Reference Count': 'Cited by',
    'Keywords Plus': 'Index Keywords',
    'Addresses': 'Authors with affiliations',
    'DOI Link': 'Link'
})


# Unir los DataFrames
df_unido = pd.concat([df_scopus, df_wos_renombrado], ignore_index=True)

# Convertir todo a mayúsculas
df_unido['Title'] = df_unido['Title'].str.upper()
df_unido['Source title'] = df_unido['Source title'].str.upper()

# Reemplazar caracteres especiales en la columna "Title"
df_unido['Title'] = df_unido['Title'].apply(lambda x: re.sub(r'[^A-Z0-9]+', ' ', x).strip())
df_unido['Source title'] = df_unido['Source title'].apply(lambda x: re.sub(r'[^A-Z0-9]+', ' ', x).strip())

# Identificar registros duplicados basados en la columna "Title"
repetidos_mask = df_unido.duplicated(subset=['Title'], keep='first')
df_repetidostitle = df_unido[repetidos_mask].sort_values(by='Title')
# Mantener la primera aparición de cada registro duplicado y eliminar las apariciones subsiguientes
df_unido = df_unido.drop_duplicates(subset=['Title'], keep='first').sort_values(by='Title')

# Encontrar los registros únicos, incluyendo la primera aparición de cada valor duplicado doi y revista
repetidos_mask = df_unido.duplicated(subset=['Year','Source title','DOI'], keep='first')
df_repetidosrevista = df_unido[repetidos_mask].sort_values(by='Title')
revistadoi = df_unido.drop_duplicates(subset=['Year','Source title','DOI'], keep='first').sort_values(by='Title')

revistadoi.to_csv('unicosfinal.csv', index=False)
# Imprimir la cantidad de registros en cada DataFrame
print("Cantidad de registros repetidos title(sin incluir la primera aparición):", len(df_repetidostitle))
print("Cantidad de registros repetidos revista(sin incluir la primera aparición):", len(df_repetidosrevista))
print("Cantidad de registros únicos (incluyendo la primera aparición de valores duplicados):", len(df_unido))
print("Cantidad de TOTAL (incluyendo la primera aparición de valores duplicados):", len(revistadoi))