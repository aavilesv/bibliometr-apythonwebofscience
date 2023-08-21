import pandas as pd
import re

# Cargar los archivos
df_wos = pd.read_excel('C:\\Investigación\\Trabajo_2023\Codificaciones\\archivo_unidoprivadaspublicas.xlsx')

df_wos_original = df_wos.copy()


variants = [
'UNIV OTAVALO ECUADOR',
'UNIV OTAVALO IMBABURA',
'UNIV OTAVALO',
]


standard_name = 'UNIVERSIDAD DE OTAVALO'

# Función de reemplazo actualizada


def replace_with_standard(text, delimiter=','):
    # Verificar si el texto es una cadena
    if not isinstance(text, str):
        return text  # Devuelve el valor original si no es una cadena

    parts = text.split(delimiter)
    for i, part in enumerate(parts):
        if any(part.strip().lower().startswith(variant.lower()) for variant in variants):
          
            parts[i] = standard_name
           
    return delimiter.join(parts)

# Actualizar la columna 'affiliation'
df_wos['affiliation'] = df_wos['affiliation'].apply(lambda x: replace_with_standard(x))

# Actualizar la columna 'affiliations' usando el delimitador ';'
df_wos['affiliations'] = df_wos['affiliations'].apply(lambda x: replace_with_standard(x, delimiter=';'))





# Identificar las filas que cambiaron en la columna 'affiliation'
updated_affiliation = df_wos_original['affiliation'] != df_wos['affiliation']

# Identificar las filas que cambiaron en la columna 'affiliations'
updated_affiliations = df_wos_original['affiliations'] != df_wos['affiliations']

# Combinar las dos series booleanas para obtener un único indicador de filas actualizadas
updated_rows = updated_affiliation | updated_affiliations

# Filtrar el DataFrame para obtener solo las filas actualizadas
print('Universidad:  '+str(standard_name))
df_updated = df_wos[updated_rows]
# Guardar el DataFrame filtrado
df_wos.to_excel('C:\\Investigación\\Trabajo_2023\Codificaciones\\archivo_unidoprivadaspublicas.xlsx', index=False)

