import pandas as pd
import re
# Cargar los archivos
df_wos = pd.read_csv('C:\\Investigación\\Trabajo_2023\\Dr. Patricio Alvarez\\Revista Información, cultura y sociedad\\Dato\\archivocsvfinal.csv')
# Crear una nueva columna 'affiliations_modified' con los valores originales de 'affiliations'
df_wos['journal_modified'] = df_wos['journal']
# Convertir todo a mayúsculas
df_wos['journal_modified'] = df_wos['journal_modified'].astype(str)  # Convertir a cadena
df_wos['journal_modified'] = df_wos['journal_modified'].str.upper()
# Reemplazar caracteres especiales en la columna "journal_modified"
df_wos['journal_modified'] = df_wos['journal_modified'].apply(lambda x: re.sub(r'[^A-Z0-9]+', ' ', x).strip())
# Obtener el número total de revistas únicas

total_unique_journals = df_wos['journal_modified'].nunique()
# Obtener el número total de registros en el archivo
total_records = len(df_wos)

print(f"Total de revistas únicas: {total_unique_journals}")
print(f"Total de registros en el archivo: {total_records}")

# Contar el total y obtener el nombre de las revistas
journal_counts = df_wos['journal_modified'].value_counts()
output_path = 'C:\\Investigación\\Trabajo_2023\\Dr. Patricio Alvarez\\Revista Información, cultura y sociedad\\Dato\\revistatotal.csv'
#journal_counts.to_csv(output_path, header=['Total de Documentos'], index_label='Nombre de la Revista')

#print(journal_counts)