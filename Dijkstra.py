import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

#calculamos la ruta mas corta entre 2 antenas de red de telefonia celular
#importamos los datos y los convertimos en un DataFrame
DF = pd.read_csv('antenas.csv', index_col=None)

#generamos la grafica a partir del DataFrame con los datos
antenas = nx.from_pandas_edgelist(DF, source='origen', target='destino', edge_attr='distancia entre antenas (m)')
antenas.nodes()
antenas.edges()
antenas.order()

#nodos con mas de una conexion
for x in antenas.nodes():
    if antenas.degree(x) > 2:
        #imprimimos los nodos con mas de 2 conexiones
        print(x)

#ejecutamos el algoritmo de Dijkstra
camino = nx.dijkstra_path(antenas, source='A1', target='A11', weight=True)

#funcion para imprimir el grafo con el camino mas corto resaltado
def plot_shortest_path(camino):
    #imprimimos el resultado que nos da el algoritmo
    print(camino)
    positions = nx.circular_layout(antenas)
    nx.draw(antenas, pos = positions,with_labels=True, node_size = 500, width = 2, node_color='lightblue', edge_color='gray')

    short_path = nx.DiGraph()
    for i in range(len(camino)-1):
        short_path.add_edge(camino[i], camino[i+1])

    nx.draw(short_path, pos = positions,with_labels=True, node_size = 500, width = 4, node_color='#ff5733', edge_color='#f0b206')
    plt.show()

plot_shortest_path(camino)
#ruta = antenas.subgraph(camino)
#nx.draw(ruta, with_labels=True, node_size = 400, width = 0.3)


