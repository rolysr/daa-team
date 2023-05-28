import copy
from Soluciones.graph import Graph

def brute_force(n, m, edges):
    g = Graph(n, m, edges)
    degrees = [0 for i in n]
    for edge in edges:
        degrees[edge[0]]+=1
    get_reduction(g,degrees)
        

def get_reduction(g,degrees):
    for i in range(degrees):
        if degrees[i] < 3 and degrees[i] != 0:
            delete_edges(g,i)
            