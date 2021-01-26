# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 16:32:32 2021

@author: quent
"""

###################### 3-Coloration ######################

import networkx as nx 
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp 
#import des librairies necessaires

node_number = 10
initial_nodes = 2
G = nx.barabasi_albert_graph(node_number, initial_nodes)
#génération d'un graphe en fonction du nombres de points

mat = nx.adjacency_matrix(G)
print("Matrice d'adjacence (commence à 0) : ")
print(mat.todense())
#matrice d'adjacence pour faire les calculs
#affichage de la matrice pour faire des vérifications


colmatrix = []
for i in range(node_number):
    colmatrix.append('r')
#on colorise tous les vertices en rouge

for i in range (mat.shape[0]):
    for j in range (mat.shape[1]): 
        if mat[i,j] == 1:
            if colmatrix[i]==colmatrix[j]:#les couleurs de colorisation sont :
                if colmatrix[i] == 'r':   #rouge vert bleu
                    colmatrix[j] = 'g'    #le jaune est la couleur d'erreur
                elif colmatrix[i] == 'g':
                    colmatrix[j] = 'b'
                elif colmatrix[i] == 'b':
                    colmatrix[j] = 'r'
#algo qui parcourt toute la matrice et colorise en foncrtion des voisins                    

'''
for i in range (0,mat.shape[0]):
    for j in range (0,i): #on peut le faire terminer à i-1 peut-être
        if mat[i,j] == 1:
            if colmatrix[i]==colmatrix[j]:
                if colmatrix[i] == 'r':
                    colmatrix[j] = 'g'
                elif colmatrix[i] == 'g':
                    colmatrix[j] = 'b'
                elif colmatrix[i] == 'b':
                    colmatrix[j] = 'r'
'''
#algo qui parcourt la moitié de la matrice (car elle est symétrique)
#c'est un autre algo, mais il fonctionne moins bien que le précédent


for i in range (mat.shape[0]):
    for j in range (mat.shape[1]): 
        if mat[i,j] == 1:
            if colmatrix[i]==colmatrix[j]:
                colmatrix[j] = 'y'
print("ECHEC de la 3-coloration (les noeuds non colorisables sont affichés en jaune)")
#Algo de vérification de la bonne colorisation du graphe

my_pos = nx.spring_layout(G, seed = 100)
nx.draw(G, pos = my_pos, with_labels=True, node_color= colmatrix, node_size=1000, edge_color='black', linewidths=10, font_size=30)
#affichage du graphe (pos ne sert que si l'on utilise toujours le même graphe)









