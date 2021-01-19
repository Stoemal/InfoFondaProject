# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 14:31:37 2021

@author: quent
"""

import networkx as nx 
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
#import des librairies


G=nx.Graph()
G.add_nodes_from([("a",{"col": "blue"}),
                  ("b",{"col": "red"}),
                  ("c",{"col": "red"}),
                  ("d",{"col": "red"}),
                  ("e",{"col": "blue"}),
                  ("f",{"col": "red"}),
                  ("g",{"col": "blue"}),
                  ("h",{"col": "green"}),                  
                  ])
#déclaration des noeuds et de leurs attributs

col_list = nx.get_node_attributes(G, "col")
#lectures des attributs

colle = [col_list.get(node) for node in G.nodes()]
#//////////////////////////////////////////////////////
G.add_edges_from([("a","b"),
                  ("a","c"),
                  ("b","d"),
                  ("d","e"),
                  ("e","f"),
                  ("e","g"),
                  ("h","d"),
                  ("h","b"),
                  ("c","g"),
                  ])
#déclaration des edges




cool = {n : {'col' : 'black'} for n in G.nodes()}
#G.nodes['b']['col'] = "black"
#cool = {'a' : {'col' : 'black'}}
#creation d'attributs

print(G.nodes.data())
#permet d'afficher les attributs des noeuds

nx.set_node_attributes(G,cool)
#attribution d'attributs

coo = [col_list.get(node) for node in G.nodes()]

for i in range(len(coo)):
    print(coo[i])





matrice = nx.adjacency_matrix(G)
#print (matrice.todense())
#print (matrice)


#nx.draw(G,with_labels=True)
my_pos = nx.spring_layout(G, seed = 100)
nx.draw(G, pos = my_pos, with_labels=True, node_color= colle, node_size=1000, edge_color='black', linewidths=10, font_size=30)
#plt.show()
#affichage du graphe
