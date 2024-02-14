import pandas as pd
import matplotlib.pyplot as plt

# Rutas a los archivos de Excel
archivo_excel_scopus = 'G:\\Mi unidad\\2024\\Msc. Jorge Vinueza\\_1908scopusalid.xlsx'
archivo_excel_wos = 'G:\\Mi unidad\\2024\\Msc. Jorge Vinueza\\_final833savedrecsalid.xlsx'

# Cargar los archivos de Excel
df_scopus = pd.read_excel(archivo_excel_scopus)
df_wos = pd.read_excel(archivo_excel_wos)

# Extraer y limpiar el número de citas para Scopus
df_scopus['citations_scopus'] = df_scopus['note'].str.extract(r'Cited by: (\d+)')
df_scopus['citations_scopus'] = pd.to_numeric(df_scopus['citations_scopus'], errors='coerce').fillna(0).astype(int)

# Asegurarse de que el número de citas es un entero para Web of Science
df_wos['citations_wos'] = pd.to_numeric(df_wos['number-of-cited-references'], errors='coerce').fillna(0).astype(int)

# Limpiar el campo 'issn' quitando el guion
df_scopus['issn'] = df_scopus['issn'].str.replace('-', '', regex=False)
df_wos['issn'] = df_wos['issn'].str.replace('-', '', regex=False)

# Seleccionar las columnas relevantes para la comparación y mantener los campos de citas separados
columns_to_select = ['title', 'abstract', 'journal', 'year', 'doi', 'language', 'issn']
columns_to_compare = ['doi']

# Agregar los campos de citas a los DataFrames
df_scopus_selected = df_scopus[columns_to_select + ['citations_scopus']]
df_wos_selected = df_wos[columns_to_select + ['citations_wos']]

# Unir ambos DataFrames
combined_df = pd.concat([df_scopus_selected, df_wos_selected], ignore_index=True)
df_undido = combined_df.sort_values(by='title')

# Guardar el DataFrame consolidado en un nuevo archivo Excel
output_file = 'G:\\Mi unidad\\2024\\Msc. Jorge Vinueza\\consolidadovundido.xlsx'
df_undido.to_excel(output_file, index=False)

print(f"El archivo consolidado ha sido guardado como {output_file}.")
