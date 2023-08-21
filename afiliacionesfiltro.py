import pandas as pd
import re
# Cargar los archivos
df_wos = pd.read_csv('C:\\Investigación\\Trabajo_2023\Codificaciones\\finalbib.csv')


# Lista de palabras o frases para buscar

df_wos['affiliations_mod'] = df_wos['affiliations']
# Convertir todo a mayúsculas
df_wos['affiliations_mod'] = df_wos['affiliations_mod'].astype(str)  # Convertir a cadena
df_wos['affiliations_mod'] = df_wos['affiliations_mod'].str.upper()


df_wos['funding-acknowledgement_mod'] = df_wos['funding-acknowledgement']
# Convertir todo a mayúsculas
df_wos['funding-acknowledgement_mod'] = df_wos['funding-acknowledgement_mod'].astype(str)  # Convertir a cadena
df_wos['funding-acknowledgement_mod'] = df_wos['funding-acknowledgement_mod'].str.upper()

df_wos['funding-text_mod'] = df_wos['funding-text']
# Convertir todo a mayúsculas
df_wos['funding-text_mod'] = df_wos['funding-text_mod'].astype(str)  # Convertir a cadena
df_wos['funding-text_mod'] = df_wos['funding-text_mod'].str.upper()

df_wos['address_mod'] = df_wos['address']
# Convertir todo a mayúsculas
df_wos['address_mod'] = df_wos['address_mod'].astype(str)  # Convertir a cadena
df_wos['address_mod'] = df_wos['address_mod'].str.upper()

df_wos['affiliation_mod'] = df_wos['affiliation']
# Convertir todo a mayúsculas
df_wos['affiliation_mod'] = df_wos['affiliation_mod'].astype(str)  # Convertir a cadena
df_wos['affiliation_mod'] = df_wos['affiliation_mod'].str.upper()

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
words_to_searchpublicas=[("UNIV","YACHAY","TECH")]
words_to_searchpublicas = [("UNIV","YACHAY","TECH")
                           ,("UNIV","TEC","AMBATO")
                           ,("UNIV","EST","AMAZO ")
                           ,("UNIV","EST","ELENA")
                           ,("ESC","POL","EJERCITO")
                           ,("ESC","POL","NAC")
                            ,("FAC","LAT","CIENCIAS")
                             ,("UNIV","DE","QUITO")
                              ,("INSTITUTO","ALTOS","NAC")
                               ,("UNIV","AN","BOLIVAR")
                                ,("UNIV","EST","AMAZO")
                                ,("UNIV","AGRARIA","ECUADOR")
                                ,("UNIV","TEC","ESMERALDAS")
                                ,("UNIV","REG","AMAZO")
                                ,("ESC","POL","MANABI")
,("UNIV","EST","MANABI")
,("UNIV","CEN","ECUADOR")
,("UNIV","LAICA","MANABI")
,("UNIV","TEC","MANABI")
,("UNIV","NAC","LOJA")
,("UNIV","TEC","BABAHOYO")
,("UNIV","TEC","QUEVEDO")
,("ESC","SUP","LITORAL")
,("UNIV","AGR","ECUADOR")
,("UNIV","DE","GUAYAQUIL ")
,("UNIV","EST","MILAGRO")
,("UNIV","DE","ARTES")
,("UNIV","VAR","TORRES")
,("UNIV","TEC","NORTE")
,("ESC","TEC","COTOPAXI")
,("ESC","POL","EJERCITO")
,("ESC","TEC","COTOPAXI")
,("ESC","TEC","MACHALA")
,("UNIV","POL","CARCHI")
,("ESC","POL","CHIMBORAZO")
,("UNIV","NAC","CHIMBORAZO")
,("UNIV","DE","CUENCA")
,("UNIV","NA","ECUADOR")
,("UNIV","NA","EDUCACION")
,("UNIV","EST","BOLIVAR"),

# PRIVADAS
("UNIV","CAT","CUENCA") 
,("UNIV","DEL","AZUAY")
 ,("UNIV","PAN","CUENCA")
 ,("UNIV","POL","SALESIANA")
 ,("UNIV","INTER","ECUADOR")
 ,("UNIV","ANTONIO","MACHALA")
 ,("UNIV","U","METROPOLITANA")
 ,("PONTIFICIA","UNIV","ECUADOR")
 ,("UNIV","U","OTAVALO")
 ,("UNIV","CASA","GRANDE")
 ,("UNIV","CAT","SANTIAGO")
 ,("UNIV","FRA","QUITO")
 ,("UNIV","DEL","RIO")
 ,("UNIV","SANTA","MARIA")
 ,("UNIV","PACIFICO","NEGOCIOS")
 ,("UNIV ","LAICA","ROCAFUERTE")
 ,("UNIV","NAVAL","VALVERDE")
 ,("UNIV","FRAN","QUITO")
 ,("UNIV","ESP","SANTO")
 ,("UNIV","TEC","ECOTEC")
 ,("UNIV","U","ECOTEC")
 ,("UNIV","EMPRESARIAL","GUAYAQUIL")
 ,("IDE","BUSINESS","SCHOOL")
 ,("UNIV","U","HEMISFERIOS")
 ,("UNIV","IBERO","ECUADOR")
 ,("UNIV","INTE","ECUADOR")
 ,("ESC","POL","ECOLOGICA")
        ,("UNIV","TEC","PARTICULAR")
        ,("UNIV","INTE","ECUADOR")
         ,("ESC","TEC","AMAZO ")
         ,("UNIV","GRE","PORTOVIEJO")
         
         ,("ESC","JAV","ECUADOR")
         ,("UNIV","ALF","GUERRERO")
         ,("UNIV","CRIS","LATINO")
          ,("UNIV","ESP","TURISTICAS")
          ,("UNIV","TEC","INDOAMERICA")
        ,("UNIV","U","INDOAMÉRICA")
        
        
         ,("ESC","SUP","AMAZO")
         ,("UNIV","IBE","ECUADOR")
         ,("UNIV","INT","ECUADOR")
          ,("UNIV","OG","MANDINO")
          ,("UNIV","INTE","SEK")
          ,("UNIV","TEC","AMERICA")
        ,("UNIV","TEC","EQUINOCCIAL")
        
         ,("UNIV","U","ISRAEL")
         ,("NACIONES","PUEBLOS","WASI")
          ,("UNIV","DE","AMERICAS")
          ,("UNIV","PAC","NEGOCIOS")
          ,("UNIV","POL","SALESIANA")
        ,("UNIV","U","METROPOLITANA ")
        
        
        ,("FLASCO","F","FLASCO")
        ,("UNIV","REGIONAL","ANDES")
        ,("UNIV","TEC","INDOAMERICA")
        ,("PONT","CAT","ECUADOR")
        
]
# ... [El resto del código anterior sigue igual]

