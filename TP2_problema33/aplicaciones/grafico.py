import networkx as nx
import matplotlib.pyplot as plt
from TP2_problema33.modulos.Grafo import Grafo

mi_grafo = Grafo()
G = nx.Graph()
with open("rutas.txt", "r") as archivo:
    for linea in archivo:
        linea = linea.rstrip()
        datos = linea.split(",")
        if len(datos) == 4:
            ciudad_origen, ciudad_destino, peso, precio = datos
            peso = int(peso)
            precio = int(precio)  # Convierte la segunda ponderación a entero
            G.add_edge(ciudad_origen, ciudad_destino, weight=peso, second_weight=precio)

pos = nx.spring_layout(G)
labels = {vertice.obtenerId(): vertice.obtenerId() for vertice in mi_grafo}
edge_labels = {(u, v): f'{d["weight"]}/{d["second_weight"]}' for u, v, d in G.edges(data=True)}
nx.draw(G, pos, with_labels=True, node_size=500, node_color='skyblue', font_size=7, font_color='black')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
nx.draw_networkx_labels(G, pos, labels=labels)
plt.title("Grafo")
plt.show()