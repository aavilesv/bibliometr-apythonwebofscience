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
 
words_to_searchprivadas = [("UNIVERSIDAD","CATOLICA","CUENCA") 
                           ,("UNIVERSIDAD","DEL","AZUAY")
 ,("UNIVERSIDAD","PANAMERICANA","CUENCA")
 ,("UNIVERSIDAD","POLITECNICA","SALESIANA")
 ,("UNIVERSIDAD","INTERAMERICANA","ECUADOR")
 ,("UNIVERSIDAD","ANTONIO","MACHALA")
  ,("UNIVERSIDAD","U","METROPOLITANA")
   ,("PONTIFICIA","UNIVERSIDAD","ECUADOR")
    ,("UNIVERSIDAD","U","OTAVALO")
     ,("UNIVERSIDAD","CASA","GRANDE")
      ,("UNIVERSIDAD","CATOLICA","SANTIAGO")
      ,("UNIVERSIDAD","FRANCISCO","QUITO")
      ,("UNIVERSIDAD","DEL","RIO")
      ,("UNIVERSIDAD","SANTA","MARIA")
      ,("UNIVERSIDAD","PACIFICO","NEGOCIOS")
      
      ,("UNIVERSIDAD ","LAICA","ROCAFUERTE")
       ,("UNIVERSIDAD","NAVAL","VALVERDE")
       ,("UNIVERSIDAD","FRANCISCO","QUITO")
       ,("UNIVERSIDAD","ESPECIALIDADES","SANTO")
     
       ,("UNIVERSIDAD","TECNOLOGICA","ECOTEC")
       ,("UNIVERSIDAD","U","ECOTEC")
       ,("UNIVERSIDAD","EMPRESARIAL","GUAYAQUIL")
        ,("IDE","BUSINESS","SCHOOL")
        ,("UNIVERSIDAD","U","HEMISFERIOS")
        ,("UNIVERSIDAD","IBEROAMERICANA","ECUADOR")
        ,("UNIVERSIDAD","INTERNACIONAL","ECUADOR")
        
        ,("ESC","POLITEC","ECOLOGICA")
        ,("UNIVERSIDAD","TECNICA","PARTICULAR")
        ,("UNIVERSIDAD","INTERNACIONAL","ECUADOR")
         ,("ESCUELA","TECNOLOGICA","AMAZONICA ")
         ,("UNIVERSIDAD","GREGORIO","PORTOVIEJO")
         
         ,("ESC","JAVERIANA","ECUADOR")
         ,("UNIVERSIDAD","ALFREDO","GUERRERO")
         ,("UNIVERSIDAD","CRISTIANA","LATINOAMERICANA")
          ,("UNIVERSIDAD","ESPECIALIDADES","TURISTICAS")
          ,("UNIVERSIDAD","TECNOLOGICA","INDOAMERICA")
        ,("UNIVERSIDAD","U","INDOAMÉRICA")
        
        
         ,("ESC","SUPERIOR","AMAZONICA")
         ,("UNIVERSIDAD","IBEROAMERICANA","ECUADOR")
         ,("UNIVERSIDAD","INTERNACIONAL","ECUADOR")
          ,("UNIVERSIDAD","OG","MANDINO")
          ,("UNIVERSIDAD","INTERNACIONAL","SEK")
          ,("UNIVERSIDAD","TECNOLOGICA","AMERICA")
        ,("UNIVERSIDAD","TECNOLOGICA","EQUINOCCIAL")
        
         ,("UNIVERSIDAD","U","ISRAEL")
         ,("NACIONES","PUEBLOS","WASI")
          ,("UNIVERSIDAD","DE","AMERICAS")
          ,("UNIVERSIDAD","PACIFICO","NEGOCIOS")
          ,("UNIVERSIDAD","POLITECNICA","SALESIANA")
        ,("UNIVERSIDAD","U","METROPOLITANA ")
        
        
        ,("FLASCO","F","FLASCO")
        ,("UNIVERSIDAD","REGIONAL","ANDES")
        ,("UNIVERSIDAD","TECNOLOGICA","INDOAMERICA")
        ,("PONTIFICIA","CATOLICA","ECUADOR")
        
        
      ]  # Continúa con el resto de las combinaciones
