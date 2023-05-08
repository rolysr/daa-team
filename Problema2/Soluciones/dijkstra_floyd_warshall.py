from math import inf
from Soluciones.dijkstra_qe import dijkstra_qe


def dijsktra_floyd_warshall(n, m, edges, useful_paths_tuples):
    number_dist_nodes = get_number_dist_nodes(n, useful_paths_tuples)

    if number_dist_nodes < n or m < (n*(n-1))/2:
        return dijkstra_qe(n, m, edges, useful_paths_tuples)

    useful_edge = [False for i in range(m)]
    node_dist = [None for i in range(n)]
    total_useful_edges = 0
    
    node_dist = floyd_warshall(n, edges)
    
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

def get_number_dist_nodes(n, useful_paths_tuples):
    node_calculated = [False for i in range(n)]
    answer = 0
    for tuple in useful_paths_tuples:
        u, v, l = tuple
        if not node_calculated[u]:
            node_calculated[u] = True
            answer += 1
        if not node_calculated[v]:
            node_calculated[v] = True
            answer += 1
        if answer == n:
            break
    return answer

def floyd_warshall(n, edges):
    dist = [[inf for i in range(n)] for i in range(n)]
    for i in range(n):
        dist[i][i] = 0

    for edge in edges:
        u, v, weight = edge
        dist[u][v] = weight
        dist[v][u] = weight

    for i in range(n):
        for j in range(n):
            for k in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist