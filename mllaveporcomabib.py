import re

# Ruta del archivo .bib
archivo_bib ='C:\\Investigación\\Trabajo_2023\\Master Miguel Yuqui\\wosarticle466salida.bib '

# Leer el archivo .bib línea por línea
with open(archivo_bib, 'r', encoding='utf-8') as f:
    lineas = f.readlines()

# Procesar cada línea
nuevas_lineas = []
for i, linea in enumerate(lineas):
    # Si la línea tiene un igual (=), es probable que sea un campo
    if "=" in linea:
        # Reemplazar comillas dobles al principio y al final de un campo por llaves
        linea = re.sub(r'=\s*"([^"]+)"\s*,', r'= {\1},', linea)
        
        # Caso especial para el último campo antes de la llave de cierre
        if i < len(lineas) - 1 and lineas[i + 1].strip() == "}":
            linea = re.sub(r'=\s*"([^"]+)"\s*$', r'= {\1}', linea)
            
    nuevas_lineas.append(linea)

# Guardar los cambios en el archivo .bib
with open(archivo_bib, 'w', encoding='utf-8') as f:
    f.writelines(nuevas_lineas)

print('Los cambios se han guardado en el archivo .bib.')
