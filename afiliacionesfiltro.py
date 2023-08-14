import pandas as pd
import re
# Cargar los archivos
df_wos = pd.read_csv('C:\\Investigación\\Trabajo_2023\\Dr. Patricio Alvarez\\Revista Información, cultura y sociedad\\Dato\\archivocsvfinal.csv')

# Crear una nueva columna 'affiliations_modified' con los valores originales de 'affiliations'
df_wos['affiliations_modified'] = df_wos['affiliations']
# Convertir todo a mayúsculas
df_wos['affiliations_modified'] = df_wos['affiliations_modified'].astype(str)  # Convertir a cadena
df_wos['affiliations_modified'] = df_wos['affiliations_modified'].str.upper()

# Reemplazar caracteres especiales en la columna "affiliations_modified"
#df_wos['affiliations_modified'] = df_wos['affiliations_modified'].apply(lambda x: re.sub(r'[^A-Z0-9]+', ' ', x).strip())


# Lista de palabras o frases para buscar
 
words_to_searchprivadas = ["Católica", "Azuay", "Panamericana", "Salesiana", "Casa", "Santiago",
           "Francisco", "Rio", "Ecologica", "Particular", "Internacional",
           "Javeriana", "Alfredo", "Cristiana", "Especialidades", "Indoamerica",
           "Interamericana", "Tecnológica", "Metropolitana", "Otavalo",
           "Santa", "Pacifico", "Laica", "Naval", "Ecotec", "IDE", "Iberoamericana",
           "San", "Hemisferios", "Mandino", "Israel", "Américas", "FLACSO", "Catolica",
           "Americas"]
words_to_searchprivadas = ["Milagro"]
# Buscar filas donde 'affiliations' comienza con alguna de las palabras en words_to_search
#df_starts_with = df_wos[df_wos['affiliations'].str.startswith(tuple(words_to_search))]
# Buscar filas donde 'affiliations' termina con alguna de las palabras en words_to_search
#df_ends_with = df_wos[df_wos['affiliations'].str.endswith(tuple(words_to_search))]
words_to_searchpublicas = [("UNIVERSIDAD","YACHAY","TECH"),("UNIVERSIDAD","TECNICA","AMBATO"),("UNIVERSIDAD","ESTATAL","AMAZONICA ")
                           ,("UNIVERSIDAD","ESTATAL","ELENA"),("ESCUELA","POLITECNICA ","EJERCITO ")
                           ,("ESCUELA","POLITECNICA ","NACIONAL")
                            ,("FACULTAD","LATINOAMERICANA","CIENCIAS")
                             ,("UNIVERSIDAD","DE","QUITO")
                              ,("INSTITUTO","ALTOS","NACIONALES")
                               ,("UNIVERSIDAD","ANDINA","BOLIVAR")
                                ,("UNIVERSIDAD","ESTATAL","AMAZONICA")
                                ,("UNIVERSIDAD","AGRARIA","ECUADOR")
                                ,("UNIVERSIDAD","TECNICA","ESMERALDAS")
                                ,("UNIVERSIDAD","REGIONAL","AMAZONICA")
                                ,("ESCUELA","POLITECNICA","MANABI")
,("UNIVERSIDAD","ESTATAL","MANABI"),("UNIVERSIDAD","CENTRAL","ECUADOR")
,("UNIVERSIDAD","LAICA","MANABI")
,("UNIVERSIDAD","TECNICA","MANABI")
,("UNIVERSIDAD","NACIONAL","LOJA")
,("UNIVERSIDAD","TECNICA","BABAHOYO")
,("UNIVERSIDAD","TECNICA","QUEVEDO")
,("ESCUELA","SUPERIOR","LITORAL")
,("UNIVERSIDAD","AGRARIA","ECUADOR")
,("UNIVERSIDAD","LAICA","MANABI")
,("UNIVERSIDAD","TECNICA","MANABI")
,("UNIVERSIDAD","NACIONAL","LOJA")]

words_to_searchprivadas = [("UNIVERSIDAD", "YACHAY"), ("Universidad", "Ambato")]  # Continúa con el resto de las combinaciones
# Inicialmente, asumimos que ninguna fila es válida
mask = pd.Series([False] * len(df_wos))
for word_triplet in words_to_searchprivadas:
    # Para cada conjunto de tres palabras, actualizamos la máscara para incluir las filas que contienen las tres palabras
    mask |= (df_wos['affiliations_modified'].str.contains(word_triplet[0].upper(), case=False)) & \
            (df_wos['affiliations_modified'].str.contains(word_triplet[1].upper(), case=False)) & \
            (df_wos['affiliations_modified'].str.contains(word_triplet[2].upper(), case=False))

# Aplicar la máscara al DataFrame
df_contains = df_wos[mask]

# Si deseas buscar filas donde 'affiliations' contiene cualquiera de las palabras en words_to_search
#df_containsprivada = df_wos[df_wos['affiliations_modified'].str.contains('|'.join(words_to_searchprivadas))]
#df_containspublicas = df_wos[df_wos['affiliations_modified'].str.contains('|'.join(words_to_searchpublicas))]
# Si estás satisfecho con los cambios en 'affiliations_modified', puedes reemplazar la columna original
#df_containsprivada.drop(columns=['affiliations_modified'], inplace=True)

#output_path = 'C:\\Investigación\\Trabajo_2023\\Dr. Patricio Alvarez\\Revista Información, cultura y sociedad\\Dato\\afiliaciones_filtrado.csv'
#df_containsprivada.to_csv(output_path, index=False)

print(f" se guardo la información")