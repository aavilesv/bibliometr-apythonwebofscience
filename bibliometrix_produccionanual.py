import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
#df = pd.read_excel('C:\\Users\\AAVILESV\\Downloads\\Author_Production_Over_Time.xlsx')
# Datos de Web of Science
data_web_of_science = {
    'Year': [2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023],
    'Web of Science Articles': [31, 27, 27, 27, 47, 54, 52, 77, 152, 175, 161]
}

df_web_of_science = pd.DataFrame(data_web_of_science)

# Datos de Scopus
data_scopus = {
    'Year': [2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023],
    'Scopus Articles': [52, 55, 60, 58, 75, 84, 103, 175, 341, 455, 400]
}

df_scopus = pd.DataFrame(data_scopus)

# Configurar el estilo de Seaborn
sns.set_theme(style="whitegrid")

# Calcular un pequeño desplazamiento vertical para evitar la superposición
offset = 10

# Graficar ambas series de datos en el mismo gráfico con desplazamiento vertical
plt.figure(figsize=(10, 6))
ax = sns.lineplot(x='Year', y='Web of Science Articles', data=df_web_of_science, marker='o', label='Web of Science', ci=None)
ax2 = sns.lineplot(x='Year', y='Scopus Articles', data=df_scopus, marker='o', label='Scopus', ci=None)

# Agregar etiquetas a los valores de arriba de la línea
for x, y in zip(df_web_of_science['Year'], df_web_of_science['Web of Science Articles']):
    ax.annotate(f'{y}', (x, y+offset), textcoords='offset points', xytext=(0,-5), ha='center')

# Agregar etiquetas a los valores de abajo de la línea
for x, y in zip(df_scopus['Year'], df_scopus['Scopus Articles']):
    ax2.annotate(f'{y}', (x, y-offset), textcoords='offset points', xytext=(0,15), ha='center')

plt.title('Articles per year', fontsize=14, color='black')
plt.xlabel('Year', fontsize=12, color='black')
plt.ylabel('Number of articles', fontsize=12, color='black')
plt.legend()
plt.tight_layout()
plt.show()


'''
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Datos de Web of Science
data_web_of_science = {
    'Year': [2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023],
    'Web of Science Articles': [31, 27, 27, 27, 47, 54, 52, 77, 152, 175, 161]
}
df_web_of_science = pd.DataFrame(data_web_of_science)

# Datos de Scopus
data_scopus = {
    'Year': [2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023],
    'Scopus Articles': [52, 55, 60, 58, 75, 84, 103, 175, 341, 455, 400]
}
df_scopus = pd.DataFrame(data_scopus)

# Configurar el estilo de Seaborn
sns.set_theme(style="whitegrid")

# Configuración de la figura
plt.figure(figsize=(10, 6))
ax = sns.lineplot(x='Year', y='Web of Science Articles', data=df_web_of_science, marker='o', label='Web of Science', ci=None, color='blue', linestyle='-')
ax2 = ax.twinx()  # Crea un segundo eje Y que comparte el mismo eje X
sns.lineplot(x='Year', y='Scopus Articles', data=df_scopus, marker='o', label='Scopus', ci=None, color='green', linestyle='--', ax=ax2)

# Ajustes en las etiquetas y títulos
plt.title('Comparativa de Artículos por Año entre Web of Science y Scopus')
ax.set_xlabel('Año')
ax.set_ylabel('Número de artículos en Web of Science', color='blue')
ax2.set_ylabel('Número de artículos en Scopus', color='green')

# Ajustar leyendas para mejorar la legibilidad
ax.legend(loc='upper left')
ax2.legend(loc='upper right')

# Evitar superposición de etiquetas y leyendas
plt.tight_layout()

# Mostrar el gráfico
plt.show()
'''