# Buscar filas donde 'affiliations' comienza con alguna de las palabras en words_to_search
#df_starts_with = df_wos[df_wos['affiliations'].str.startswith(tuple(words_to_search))]
# Buscar filas donde 'affiliations' termina con alguna de las palabras en words_to_search
#df_ends_with = df_wos[df_wos['affiliations'].str.endswith(tuple(words_to_search))]
words_to_searchpublicas = [("UNIVERSIDAD","YACHAY","TECH")
                           ,("UNIVERSIDAD","TECNICA","AMBATO")
                           ,("UNIVERSIDAD","ESTATAL","AMAZONICA ")
                           ,("UNIVERSIDAD","ESTATAL","ELENA")
                           ,("ESCUELA","POLITECNICA","EJERCITO")
                           ,("ESCUELA","POLITECNICA","NACIONAL")
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
,("UNIVERSIDAD","DE","GUAYAQUIL ")
,("UNIVERSIDAD","ESTATAL","MILAGRO")
,("UNIVERSIDAD","DE","ARTES")
,("UNIVERSIDAD","VARGAS","TORRES")
,("UNIVERSIDAD","TECNICA","NORTE")
,("ESCUELA","TECNICA","COTOPAXI")
,("ESCUELA","POLITECNICA","EJERCITO")
,("ESCUELA","TECNICA","COTOPAXI")
,("ESCUELA","TECNICA","MACHALA")
,("UNIVERSIDAD","POLITECNICA","CARCHI")
,("ESCUELA","POLITECNICA","CHIMBORAZO")
,("UNIVERSIDAD","NACIONAL","CHIMBORAZO")
,("UNIVERSIDAD","DE","CUENCA")
,("UNIVERSIDAD","NACIONAL","ECUADOR")
,("UNIVERSIDAD","NACIONAL","EDUCACION")
,("UNIVERSIDAD","ESTATAL","BOLIVAR")
]


# Inicialmente, asumimos que ninguna fila es válida
mask = pd.Series([False] * len(df_wos))
for word_triplet in words_to_searchpublicas:
    # Para cada conjunto de tres palabras, actualizamos la máscara para incluir las filas que contienen las tres palabras
    mask |= (df_wos['affiliations_modified'].str.contains(word_triplet[0].upper(), case=False)) & \
            (df_wos['affiliations_modified'].str.contains(word_triplet[1].upper(), case=False)) & \
            (df_wos['affiliations_modified'].str.contains(word_triplet[2].upper(), case=False))

# Aplicar la máscara al DataFrame
df_containspublica = df_wos[mask]

mask = pd.Series([False] * len(df_wos))
for word_triplet in words_to_searchprivadas:
    # Para cada conjunto de tres palabras, actualizamos la máscara para incluir las filas que contienen las tres palabras
    mask |= (df_wos['affiliations_modified'].str.contains(word_triplet[0].upper(), case=False)) & \
            (df_wos['affiliations_modified'].str.contains(word_triplet[1].upper(), case=False)) & \
            (df_wos['affiliations_modified'].str.contains(word_triplet[2].upper(), case=False))

# Aplicar la máscara al DataFrame
df_containsprivada = df_wos[mask]
# Si deseas buscar filas donde 'affiliations' contiene cualquiera de las palabras en words_to_search
#df_containsprivada = df_wos[df_wos['affiliations_modified'].str.contains('|'.join(words_to_searchprivadas))]
#df_containspublicas = df_wos[df_wos['affiliations_modified'].str.contains('|'.join(words_to_searchpublicas))]
# Si estás satisfecho con los cambios en 'affiliations_modified', puedes reemplazar la columna original
df_containspublica.drop(columns=['affiliations_modified'], inplace=True)
df_containsprivada.drop(columns=['affiliations_modified'], inplace=True)

output_pathpublicas = 'C:\\Investigación\\Trabajo_2023\\Dr. Patricio Alvarez\\Revista Información, cultura y sociedad\\Dato\\finalpublicas.xlsx'
output_pathprivadas = 'C:\\Investigación\\Trabajo_2023\\Dr. Patricio Alvarez\\Revista Información, cultura y sociedad\\Dato\\finalprivadas.xlsx'
df_containspublica.to_excel(output_pathpublicas, index=False)
df_containsprivada.to_excel(output_pathprivadas, index=False)


print('el total privadas ', {str(len(words_to_searchprivadas))})
print('el total publicas', {str(len(words_to_searchpublicas))})
print(f" se guardo la información")