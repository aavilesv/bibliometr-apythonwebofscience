import pandas as pd
import re
# Cargar los archivos
df_scopos =  pd.read_excel('C:\\Investigación\\Trabajo_2023\\Msc. Alberto León Batallas\\data\\Producción de las fuentes a lo largo del tiempo scopus 20_.xlsx')
df_wos = pd.read_excel('C:\\Investigación\\Trabajo_2023\\Msc. Alberto León Batallas\\data\Producción de las fuentes a lo largo del tiempo wos_.xlsx')


cols_comunes = df_scopos.columns.intersection(df_wos.columns).drop('Year')
for col in cols_comunes:
    df_scopos[col] = df_scopos[col] + df_wos.groupby('Year')[col].transform('sum')

resultado = pd.merge(df_scopos, df_wos, on='Year', how='outer', suffixes=('', '_drop'))
# Eliminar columnas con sufijo "_drop"
resultado.drop(columns=resultado.filter(regex='_drop$').columns, inplace=True)


resultado.fillna(0, inplace=True)
#esultado = resultado.filter(regex='_drop$').columns
resultado.to_excel('C:\\Investigación\\Trabajo_2023\\Msc. Alberto León Batallas\\data\\resultado_finalproduccion.xlsx', index=False)


#columnas=resultado.columns.tolist()
#resultadofinal=resultado.columns