# Función para generar una máscara de búsqueda basada en una columna y una lista de palabras/frases
def generate_search_mask(df, column, words_to_search):
    mask = pd.Series([False] * len(df))
    for word_triplet in words_to_search:
        mask |= (df[column].str.contains(word_triplet[0].upper(), case=False, na=False)) & \
                (df[column].str.contains(word_triplet[1].upper(), case=False, na=False)) & \
                (df[column].str.contains(word_triplet[2].upper(), case=False, na=False))
    return mask


columns_to_check = ['affiliations_mod', 'funding-acknowledgement_mod','address_mod', 'address_mod', 'affiliation_mod']
# Máscara general inicializada en False
overall_mask_privadas = pd.Series([False] * len(df_wos))
overall_mask_publicas = pd.Series([False] * len(df_wos))

# Iterar sobre las columnas y actualizar la máscara general
for col in columns_to_check:
    overall_mask_privadas |= generate_search_mask(df_wos, col, words_to_searchprivadas)
    overall_mask_publicas |= generate_search_mask(df_wos, col, words_to_searchpublicas)

# Filtrar el DataFrame original usando la máscara general
df_containsprivada = df_wos[overall_mask_privadas]
#df_containspublica = df_wos[overall_mask_publicas]
df_containtotal = df_wos[overall_mask_publicas]

df_containtotal=df_containtotal.drop(columns=['affiliations_mod', 'funding-acknowledgement_mod','address_mod', 'address_mod', 'affiliation_mod'], inplace=True)
output_pathpublicas = 'C:\\Investigación\\Trabajo_2023\Codificaciones\\finalpublicasprivadas.xlsx'
df_containtotal.to_csv(output_pathpublicas, index=False)
# ... [El resto del código sigue igual]


