import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Datos de Web of Science
data_web_of_science = {
    'Year': [2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023],
    'Web of Science Articles': [31, 27, 27, 27, 47, 54, 52, 77, 153, 174, 131]
}

df_web_of_science = pd.DataFrame(data_web_of_science)

# Datos de Scopus
data_scopus = {
    'Year': [2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023],
    'Scopus Articles': [51, 57, 60, 63, 80, 87, 104, 184, 357, 465, 333]
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

plt.title('Artículos por año')
plt.xlabel('Año')
plt.ylabel('Número de artículos')
plt.legend()
plt.tight_layout()
plt.show()
