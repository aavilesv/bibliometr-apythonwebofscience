

import pandas as pd

# Cargar los archivos
df_scopus = pd.read_csv('C:\\Investigación\\Trabajo_2023\\Codificaciones\\batallasleon843scopuscsv.csv')
df_wos = pd.read_excel('C:\\Investigación\\Trabajo_2023\\Codificaciones\\batallasleonwos580.xlsx')

# Seleccionar las columnas relevantes
columnascopus = ['Authors', 'Title', 'Source title', 'Year', 'Cited by', 'Affiliations', 'Abstract', 'Author Keywords', 'Index Keywords','Document Type','Authors with affiliations','DOI','Link']
columnaswebofscience = ['Authors', 'Article Title', 'Source Title', 'Publication Year', 'Cited Reference Count', 'Affiliations', 'Abstract', 'Author Keywords', 'Keywords Plus','Document Type','Addresses','DOI','DOI Link']
df_scopus = df_scopus[columnascopus]
df_wos = df_wos[columnaswebofscience]
# Convertir las columnas relevantes a mayúsculas
df_scopus['Title'] = df_scopus['Title'].str.upper()
df_scopus['Source title'] = df_scopus['Source title'].str.upper()
df_wos['Article Title'] = df_wos['Article Title'].str.upper()
df_wos['Source Title'] = df_wos['Source Title'].str.upper()


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

## Encontrar los registros repetidos, manteniendo solo la primera aparición de cada valor duplicado
repetidos_mask = df_unido.duplicated(subset=['Title'], keep='first')# subset debes poner las variables que deseas saber si se repiten
df_repetidos = df_unido[repetidos_mask]
# Encontrar los registros únicos, incluyendo la primera aparición de cada valor duplicado
df_unicos = df_unido[~df_unido.duplicated(subset=['Title'], keep=False)]

# Imprimir la cantidad de registros en cada DataFrame
print("Cantidad de registros repetidos (sin incluir la primera aparición):", len(df_repetidos))
print("Cantidad de registros únicos (incluyendo la primera aparición de valores duplicados):", len(df_unicos))