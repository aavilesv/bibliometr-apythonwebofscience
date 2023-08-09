import pandas as pd

# Cargar los archivos
df_scopus = pd.read_csv('C:\\Investigación\\Trabajo_2023\\Codificaciones\\batallasleon843scopuscsv.csv')
df_wos = pd.read_excel('C:\\Investigación\\Trabajo_2023\\Codificaciones\\batallasleonwos580.xlsx')

# Seleccionar las columnas relevantes
columnascopus = ['Authors', 'Title', 'Source title', 'Year', 'Cited by', 'Affiliations', 'Abstract', 'Author Keywords', 'Index Keywords','Document Type','Authors with affiliations','DOI','Link']
columnaswebofscience = ['Authors', 'Article Title', 'Source Title', 'Publication Year', 'Cited Reference Count', 'Affiliations', 'Abstract', 'Author Keywords', 'Keywords Plus','Document Type','Addresses','DOI','DOI Link']
df_scopus = df_scopus[columnascopus]
df_wos = df_wos[columnaswebofscience]
print(df_wos)
print(df_scopus)