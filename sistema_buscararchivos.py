import os
import fnmatch

def buscar_archivos(directorio, patrones=["*843*.xls", "*Author_Productio*.xlsx", "*843*.csv", "*843*.bib"]):
    archivos_encontrados = []

    for raiz, dirs, archivos in os.walk(directorio):
        for patron in patrones:
            for archivo in fnmatch.filter(archivos, patron):
                archivos_encontrados.append(os.path.join(raiz, archivo))

    return archivos_encontrados

directorio_inicio = '.'  # Buscará en el directorio actual y sus subdirectorios
resultados = buscar_archivos(directorio_inicio)

for archivo in resultados:
    print(archivo)
