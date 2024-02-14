# -*- coding: utf-8 -*-
"""
Created on Wed May 10 14:16:47 2023
@author: AAVILESV
"""
import bibtexparser

def limpiar_caracteres(archivo_bib):
    try:
        with open(archivo_bib, 'r', encoding='utf-8') as f:
            contenido = f.read()

        contenido = contenido.replace('\x05', '')  # Reemplaza '\x05' con el carácter no deseado

        with open(archivo_bib, 'w', encoding='utf-8') as f:
            f.write(contenido)
        print('Archivo limpiado y guardado con codificación UTF-8.')
    except Exception as e:
        print(f"Error al limpiar el archivo {archivo_bib}: {e}")

def procesar_bib(archivo_bib):
    try:
        with open(archivo_bib, encoding='utf-8') as bibtex_file:
            bib_database = bibtexparser.load(bibtex_file)

        for entry in bib_database.entries:
            if entry['ENTRYTYPE'] == 'article':
                if 'keywords' in entry and 'author_keywords' not in entry:
                    entry['author_keywords'] = entry['keywords'].lower()
                elif 'keywords' in entry and 'author_keywords' in entry:
                    keywords = entry['keywords']
                    author_keywords = entry['author_keywords']
                    entry['author_keywords'] = f"{keywords.lower()}; {author_keywords.lower()}"

        with open(archivo_bib, 'w', encoding='utf-8') as bibtex_file:
            bibtexparser.dump(bib_database, bibtex_file)
        print('Los cambios se han guardado en el archivo .bib.')
    except Exception as e:
        print(f"Error al procesar el archivo {archivo_bib}: {e}")

# Usar las funciones definidas
archivo_bib_path = 'C:\\Investigación\\Trabajo_2023\\Master Miguel Yuqui\\scopussalid.bib'
limpiar_caracteres(archivo_bib_path)
procesar_bib(archivo_bib_path)
