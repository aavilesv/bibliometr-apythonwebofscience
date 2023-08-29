import pandas as pd

# Cargar el archivo de Scopus
df_scopus = pd.read_excel('C:\\Investigación\\Trabajo_2023\\Codificaciones\\archivo_scopus.xlsx')

# Ajusta estos valores según las categorías y palabras clave que quieras filtrar en Scopus
valores_scopus = ['Computer Science', 'Information Science', 'Technology', 'computacion de ciencias']
palabras_scopus = ['web application', 'website', 'evaluation', 'evaluate']

regex_scopus = r'^(.*\s)?(' + '|'.join(valores_scopus) + r')(\s.*)?$'
df_filtradoarea_scopus = df_scopus[df_scopus['categories_column_name'].str.split(';').apply(lambda x: any(pd.Series(x).str.contains(regex_scopus, case=False, na=False)))]

def contains_words_scopus(text): 
    text = '' if pd.isnull(text) else text
    return pd.Series(text.split(';')).str.contains('|'.join([rf'\b{word}\b' for word in palabras_scopus]), case=False, na=False).any()

def contains_words_no_split_scopus(text):
    text = '' if pd.isnull(text) else text
    return pd.Series(text).str.contains('|'.join([rf'\b{word}\b' for word in palabras_scopus]), case=False, na=False).any()

df_filtrado_scopus = df_filtradoarea_scopus[df_filtradoarea_scopus[['keywords_column_name', 'other_keywords_column_name']].applymap(contains_words_scopus).any(axis=1) | df_filtradoarea_scopus[['title_column_name', 'abstract_column_name']].applymap(contains_words_no_split_scopus).any(axis=1)]

# Guardar el DataFrame filtrado
df_filtrado_scopus.to_excel('df_scopus_filtrado.xlsx', index=False)
