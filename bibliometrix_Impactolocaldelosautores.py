import pandas as pd
import matplotlib.pyplot as plt
import numpy as np  # Añade la importación de numpy para generar colores únicos

# Leer el archivo Excel
ruta_archivo = 'G:\\Mi unidad\\2024\\Msc. Jorge Vinueza\\informaciondata\\scopus_Author_Impact.xlsx'

df = pd.read_excel(ruta_archivo)

# Asegurarse de que las columnas estén en el formato correcto
columnas_esperadas = ["Element", "h_index", "g_index", "m_index", "TC", "NP", "PY_start"]
if not all(col in df.columns for col in columnas_esperadas):
    raise ValueError("El archivo Excel no tiene las columnas esperadas.")

# Ordenar el DataFrame por h_index en orden descendente y tomar los primeros 10 registros
df_top10 = df.sort_values(by='h_index', ascending=False).head(10)

# Generar colores únicos para cada autor
colores = plt.cm.get_cmap('tab20', len(df_top10))

# Crear gráfico de dispersión con colores únicos
plt.figure(figsize=(12, 7))
for i, autor in enumerate(df_top10['Element']):
    plt.scatter(df_top10['h_index'].iloc[i], df_top10['TC'].iloc[i], color=colores(i), s=100, label=autor)

plt.title("Authors' Local Impact: h index vs Total Citations")
plt.xlabel('h_index')
plt.ylabel('Total Citations (TC)')
plt.legend()  # Mostrar etiquetas de autor en la leyenda
plt.grid(True)
plt.tight_layout()
plt.show()
