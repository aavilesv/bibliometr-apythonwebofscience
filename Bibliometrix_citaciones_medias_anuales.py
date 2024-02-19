import matplotlib.pyplot as plt
import pandas as pd

# Data provided by the user
data = {
    "Year": [2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023],
    "MeanTCperArt": [18.84, 25.11, 31.81, 22.7, 21.96, 35.22, 21.69, 13.22, 13.11, 4.01, 1.76],
    "N": [31, 27, 27, 27, 47, 54, 52, 77, 152, 175, 161],
    "MeanTCperYear": [1.57, 2.28, 3.18, 2.52, 2.74, 5.03, 3.62, 2.64, 3.28, 1.34, 0.88]
}

# Create DataFrame
df = pd.DataFrame(data)
# Define the offset for positioning the data labels for MeanTCperArt
mean_tc_per_art_offsets = [(-5, 10), (-5, 10), (-1, 10), (12, 8), (-15, 10),
                           (-20, 0), (-15, -15), (-15, -15), (-15, -15), (-15, -15), (-15, -15)]

# Define the offset for positioning the data labels for MeanTCperYear
mean_tc_per_year_offsets = [(-5, 7), (-8, 15), (0, 8), (8, 10), (15, -15),
                            (20, -15), (15, 10), (4, 12), (0, 10), (15, 10), (5, 10)]


# Create figure and axis objects with subplots()
fig, ax = plt.subplots(figsize=(15, 7))

# Bar plot for the number of articles
bars = ax.bar(df["Year"], df["N"], color="skyblue", width=0.65, label="Number of Items")

# Adding data labels to the bars
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2.0, yval, int(yval), va='bottom', ha='center', fontsize=10)

# Line plot for MeanTCperArt
ax2 = ax.twinx()
line1, = ax2.plot(df["Year"], df["MeanTCperArt"], color="darkslategrey", marker="o", label="MeanTCperArt", linestyle='--')

# Añadir etiquetas de datos al gráfico de líneas para MeanTCperArt
for i, (txt, (dx, dy)) in enumerate(zip(df["MeanTCperArt"], mean_tc_per_art_offsets)):
    ax2.annotate(f"{txt:.2f}", (df["Year"][i], df["MeanTCperArt"][i]), textcoords="offset points", 
                 xytext=(dx, dy), ha='center', fontsize=10)
#Gráfico lineal de la media anual de TCT
ax3 = ax.twinx()
line2, = ax3.plot(df["Year"], df["MeanTCperYear"], color="green", marker="s", label="MeanTCperYear")
ax3.spines["right"].set_position(("axes", 1.15))  # Offset the right spine of ax3

# Añadir etiquetas de datos al gráfico de líneas para MeanTCperYear

for i, (txt, (dx, dy)) in enumerate(zip(df["MeanTCperYear"], mean_tc_per_year_offsets)):
    ax3.annotate(f"{txt:.2f}", (df["Year"][i], df["MeanTCperYear"][i]), textcoords="offset points", 
                 xytext=(dx, dy), ha='center', fontsize=10)
# Establecer las etiquetas del eje y
ax.set_ylabel('Number of Items', fontsize=14, color='black')
ax2.set_ylabel('Average number of citations per article', fontsize=14, color='black')
ax3.set_ylabel('Average Number of Citations per Year', fontsize=14, color='black')

# Establecer la etiqueta del eje x
ax.set_xlabel('Year', fontsize=14, color='black')


# Establecer el título
plt.title('Bibliometric Study: Articles and Citations by Year', fontsize=16)

# Establecer la leyenda
ax.legend(loc='upper left')
ax2.legend(loc='upper right')
ax3.legend(loc='center right')

# Ajustar el diseño para hacer espacio para las etiquetas
plt.tight_layout()

# Show plot
plt.show()
