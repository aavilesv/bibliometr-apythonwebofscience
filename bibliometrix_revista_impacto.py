


#pip install adjustText

#ruta_archivo = 'C:\\Users\\AAVILESV\\Downloads\\Most_Relevant_Sources.xlsx'
from adjustText import adjust_text

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np  # Añade la importación de numpy para generar colores únicos

# Leer el archivo Excel
ruta_archivo = 'G:\\Mi unidad\\2024\\Msc. Jorge Vinueza\\informaciondata\\scopus_Source_Impact.xlsx'


# Leer el archivo Excel
df = pd.read_excel(ruta_archivo)
offsets = [(-5, 10), (-5, 10), (-1, 10), (12, 8), (-15, 10),
           (-20, 0), (-15, -15), (-15, -15), (-15, -15), (-15, -15), (-15, -15)]

# Asegurarse de que las columnas estén en el formato correcto
columnas_esperadas = ["Element", "h_index", "g_index", "m_index", "TC", "NP", "PY_start"]
if not all(col in df.columns for col in columnas_esperadas):
    raise ValueError("El archivo Excel no tiene las columnas esperadas.")

# Crear gráfico de dispersión
plt.figure(figsize=(12, 7))
# Una lista para guardar las instancias de texto y poder ajustarlas luego
texts = []

for index, row in df.iterrows():
    plt.scatter(row['h_index'], row['TC'], color='blue')
    texts.append(plt.text(row['h_index'], row['TC'], row['Element'], fontsize=9))

# Usa la función adjust_text para evitar superposiciones
adjust_text(texts, arrowprops=dict(arrowstyle='->', color='red'))

# Calcular y dibujar la línea de tendencia
z = np.polyfit(df['h_index'], df['TC'], 1)
p = np.poly1d(z)
plt.plot(df['h_index'], p(df['h_index']), "r--")

# Títulos y etiquetas
plt.title("Sources' Local Impact: h index vs Total Citations")
plt.xlabel('h_index')
plt.ylabel('Total Citations (TC)')

# Rejilla, ajuste de diseño y mostrar el gráfico
plt.grid(True)
plt.tight_layout()
plt.show()
'''

#ruta_archivo = 'C:\\Users\\AAVILESV\\Downloads\\Most_Relevant_Sources.xlsx'

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np  # Añade la importación de numpy para generar colores únicos

# Leer el archivo Excel
ruta_archivo = 'G:\\Mi unidad\\2024\\Msc. Jorge Vinueza\\informaciondata\\wos_source_Impact.xlsx'
df = pd.read_excel(ruta_archivo)

# Asegurarse de que las columnas estén en el formato correcto
columnas_esperadas = ["Element", "h_index", "g_index", "m_index", "TC", "NP", "PY_start"]
if not all(col in df.columns for col in columnas_esperadas):
    raise ValueError("El archivo Excel no tiene las columnas esperadas.")

# Ordenar el DataFrame por h_index en orden descendente y tomar los primeros 10 registros
df_top10 = df.sort_values(by='h_index', ascending=False).head(10)

# Generar colores únicos para cada fuente
colores = plt.cm.get_cmap('tab20', len(df_top10))

# Crear gráfico de dispersión con colores únicos
plt.figure(figsize=(12, 7))
for i, source in enumerate(df_top10['Element']):
    plt.scatter(df_top10['h_index'].iloc[i], df_top10['TC'].iloc[i], color=colores(i), s=100, label=source)

plt.title("Sources' Local Impact: h index vs Total Citations")
plt.xlabel('h_index')
plt.ylabel('Total Citations (TC)')
plt.legend()  # Mostrar etiquetas de las fuentes en la leyenda
plt.grid(True)
plt.tight_layout()
plt.show()
'''