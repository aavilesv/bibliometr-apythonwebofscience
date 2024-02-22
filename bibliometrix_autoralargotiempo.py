import pandas as pd
import matplotlib.pyplot as plt

# Leer el archivo Excel
df = pd.read_excel('G:\\Mi unidad\\2024\\Msc. Jorge Vinueza\\informaciondata\\_wos_Author_Production_Over_Time.xlsx')

# Imprimir los nombres de las columnas

# Crear un gráfico de líneas para cada autor
authors = df['Author'].unique()
plt.figure(figsize=(15, 8))

for author in authors:
    subset = df[df['Author'] == author]
    plt.plot(subset['year'], subset['TC'], label=author, marker='o')

# Preparar los datos
df_pivot = df.pivot(index='year', columns='Author', values='TC').fillna(0)

# Gráfico de barras apiladas
ax = df_pivot.plot(kind='bar', stacked=True, figsize=(15, 7), cmap="tab20c")

# Establecer título y etiquetas
ax.set_title("Authors' Production Over Time", fontsize=16)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Number of Publications', fontsize=14)
ax.legend(title='Author', bbox_to_anchor=(1.05, 1), loc='upper left')

# Mostrar el gráfico
plt.tight_layout()
plt.show()