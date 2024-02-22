import pandas as pd
import matplotlib.pyplot as plt

# Leer el archivo Excel
df = pd.read_excel("G:\\Mi unidad\\2024\\Msc. Jorge Vinueza\\informaciondata\\scopus_Source_Dynamics.xlsx")

# Establecer el año como índice
df.set_index('Year', inplace=True)

# Plotting the graph with the legend inside
plt.figure(figsize=(14, 8))

for column in df.columns:
    plt.plot(df.index, df[column], marker='o', linestyle='-', linewidth=2, label=column)

# Configuration of the graph with the legend inside the plot area
plt.title("Sources' Production over Time")
plt.xlabel('Year')
plt.ylabel('Number of Publications')
plt.xticks(df.index)
plt.legend(loc='upper left')  # Move the legend to the upper left inside the plot area
plt.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.6)
plt.tight_layout()

# Display the plot
plt.show()