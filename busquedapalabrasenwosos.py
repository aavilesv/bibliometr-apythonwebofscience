import pandas as pd

# Cargar el archivo
df1 = pd.read_excel('C:\\Investigación\\Trabajo_2023\\Codificaciones\\archivo_unidoprivadaspublicas.xlsx')

# Convertir las columnas relevantes a cadenas y reemplazar NaN por cadenas vacías
cols_to_convert = ['keywords', 'keywords-plus', 'title', 'abstract']
for col in cols_to_convert:
    df1[col] = df1[col].fillna('').astype(str)

# Crear una lista con las palabras de interés
palabras = ['Web of science','Scopus', 'Wos','Open Access','Scientific Production','bibliometric indicators','open science']

# Crear una función que verifica si una cadena de texto comienza, termina o contiene alguna de las palabras de interés
def contains_words(text):
    return pd.Series(text.split(';')).str.contains('|'.join([rf'\b{word}\b' for word in palabras]), case=False).any()

# Crear una función que verifica si una cadena de texto (no dividida) comienza, termina o contiene alguna de las palabras de interés
def contains_words_no_split(text):
    return pd.Series(text).str.contains('|'.join([rf'\b{word}\b' for word in palabras]), case=False).any()

# Aplicar la función a las columnas de interés
df_filtrado = df1[df1[['keywords', 'keywords-plus']].applymap(contains_words).any(axis=1) | df1[['title']].applymap(contains_words_no_split).any(axis=1)]

# Si deseas guardar el resultado en un archivo Excel
df_filtrado.to_excel('C:\\Investigación\\Trabajo_2023\\Dr. Patricio Alvarez\\Revista Información, cultura y sociedad\\ppalabrasresultadofinall.xlsx')