print('el total de registros', {str(len(df_wos))})
columnas=df_wos.columns.tolist()

#output_pathpublicas = 'C:\\Investigación\\Trabajo_2023\\Dr. Patricio Alvarez\\Revista Información, cultura y sociedad\\Dato\\finalpublicas.xlsx'
#output_pathprivadas = 'C:\\Investigación\\Trabajo_2023\\Dr. Patricio Alvarez\\Revista Información, cultura y sociedad\\Dato\\finalprivadas.xlsx'
#df_containspublica.to_excel(output_pathpublicas, index=False)
#df_containsprivada.to_excel(output_pathprivadas, index=False)


print('el total privadas ', {str(len(words_to_searchprivadas))})
print('el total publicas', {str(len(words_to_searchpublicas))})
print(f" se guardo la información")


import pandas as pd
import re
# Cargar los archivos
df_wos = pd.read_csv('C:\\Investigación\\Trabajo_2023\Codificaciones\\finalbib.csv')


# Lista de palabras o frases para buscar

df_wos['affiliations_mod'] = df_wos['affiliations']
# Convertir todo a mayúsculas
df_wos['affiliations_mod'] = df_wos['affiliations_mod'].astype(str)  # Convertir a cadena
df_wos['affiliations_mod'] = df_wos['affiliations_mod'].str.upper()


df_wos['funding-acknowledgement_mod'] = df_wos['funding-acknowledgement']
# Convertir todo a mayúsculas
df_wos['funding-acknowledgement_mod'] = df_wos['funding-acknowledgement_mod'].astype(str)  # Convertir a cadena
df_wos['funding-acknowledgement_mod'] = df_wos['funding-acknowledgement_mod'].str.upper()

df_wos['funding-text_mod'] = df_wos['funding-text']
# Convertir todo a mayúsculas
df_wos['funding-text_mod'] = df_wos['funding-text_mod'].astype(str)  # Convertir a cadena
df_wos['funding-text_mod'] = df_wos['funding-text_mod'].str.upper()

df_wos['address_mod'] = df_wos['address']
# Convertir todo a mayúsculas
df_wos['address_mod'] = df_wos['address_mod'].astype(str)  # Convertir a cadena
df_wos['address_mod'] = df_wos['address_mod'].str.upper()

df_wos['affiliation_mod'] = df_wos['affiliation']
# Convertir todo a mayúsculas
df_wos['affiliation_mod'] = df_wos['affiliation_mod'].astype(str)  # Convertir a cadena
df_wos['affiliation_mod'] = df_wos['affiliation_mod'].str.upper()

words_to_searchprivadas = [
# PRIVADAS
("UNIV","CAT","CUENCA") 
,("UNIV","DEL","AZUAY")
 ,("UNIV","PAN","CUENCA")
 ,("UNIV","POL","SALESIANA")
 ,("UNIV","INTER","ECUADOR")
 ,("UNIV","ANTONIO","MACHALA")
 ,("UNIV","U","METROPOLITANA")
 ,("PONTIFICIA","UNIV","ECUADOR")
 ,("UNIV","U","OTAVALO")
 ,("UNIV","CASA","GRANDE")
 ,("UNIV","CAT","SANTIAGO")
 ,("UNIV","FRA","QUITO")
 ,("UNIV","DEL","RIO")
 ,("UNIV","SANTA","MARIA")
 ,("UNIV","PACIFICO","NEGOCIOS")
 ,("UNIV ","LAICA","ROCAFUERTE")
 ,("UNIV","NAVAL","VALVERDE")
 ,("UNIV","FRAN","QUITO")
 ,("UNIV","ESP","SANTO")
 ,("UNIV","TEC","ECOTEC")
 ,("UNIV","U","ECOTEC")
 ,("UNIV","EMPRESARIAL","GUAYAQUIL")
 ,("IDE","BUSINESS","SCHOOL")
 ,("UNIV","U","HEMISFERIOS")
 ,("UNIV","IBERO","ECUADOR")
 ,("UNIV","INTE","ECUADOR")
 ,("ESC","POL","ECOLOGICA")
        ,("UNIV","TEC","PARTICULAR")
        ,("UNIV","INTE","ECUADOR")
         ,("ESC","TEC","AMAZO ")
         ,("UNIV","GRE","PORTOVIEJO")
         
         ,("ESC","JAV","ECUADOR")
         ,("UNIV","ALF","GUERRERO")
         ,("UNIV","CRIS","LATINO")
          ,("UNIV","ESP","TURISTICAS")
          ,("UNIV","TEC","INDOAMERICA")
        ,("UNIV","U","INDOAMÉRICA")
        
        
         ,("ESC","SUP","AMAZO")
         ,("UNIV","IBE","ECUADOR")
         ,("UNIV","INT","ECUADOR")
          ,("UNIV","OG","MANDINO")
          ,("UNIV","INTE","SEK")
          ,("UNIV","TEC","AMERICA")
        ,("UNIV","TEC","EQUINOCCIAL")
        
         ,("UNIV","U","ISRAEL")
         ,("NACIONES","PUEBLOS","WASI")
          ,("UNIV","DE","AMERICAS")
          ,("UNIV","PAC","NEGOCIOS")
          ,("UNIV","POL","SALESIANA")
        ,("UNIV","U","METROPOLITANA ")
        
        
        ,("FLASCO","F","FLASCO")
        ,("UNIV","REGIONAL","ANDES")
        ,("UNIV","TEC","INDOAMERICA")
        ,("PONT","CAT","ECUADOR")
        
        
        
      ]  # Continúa con el resto de las combinaciones
