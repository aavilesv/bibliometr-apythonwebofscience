"""
Created on Wed May 10 14:16:47 2023

@author: AAVILESV
"""
#pip install pybtex
   
from pybtex.database import parse_file

try:
    archivo_bib = 'C:\\Investigación\\Trabajo_2023\\Msc. Isabel Leal\\Búsqueda 1\\originalbibliometriascopusnew1.bib'
    
    # Parsear el archivo .bib
    bib_data = parse_file(archivo_bib)

    def limpiar_caracteres(archivo_bib):
        with open(archivo_bib, 'r', encoding='utf-8') as f:
            contenido = f.read()

        # Reemplaza los caracteres no deseados
        contenido = contenido.replace('\x05', '')  # Reemplaza '\x05' con el carácter no deseado

        with open(archivo_bib, 'w', encoding='utf-8') as f:
            f.write(contenido)

    limpiar_caracteres(archivo_bib)

    for clave, entrada in bib_data.entries.items():
        if 'keywords' in entrada.fields and 'author_keywords' in entrada.fields:
            keywords = entrada.fields['keywords']
            author_keywords = entrada.fields['author_keywords']
            
            # Separa las palabras clave en author_keywords y keywords
            author_keywords_list = author_keywords.split(';')
            keywords_list = keywords.split(';')
            
            # Elimina las palabras clave de keywords que ya están en author_keywords
            for kw in author_keywords_list:
                if kw.strip().lower() in keywords_list:
                    keywords_list.remove(kw.strip().lower())
            
            # Une las palabras clave de keywords a author_keywords
            entrada.fields['author_keywords'] = "; ".join(author_keywords_list + keywords_list).strip()

    # Guarda los cambios en el archivo .bib
    with open(archivo_bib, 'w', encoding='utf-8') as archivo:
        archivo.write(bib_data.to_string('bibtex'))
    print('Los cambios se han guardado en el archivo .bib.')

except Exception as e:
    print(f"Error al analizar el archivo {archivo_bib}: {e}"),
