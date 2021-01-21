import networkx as nx 
import matplotlib.pyplot as plt
G=nx.Graph()


node_number = 10 
initial_nodes = 3 
G = nx.barabasi_albert_graph(node_number, initial_nodes)

nx.draw_spring(G, width = 3, node_size = 500, node_color = 'R')












