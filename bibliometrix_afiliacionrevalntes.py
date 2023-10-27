import matplotlib.pyplot as plt

# Datos
affiliations = ["OPEN UNIV", "KING SAUD UNIV", "UNIV TASMANIA", "GRIFFITH UNIV", "UNIV HONG KONG", 
                "UNIV SOUTHERN QUEENSLAND", "UNIV WISCONSIN", "BOISE STATE UNIV", "LA TROBE UNIV", 
                "MONASH UNIV", "UNIV CALIF IRVINE", "UNIV CENT FLORIDA", "UNIV KEBANGSAAN MALAYSIA", 
                "DEAKIN UNIV", "UNIV LEEDS"]

articles = [14, 9, 9, 8, 8, 8, 8, 7, 7, 7, 7, 7, 7, 6, 6]

# Gráfica
plt.figure(figsize=(8,8))  # Cambio de tamaño de la figura
plt.barh(affiliations, articles, color='steelblue')
plt.xlabel('Number of Articles', fontsize=12)  # Cambio de tamaño de letra
plt.ylabel('Affiliation', fontsize=12)  # Cambio de tamaño de letra
plt.title('Number of Articles by Affiliation', fontsize=14)  # Cambio de tamaño de letra
plt.gca().invert_yaxis()  # invertir el eje y para que las universidades con más artículos aparezcan arriba
plt.tight_layout()
plt.show()