# Buscar filas donde 'affiliations' comienza con alguna de las palabras en words_to_search
#df_starts_with = df_wos[df_wos['affiliations'].str.startswith(tuple(words_to_search))]
# Buscar filas donde 'affiliations' termina con alguna de las palabras en words_to_search
#df_ends_with = df_wos[df_wos['affiliations'].str.endswith(tuple(words_to_search))]
words_to_searchpublicas=[("UNIV","YACHAY","TECH")]
words_to_searchpublicas = [("UNIV","YACHAY","TECH")
                           ,("UNIV","TEC","AMBATO")
                           ,("UNIV","EST","AMAZO ")
                           ,("UNIV","EST","ELENA")
                           ,("ESC","POL","EJERCITO")
                           ,("ESC","POL","NAC")
                            ,("FAC","LAT","CIENCIAS")
                             ,("UNIV","DE","QUITO")
                              ,("INSTITUTO","ALTOS","NAC")
                               ,("UNIV","AN","BOLIVAR")
                                ,("UNIV","EST","AMAZO")
                                ,("UNIV","AGRARIA","ECUADOR")
                                ,("UNIV","TEC","ESMERALDAS")
                                ,("UNIV","REG","AMAZO")
                                ,("ESC","POL","MANABI")
,("UNIV","EST","MANABI")
,("UNIV","CEN","ECUADOR")
,("UNIV","LAICA","MANABI")
,("UNIV","TEC","MANABI")
,("UNIV","NAC","LOJA")
,("UNIV","TEC","BABAHOYO")
,("UNIV","TEC","QUEVEDO")
,("ESC","SUP","LITORAL")
,("UNIV","AGR","ECUADOR")
,("UNIV","DE","GUAYAQUIL ")
,("UNIV","EST","MILAGRO")
,("UNIV","DE","ARTES")
,("UNIV","VAR","TORRES")
,("UNIV","TEC","NORTE")
,("ESC","TEC","COTOPAXI")
,("ESC","POL","EJERCITO")
,("ESC","TEC","COTOPAXI")
,("ESC","TEC","MACHALA")
,("UNIV","POL","CARCHI")
,("ESC","POL","CHIMBORAZO")
,("UNIV","NAC","CHIMBORAZO")
,("UNIV","DE","CUENCA")
,("UNIV","NA","ECUADOR")
,("UNIV","NA","EDUCACION")
,("UNIV","EST","BOLIVAR"),

# PRIVADAS
("UNIV","CAT","CUENCA") 
,("UNIV","DEL","AZUAY")
 ,("UNIV","PAN","CUENCA")
 ,("UNIV","POL","SALESIANA")
 ,("UNIV","INTER","ECUADOR")
 ,("UNIV","ANTONIO","MACHALA")
 ,("UNIV","U","METROPOLITANA")
 ,("PONTIFICIA","UNIV","ECUADOR")
 ,("UNIV","U","OTAVALO")
 ,("UNIV","CASA","GRANDE")
 ,("UNIV","CAT","SANTIAGO")
 ,("UNIV","FRA","QUITO")
 ,("UNIV","DEL","RIO")
 ,("UNIV","SANTA","MARIA")
 ,("UNIV","PACIFICO","NEGOCIOS")
 ,("UNIV ","LAICA","ROCAFUERTE")
 ,("UNIV","NAVAL","VALVERDE")
 ,("UNIV","FRAN","QUITO")
 ,("UNIV","ESP","SANTO")
 ,("UNIV","TEC","ECOTEC")
 ,("UNIV","U","ECOTEC")
 ,("UNIV","EMPRESARIAL","GUAYAQUIL")
 ,("IDE","BUSINESS","SCHOOL")
 ,("UNIV","U","HEMISFERIOS")
 ,("UNIV","IBERO","ECUADOR")
 ,("UNIV","INTE","ECUADOR")
 ,("ESC","POL","ECOLOGICA")
        ,("UNIV","TEC","PARTICULAR")
        ,("UNIV","INTE","ECUADOR")
         ,("ESC","TEC","AMAZO ")
         ,("UNIV","GRE","PORTOVIEJO")
         
         ,("ESC","JAV","ECUADOR")
         ,("UNIV","ALF","GUERRERO")
         ,("UNIV","CRIS","LATINO")
          ,("UNIV","ESP","TURISTICAS")
          ,("UNIV","TEC","INDOAMERICA")
        ,("UNIV","U","INDOAMÉRICA")
        
        
         ,("ESC","SUP","AMAZO")
         ,("UNIV","IBE","ECUADOR")
         ,("UNIV","INT","ECUADOR")
          ,("UNIV","OG","MANDINO")
          ,("UNIV","INTE","SEK")
          ,("UNIV","TEC","AMERICA")
        ,("UNIV","TEC","EQUINOCCIAL")
        
         ,("UNIV","U","ISRAEL")
         ,("NACIONES","PUEBLOS","WASI")
          ,("UNIV","DE","AMERICAS")
          ,("UNIV","PAC","NEGOCIOS")
          ,("UNIV","POL","SALESIANA")
        ,("UNIV","U","METROPOLITANA ")
        
        
        ,("FLASCO","F","FLASCO")
        ,("UNIV","REGIONAL","ANDES")
        ,("UNIV","TEC","INDOAMERICA")
        ,("PONT","CAT","ECUADOR")
        
]
# ... [El resto del código anterior sigue igual]

