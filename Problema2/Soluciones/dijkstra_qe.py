import math
from queue import PriorityQueue
from Soluciones.dijsktra_foreach_qe import dijkstra
from Soluciones.graph import Graph


def dijkstra_qe(n, m, edges, useful_paths_tuples):
    g = Graph(n, m, edges)
    useful_edge = {i:False for i in m}
    node_dist = [None for i in range(n)]
    total_useful_edges = 0
    
    for useful_path_tuple in useful_paths_tuples:
        u, v, l = useful_path_tuple
        if node_dist[u] is None:
           node_dist[u] = dijkstra(u, g)
        if node_dist[v] is None:
            node_dist[v] = dijkstra(v, g)
    
    for useful_path_tuple in useful_paths_tuples:
        u, v, l = useful_path_tuple
        for i in range(m):
            edge = edges[i]
            if useful_edge[i]:
                continue
            x, y, weight = edge
            if node_dist[u][x] + weight + node_dist[v][y] <= l or node_dist[u][y] + weight + node_dist[v][x] <= l:
                useful_edge[i] = True
                total_useful_edges += 1

    return total_useful_edges