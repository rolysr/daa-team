import copy
from Soluciones.graph import Graph

def brute_force(n, m, edges):
    g = Graph(n, m, edges)
    degrees = [0 for i in range(n)]
    for edge in edges:
        degrees[edge[0]]+=1
    get_reduction(g,degrees)
 #   for i in g.nodes:
#        k
    return g
        
def get_reduction(g,degrees):
    cicle=True
    temp=degrees
    while cicle:
        cicle=False
        for i in range(len(temp)):
            if temp[i] < 3 and temp[i] != 0:
                g.delete_node(i)
                cicle=True
        if cicle:
          temp=[0 for i in range(len(degrees))]  
          for edge in g.edges:
              temp[edge[0]]+=1          
  