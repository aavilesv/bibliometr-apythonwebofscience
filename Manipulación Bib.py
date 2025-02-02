# -*- coding: utf-8 -*-
"""
Created on Wed May 10 14:16:47 2023
@author: AAVILESV
"""
#pip install pybtex
from pybtex.database import parse_file

try:


    archivo_bib = 'G:\\Mi unidad\\2024\\Msc. Jorge Vinueza\\final833savedrecsalid.bib'
    # Parsear el archivo .bib
    bib_data = parse_file(archivo_bib)
    # Obtener las entradas de tipo "article" o "articulo"
    def limpiar_caracteres(archivo_bib):
        with open(archivo_bib, 'r', encoding='utf-8') as f:
            contenido = f.read()

        # Reemplaza los caracteres no deseados
        contenido = contenido.replace('\x05', '')  # Reemplaza '\x05' con el carácter no deseado


        with open(archivo_bib, 'w', encoding='utf-8') as f:
            f.write(contenido)

    limpiar_caracteres(archivo_bib)
    
    #web of science
    for clave, entrada in bib_data.entries.items():
    # Verificar si la entrada es de tipo "article"
        if entrada.type == "article":
        # Si 'keywords' existe pero 'author_keywords' no, crear 'author_keywords'
            if 'keywords' in entrada.fields and 'keywords-plus' not in entrada.fields:
                entrada.fields['keywords-plus'] = entrada.fields['keywords'].lower()
            # Si ambos 'keywords' y 'author_keywords' existen, combinarlos
            elif 'keywords' in entrada.fields and 'keywords-plus' in entrada.fields:
                keywords = entrada.fields['keywords']
                keywords_plus = entrada.fields['keywords-plus']
                entrada.fields['keywords-plus'] = keywords.lower() + "; " + keywords_plus.lower()

    '''
        scopus
    
    for clave, entrada in bib_data.entries.items():
    # Verificar si la entrada es de tipo "article"
        if entrada.type == "article":
        # Si 'keywords' existe pero 'author_keywords' no, crear 'author_keywords'
            if 'keywords' in entrada.fields and 'author_keywords' not in entrada.fields:
                entrada.fields['author_keywords'] = entrada.fields['keywords'].lower()
            # Si ambos 'keywords' y 'author_keywords' existen, combinarlos
            elif 'keywords' in entrada.fields and 'author_keywords' in entrada.fields:
                keywords = entrada.fields['keywords']
                keywords_plus = entrada.fields['author_keywords']
                entrada.fields['author_keywords'] = keywords.lower() + "; " + keywords_plus.lower()
    '''
    # Guarda los cambios en el archivo .bib
    #bib_data.to_file(archivo_bib, bib_format='bibtex')
    with open(archivo_bib, 'w', encoding='utf-8') as archivo:
        archivo.write(bib_data.to_string('bibtex'))
    print('Los cambios se han guardado en el archivo .bib.')
except Exception as e:
    print(f"Error al analizar el archivo {archivo_bib}: {e}")