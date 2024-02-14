def corregir_identificadores(archivo_bib):
    with open(archivo_bib, 'r', encoding='utf-8') as f:
        contenido = f.readlines()

    # Buscar y reemplazar identificadores con espacios
    for i, linea in enumerate(contenido):
        if linea.startswith("@ARTICLE{"):
            # Encuentra el índice del primer espacio después de "@ARTICLE{"
            indice_espacio = linea.find(" ", len("@ARTICLE{"))
            while indice_espacio != -1:
                # Reemplaza el espacio con un guion bajo
                linea = linea[:indice_espacio] + "" + linea[indice_espacio+1:]
                indice_espacio = linea.find(" ", indice_espacio + 1)
            contenido[i] = linea

    # Guardar el archivo corregido
    with open(archivo_bib, 'w', encoding='utf-8') as f:
        f.writelines(contenido)

if __name__ == "__main__":
    archivo_bib = 'G:\\Mi unidad\\2024\\Msc. Jorge Vinueza\\final833savedrecs.bib'
    corregir_identificadores(archivo_bib)
    print("Identificadores corregidos en el archivo .bib.")
