import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo Excel
df = pd.read_csv("C:\\Users\\AAVILESV\\Downloads\\scopusBradford_Law.csv")

df=df.head(30)
# Crear un diagrama de dispersión usando 'cumFreq'
plt.figure(figsize=(10, 6))
plt.scatter(df['SO'], df['cumFreq'], color='blue', label='cumFreq')
plt.title("Core Sources by Bradford's Law")
plt.xlabel('Source')
plt.ylabel('Cumulative Frequency')
plt.xticks(rotation=90)
plt.legend()
plt.tight_layout()
plt.show()
