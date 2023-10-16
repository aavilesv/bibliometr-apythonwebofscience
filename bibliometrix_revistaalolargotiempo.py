import pandas as pd
import matplotlib.pyplot as plt

# Leer el archivo Excel
df = pd.read_excel("C:\\Users\\AAVILESV\\Downloads\\Source_Dynamics.xlsx")

# Establecer el año como índice
df.set_index('Year', inplace=True)

# Graficar
plt.figure(figsize=(14, 8))
for column in df.columns:
    plt.plot(df.index, df[column], marker='o', linestyle='-', linewidth=2, label=column)

# Configuración del gráfico
plt.title("Sources' Production over Time")
plt.xlabel('Year')
plt.ylabel('Number of Publications')
plt.xticks(df.index)  # Asegurarse de que todos los años estén en el eje x
plt.legend(loc='upper left', bbox_to_anchor=(1.05, 1))
plt.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.6)
plt.tight_layout()
plt.axhline(0, color='black',linewidth=0.5)  # Línea horizontal en y=0 para enfatizar la línea de tiempo
plt.show()
