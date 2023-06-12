import copy
from Soluciones.graph import Graph

def brute_force(n, m, edges):
    bitmask = [True for i in range(m)]

    if m == 0 or is_valid_graph(n, m, edges, bitmask):
        return True

    for i in range(1, 2**m):
        for j in range(m-1):
            print(len(bitmask), j)
            bitmask[j] = i & j
        if is_valid_graph(n, m, edges, bitmask):
            return True

    return False

def is_valid_graph(n, m, edges, bitmask):
    degree_vertex = [0 for i in range(n)]

    for i in range(m):
        if bitmask[i]:
            a, b = edges[i]
            degree_vertex[a] += 1
            degree_vertex[b] += 1
            if degree_vertex[a] > 3 or degree_vertex[b] > 3:
                return False
        
    for degree in degree_vertex:
        if degree != 3 and degree != 0:
            return False
    return True
