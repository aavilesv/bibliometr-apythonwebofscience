import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

# Crear un DataFrame con los datos proporcionados
data = {
    'From': ['ARGENTINA', 'ARGENTINA', 'ARGENTINA', 'ARGENTINA', 'ARGENTINA', 'ARGENTINA', 'ARGENTINA', 'ARGENTINA', 'ARGENTINA', 'ARGENTINA', 'ARGENTINA', 'ARGENTINA', 'ARGENTINA'],
    'To': ['AUSTRALIA', 'BOLIVIA', 'CANADA', 'CHINA', 'COSTA RICA', 'CZECH REPUBLIC', 'GUATEMALA', 'INDIA', 'IRELAND', 'ITALY', 'KOREA', 'NETHERLANDS', 'PANAMA'],
    'Frequency': [38, 39, 100, 86, 76, 65, 24, 85, 63, 26, 62, 89, 31]
}
df = pd.DataFrame(data)

# Coordenadas de los países
country_coords = {
    'ARGENTINA': (-34, -64),
    'AUSTRALIA': (-25, 135),
    'BOLIVIA': (-17, -65),
    'CANADA': (56, -106),
    'CHINA': (35, 105),
    'COSTA RICA': (10, -84),
    'CZECH REPUBLIC': (49.8, 15.5),
    'GUATEMALA': (15.7, -90.3),
    'INDIA': (21, 78),
    'IRELAND': (53, -8),
    'ITALY': (42.8, 12.8),
    'KOREA': (37, 127.5),
    'NETHERLANDS': (52.3, 5.7),
    'PANAMA': (9, -80)
}

# Contar las relaciones por país

relation_counts = pd.concat([df['From'], df['To']]).value_counts().to_dict()

# Crear el mapa
fig, ax = plt.subplots(figsize=(15, 10))
m = Basemap(projection='merc', llcrnrlat=-60, urcrnrlat=80, llcrnrlon=-180, urcrnrlon=180, resolution='c')
m.drawcoastlines()
m.drawcountries()
m.drawmapboundary(fill_color='aqua')
m.fillcontinents(color='lightgreen',lake_color='aqua')

# Dibujar las relaciones entre países con flechas dobles
for _, row in df.iterrows():
    from_country = row['From']
    to_country = row['To']
    from_coords = country_coords[from_country]
    to_coords = country_coords[to_country]
    
    x1, y1 = m(from_coords[1], from_coords[0])
    x2, y2 = m(to_coords[1], to_coords[0])
    
    m.drawgreatcircle(from_coords[1], from_coords[0], to_coords[1], to_coords[0], linewidth=2, color='blue')

# Colorear los países en función de la cantidad de relaciones
for country, coords in country_coords.items():
    if country in relation_counts:
        count = relation_counts[country]
        color = plt.cm.viridis(count / max(relation_counts.values()))
        m.drawcountries(linewidth=2, color=color)

plt.title("Relaciones entre países")
plt.show()
