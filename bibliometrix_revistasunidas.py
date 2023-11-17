import pandas as pd
data=pd.read_excel('C:\\Users\\AAVILESV\\Downloads\\revistaunidas.xlsx')

# Agrupa por la columna 'Sources' y realiza las operaciones necesarias en las otras columnas
result = data.groupby('Sources').agg({
    'Articles': 'sum',                     # Suma los valores en 'Articles'
    'Basedatos': lambda x: '/'.join(x)     # Combina las cadenas de 'Basedatos' con '/'
})


# Para guardar el DataFrame en un archivo Excel, usas el método to_excel
result.to_excel('C:\\Users\\AAVILESV\\Downloads\\revistawosscopus.xlsx', sheet_name='revistawosscopus', index=True)
