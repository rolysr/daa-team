import math
from queue import PriorityQueue
from Soluciones.graph import Graph


def dijkstra_foreach_qe(n, m, edges, useful_paths_tuples):
    g = Graph(n, m, edges)
    useful_edge = [False for i in range(m)]
    total_useful_edges = 0
    
    for useful_path_tuple in useful_paths_tuples:
        u, v, l = useful_path_tuple
        dist_u = dijkstra(u, g)
        dist_v = dijkstra(v, g)
        for i in range(m):
            edge = edges[i]
            if useful_edge[i]:
                continue
            x, y, weight = edge
            if dist_u[x] + weight + dist_v[y] <= l or dist_u[y] + weight + dist_v[x] <= l:
                useful_edge[i] = True
                total_useful_edges += 1

    return total_useful_edges

def dijkstra(s, g):
    dist = [math.inf for i in range(g.n)]
    dist[s] = 0

    pq = PriorityQueue()
    visited = [False for i in range(g.n)]
    pq.put((0, s))

    size = 1
    while size > 0:
        node_distance, node = pq.get()  # get node with minimum distance
        size -= 1
        if visited[node]:
            continue
        visited[node] = True  # set visited node as true

        for adjacent in g.adyacents[node]:  # analize each adjacent node and try to update
            # get adjacent node and its distance from initial
            adjacent_node, distance = adjacent[0], adjacent[1]

            if visited[adjacent_node]:  # don't analize visited nodes
                continue

            # new distance for adjacent node
            new_distance = distance + node_distance
            # if distance is improved, then update it and also, update parent node
            if new_distance < dist[adjacent_node]:
                dist[adjacent_node] = new_distance
                pq.put((dist[adjacent_node], adjacent_node))
                size += 1
                
    return dist