# Función para generar una máscara de búsqueda basada en una columna y una lista de palabras/frases
def generate_search_mask(df, column, words_to_search):
    mask = pd.Series([False] * len(df))
    for word_triplet in words_to_search:
        mask |= (df[column].str.contains(word_triplet[0].upper(), case=False, na=False)) & \
                (df[column].str.contains(word_triplet[1].upper(), case=False, na=False)) & \
                (df[column].str.contains(word_triplet[2].upper(), case=False, na=False))
    return mask


columns_to_check = ['affiliations_mod', 'funding-acknowledgement_mod','address_mod', 'address_mod', 'affiliation_mod','funding-text_mod']
# Máscara general inicializada en False
overall_mask_privadas = pd.Series([False] * len(df_wos))
overall_mask_publicas = pd.Series([False] * len(df_wos))

# Iterar sobre las columnas y actualizar la máscara general
for col in columns_to_check:
    overall_mask_privadas |= generate_search_mask(df_wos, col, words_to_searchprivadas)
    overall_mask_publicas |= generate_search_mask(df_wos, col, words_to_searchpublicas)

# Filtrar el DataFrame original usando la máscara general
df_containsprivada = df_wos[overall_mask_privadas]
#df_containspublica = df_wos[overall_mask_publicas]
df_containtotal = df_wos[overall_mask_publicas]

df_containtotal=df_containtotal.drop(columns=['affiliations_mod', 'funding-acknowledgement_mod','address_mod', 'address_mod', 'affiliation_mod','funding-text_mod'], inplace=True)

# ... [El resto del código sigue igual]

primeras=df_wos.head(n=5)
print('el total de registros', {str(len(df_wos))})
columnas=df_wos.columns.tolist()