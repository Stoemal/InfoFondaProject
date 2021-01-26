# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 22:40:35 2021

@author: Mehdi
"""

import networkx as nx 
import matplotlib.pyplot as plt
G=nx.Graph()


G.add_node("a")
G.add_nodes_from(["b","c"]) 

G.add_edge(1,2)
edge=("d","e")
G.add_edge(*edge)
edge=("a","b")
G.add_edge(*edge)

print("Nodesofgraph:")
print(G.nodes())
print("Edgesofgraph:")
print(G.edges())#adding a list of edges: 
G.add_edges_from([("a","c"),("c","d"),("a",1),(1,"d"),("a",2)])


nx.draw_spring(G,width=3,node_size=500,node_color='G')


nx.draw(G, linewidths=5)
#plt.savefig("simple_path.png")#save as png
#plt.show()#display

ax = plt.gca() # to get the current axis
ax.collections[0].set_edgecolor("Y")


#Ci-dessous des algorithmes de tests que nous avons utilisé pour comprendre 
#la librairie networkx et pour effectuer des tests
#Nous les mettons simplement en commentaire en les séparant pour éviter les surcharges visuelles

"""
node_number = 10 
initial_nodes = 9 
G = nx.barabasi_albert_graph(node_number, initial_nodes)
G.add_node(node_for_adding = 1, node_color = 'R')


nx.draw_spring(G, width = 3, node_size = 500, node_color = 'R')

ax = plt.gca() # to get the current axis


#ax.collections[0].set_edgecolor("Y")

#plt.savefig("simple_path.png")#save as png
#plt.show()#display

"""



"""
node_number = 15
initial_nodes = 2

G = nx.barabasi_albert_graph(node_number, initial_nodes)

nx.draw_spring(G, width = 3, node_size = 500, node_color = 'R')

G = nx.barabasi_albert_graph(node_number, initial_nodes)

color_map = []
for node in G:
    if node < 10:
        color_map.append('red')            
    else: 
        color_map.append('green')      
nx.draw(G, node_color=color_map, with_labels=True)
plt.show()

pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos)

coloring = {1, 5, 7, 8, 9}
some_colors = ['r','b','g','y','p']


nx.draw_networkx_nodes(G,pos,[x for x in G.nodes() if coloring[x]==1] ,width=8,  node_color=some_colors[0])
nx.draw_networkx_nodes
"""




"""
G = nx.Graph([(1, 2, {"color": "yellow"})])


col_list = nx.get_node_attributes(G, "node_size")
colle = [col_list.get(node) for node in G.nodes()]



#print(G.nodes('node_color'))

#FG.add_weighted_edges_from([(1, 2, 0.125), (1, 3, 0.75), (2, 4, 1.2), (3, 4, 0.375)])
for n, nbrs in G.adj.items():
   for nbr, eattr in nbrs.items():
       c = eattr
       if c == 'R' : print('R')
      
        
col = nx.get_node_attributes(G, 'node_color')
print(col)


for color in col:
    print(color)


for i in range (len(col)):
    print(col[i])
"""



"""
G=nx.Graph()

G.add_nodes_from([("a",{"col": "blue"}),
                  ("b",{"col": "red"}),
                  ("c",{"col": "blue"}),
                  ("d",{"col": "red"}),
                  ("e",{"col": "blue"}),
                  ("f",{"col": "red"}),
                  ("g",{"col": "blue"}),
                  ("h",{"col": "green"}),
                  ])

                 # "b","c","d","e","f","g","h"])

col_list = nx.get_node_attributes(G, "col")
colle = [col_list.get(node) for node in G.nodes()]

G.add_edges_from([("a","b"),
                  ("a","c"),
                  ("b","d"),
                  ("d","e"),
                  ("e","f"),
                  ("e","g"),
                  ("h","d"),
                  ("h","b"),
                  ("c","g"),
                 #("a","h")
                  ])

#nx.draw(G,with_labels=True)

my_pos = nx.spring_layout(G, seed = 100)
nx.draw(G, pos = my_pos, with_labels=True, node_color= colle, node_size=1000, edge_color='black', linewidths=10, font_size=30)
#plt.show()

#("a","b")

"""




"""

def random_coloring(graph,n_colors):
    coloring = {}
    for node in graph.nodes():
        coloring[node] = np.random.randint(0,n_colors)
    return coloring



def draw_coloring(G,coloring,colors):
    fig = plt.figure()
    n_colors = len(colors)

    pos = nx.spring_layout(G)
    for i in range(n_colors):
        nx.draw_networkx_nodes(G,pos,[x for x in G.nodes() if coloring[x]==i],width=8,node_color=colors[i])
    nx.draw_networkx_edges(G,pos,width=1.0,alpha=0.5)
        
    plt.axis('off')
    plt.show()
    return fig


G = nx.Graph()
some_coloring = random_coloring(G,5)



some_colors = ['r','b','g','y','p']

fig2 = draw_coloring(G,some_coloring,some_colors)
"""