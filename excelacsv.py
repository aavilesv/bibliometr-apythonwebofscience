import pandas as pd

# Ruta del archivo Excel de entrada
archivo_excel = 'C:\\Investigación\\Trabajo_2023\\Codificaciones\\universidades_latinoamerica1.xlsx'

# Ruta del archivo CSV de salida
archivo_csv = 'C:\\Investigación\\Trabajo_2023\\Codificaciones\\universidades_latinoamerica1salida.csv'

# Leer el archivo Excel
df = pd.read_excel(archivo_excel)

# Guardar el DataFrame en formato CSV
df.to_csv(archivo_csv, index=False)

print(f"El archivo Excel ha sido convertido y guardado en {archivo_csv}.")
