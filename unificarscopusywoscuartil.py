import pandas as pd
# Vamos a definir una función que pueda ser utilizada para buscar y normalizar ISSNs en un DataFrame

def normalize_issn(issn_series):
    """
    Normaliza los ISSNs en una serie de pandas, eliminando ceros iniciales.
    
    :param issn_series: Serie de pandas con ISSNs
    :return: Serie de pandas con ISSNs normalizados
    """
    return issn_series.str.lstrip('0')

# Crear un DataFrame de ejemplo
df_example = pd.DataFrame({
    'issn': ['13026488', '013026488', '00001123', '11234567', '013026488']
})

# Aplicar la función de normalización
df_example['normalized_issn'] = normalize_issn(df_example['issn'])

df_example