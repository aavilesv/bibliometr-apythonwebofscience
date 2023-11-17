import pandas as pd
import plotly.graph_objects as go

df=pd.read_excel('C:\\Users\\AAVILESV\\Downloads\\wosThematic_Evolution.xlsx')


# Convertir las etiquetas "From" y "To" a índices numéricos
all_nodes = df["From"].tolist() + df["To"].tolist()
unique_nodes = list(set(all_nodes))
source_indices = [unique_nodes.index(x) for x in df["From"].tolist()]
target_indices = [unique_nodes.index(x) for x in df["To"].tolist()]

# Etiquetas para los nodos con palabras y valores
from_labels = [f"{node} ({word})" for node, word in zip(df["From"], df["Words"])]
to_labels = df["To"].tolist()

node_labels = from_labels + to_labels

# Crear el diagrama de Sankey
fig = go.Figure(data=[go.Sankey(
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color="black", width=0),
        label=node_labels
    ),
    link=dict(
        source=source_indices,
        target=target_indices,
        value=df["Weighted Inclusion Index"].tolist(),
        label=df["Words"].tolist()  # Etiquetas para los enlaces
    )
)])

fig.update_layout(title_text="Diagrama de Sankey", font_size=10)
fig.show()