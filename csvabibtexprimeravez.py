import csv

def csv_to_bibtex(csv_filename, bibtex_filename):
    with open(csv_filename, 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        
        with open(bibtex_filename, 'w', encoding='utf-8') as bibtex_file:
            for row in csv_reader:
                bibtex_file.write("@article{{,\n")
                
                for key, value in row.items():
                    # Convertir cada columna del CSV en un campo BibTeX
                    bibtex_file.write(f"    {key} = {{{value}}},\n")
                
                bibtex_file.write("}\n\n")

if __name__ == "__main__":
    csv_path = "C:\\Investigación\\Trabajo_2023\\Msc. Isabel Leal\\Búsqueda 1\\finalbibliometriascopus.csv"
    bibtex_path = csv_path.replace(".csv", ".bib")
    
    csv_to_bibtex(csv_path, bibtex_path)
    print(f"Conversión completada. El archivo .bib ha sido guardado en: {bibtex_path}")
