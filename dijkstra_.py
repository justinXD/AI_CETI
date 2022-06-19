import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import random

c1 = random.randint(1,200)
c2 = random.randint(1,200)
c3 = random.randint(1,200)
c4 = random.randint(1,200)
c5 = random.randint(1,200)
c6 = random.randint(1,200)
c7 = random.randint(1,200)
c8 = random.randint(1,200)
c9 = random.randint(1,200)
c10 = random.randint(1,200)
c11 = random.randint(1,200)
c12 = random.randint(1,200)
c13 = random.randint(1,200)
c14 = random.randint(1,200)
c15 = random.randint(1,200)
c16 = random.randint(1,200)

nodos={'A1','A2','A3','A4','A5','A6','A7','A8','A9','A10','A11','A12'}


aristas = [('A1', 'A2', c1), ('A2', 'A3', c3), 
     ('A2', 'A5', c9), ('A3', 'A4', c10),
     ('A3', 'A6', c12), ('A4', 'A8', c11), 
     ('A5', 'A9', c8), ('A6', 'A9', c2), 
     ('A6', 'A9', c4), ('A6', 'A7', c6), 
     ('A7', 'A10', c5), ('A7', 'A8', c7),
     ('A8','A11',c12),('A9','A10',c13),('A10','A11',c14),
     ('A10','A12',c15),('A11','A12',c16)]

G=nx.DiGraph()
G.add_nodes_from(nodos)
G.add_weighted_edges_from(aristas)

pos={'A1':[0,10],'A2':[1,5],'A3':[1,0],'A4':[1,-3],'A5':[3,10],
   'A6':[2,5],'A7':[4,1],'A8':[6,-2],'A9':[6,11],'A10':[7,7],'A11':[7,1],'A12':[7,11]}


weight=nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=weight)
nx.draw(G, pos=pos, with_labels=True)

best= nx.dijkstra_path(G, 'A1', 'A11')
print("la mejor ruta es la siguiente:")
print(best)
best_road = nx.DiGraph()

for i in range(len(best)-1):
    best_road.add_edge(best[i], best[i+1])
    

nx.draw(best_road, pos=pos,with_labels = True, node_size = 500, width = 4, node_color = '#ff5733',edge_color = '#f0b206')
plt.show()