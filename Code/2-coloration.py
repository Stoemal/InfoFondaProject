# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 14:27:37 2021

@author: Mehdi
"""


import networkx as nx
import matplotlib.pyplot as plt

#On définit un graphe avec la méthode de barabasi albert
#Cette méthode permet de créer un graphe de manière aléatoire
G = nx.Graph()
node_number = 50   #nombre de sommets
initial_nodes = 1   #nombre de sommets à rattacher à un sommet en particulier
G = nx.barabasi_albert_graph(node_number, initial_nodes)

#On crée un tableau de couleurs noires
colors = []
for i in range (node_number):
    colors.append('k')   #couleur noire

#On crée la matrice d'adjacence du graphe G
matrice = nx.adjacency_matrix(G)
print(matrice.todense(G))


#On utilise 2 couleurs : rouge et bleue
#[i, j] affiche ligne par ligne
for i in range(1,matrice.shape[0]):
    for j in range(0, i):
        if matrice[i, j] == 1:  #le 1 signifie que 2 sommets sont liés dans la matrice
            if colors[i] == 'k':
                if colors[i] == colors[j]:
                    colors[i] = 'r'
                    colors[j] = 'b'
                elif colors[j] == 'r':
                    colors[i] = 'b'
                elif colors[j] == 'b':
                    colors[i] = 'r'
            else :
                 if colors[i] == 'r':
                     if colors[i] == colors[j]:
                         colors[j] = 'b'
                 else:
                     if colors[i] == colors[j]:
                         colors[j] = 'r'


#Renvoie true si le problème 2-coloration est résolu (avec du rouge et du bleu) et false sinon
def test(tab_color):
    a = True
    for i in range(0,matrice.shape[0]):
        for j in range(0,matrice.shape[1]):
            if matrice[i, j] == 1:
                if tab_color[i] == tab_color[j] :
                    a = False
                    break
    return a


#Si le graphe est faux on colorie tous les sommets en noir
if test(colors) == False:
    for i in range(len(colors)):
        colors[i] = 'k'

#On génère une image du graphe dans la console puis on l'enregistre
nx.draw(G, node_color=colors, with_labels=True)
plt.savefig("graphe_2coloration_test.png")





#Ci-dessous trois algorithmes permettant de résoudre le problème 2-colorations

"""
En définissant le graphe en rouge dès le départ

for i in range(matrice.shape[0]):
    for j in range(matrice.shape[1]):
        if matrice[i, j] == 1:
            if colors[i] == colors[j]:
                if colors[i] == 'r' : colors[j] = 'b'
                elif colors [i] == 'b' : colors[j] = 'r'



for i in range(1,matrice.shape[0]):
    for j in range(0, i):
        if matrice[i, j] == 1:
            if colors[i] == 'k':
                if colors[i] == colors[j]:
                    colors[i] = 'r'
                    colors[j] = 'b'
                elif colors[j] == 'r':
                    colors[i] = 'b'
                elif colors[j] == 'b':
                    colors[i] = 'r'
            else :
                 if colors[i] == 'r':
                     if colors[i] == colors[j]:
                         colors[j] = 'b'
                 else:
                     if colors[i] == colors[j]:
                         colors[j] = 'r'



for i in range(0,matrice.shape[0]):
    for j in range(0,matrice.shape[1]):
        if matrice[i, j] == 1:
            if colors[i] == 'k':
                if colors[i] == colors[j]:
                    colors[i] = 'r'
                    colors[j] = 'b'
                elif colors[j] == 'r':
                    colors[i] = 'b'
                elif colors[j] == 'b':
                    colors[i] = 'r'
            else :
                 if colors[i] == 'r':
                     if colors[i] == colors[j] or colors[j] == 'k':
                         colors[j] = 'b'
                 else:
                     if colors[i] == colors[j] or colors[j] == 'k':
                         colors[j] = 'r'

"""

