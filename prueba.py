#librerias necesarias para este ejercicio
import pandas as pd
#import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import random
i = 0
lim = 11

#calculamos la ruta mas corta entre 2 antenas de red de telefonia celular
#importamos los datos  de un archivo .csv y los convertimos en un DataFrame
for i in range(lim):
    diccionario = {'antenas': 'a'[i+1]}
        

print(diccionario['antenas'])
# DF = pd.read_csv('antenas.csv', index_col=None)

# #generamos la grafica a partir del DataFrame con los datos
# antenas = nx.from_pandas_edgelist(DF, source='origen', target='destino', edge_attr='distancia entre antenas (m)')
# #nodos del grafo
# antenas.nodes()
# #aristas del grafo
# antenas.edges()
# #orden del grafo
# antenas.order()

# #nodos con mas de una conexion
# for x in antenas.nodes():
#     if antenas.degree(x) > 2:
#         #imprimimos los nodos con mas de 2 conexiones
#         print(x)

# #ejecutamos el algoritmo de Dijkstra
# camino = nx.dijkstra_path(antenas, source='A1', target='A11', weight=True)

# #funcion para imprimir el grafo con el camino mas corto resaltado
# def plot_shortest_path(camino):
#     #imprimimos el resultado que nos da el algoritmo
#     print(camino)

#     #definimos que el grafo va a tener una forma circular
#     positions = nx.circular_layout(antenas)

#     #nos dibuja el grafo completo antes de resaltar la ruta mas corta, que para nuestro caso seria de la antena A1 a la A11
#     nx.draw(antenas, pos = positions,with_labels=True, node_size = 500, width = 2, node_color='lightblue', edge_color='gray')

#     #la variable short_path nos inicia la funcion para graficar el camino mas corto
#     short_path = nx.DiGraph()

#     #le indicamos que de la variable camino agrege las conexiones al camino mas corto
#     for i in range(len(camino)-1):
#         short_path.add_edge(camino[i], camino[i+1])

#     #resaltamos el camino mas corto cambiando el formato de los nodos y las aristas
#     nx.draw(short_path, pos = positions,with_labels=True, node_size = 500, width = 4, node_color='#ff5733', edge_color='#f0b206')

#     #imprime el grafo con el camino mas corto resaltado
#     plt.show()

# #ejecutamos la funcion plot_shortest_path()
# plot_shortest_path(camino)



