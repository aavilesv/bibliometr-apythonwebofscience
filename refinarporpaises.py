import pandas as pd
import re

# Cargar los archivos
df_wos = pd.read_excel('C:\\Investigación\\Trabajo_2023\Codificaciones\\archivo_unidoprivadaspublicas.xlsx')

# Lista de países de Latinoamérica
paises_latinoamerica = [
    'Argentina', 'Bolivia','brazil', 'Chile', 'Colombia', 'Costa Rica', 
    'Cuba', 'Ecuador', 'El Salvador', 'Guatemala', 'Honduras', 'MEXICO', 
    'Nicaragua', 'Panama', 'Paraguay', 'peru', 'Puerto Rico', 'Republica Dominicana', 
    'Uruguay', 'Venezuela'
]

mask = pd.Series([False] * len(df_wos))
for pais in paises_latinoamerica:
    affiliation_mask = df_wos['affiliation'].str.contains(pais, case=False)
    affiliations_mask = df_wos['affiliations'].str.contains(pais, case=False)
    
    mask |= affiliation_mask | affiliations_mask

df_containstotal = df_wos[mask]

# Eliminar filas duplicadas
df_containstotal = df_containstotal.drop_duplicates()
df_containstotal.to_excel('universidades_latinoamerica1.xlsx', index=False)
print('final')
