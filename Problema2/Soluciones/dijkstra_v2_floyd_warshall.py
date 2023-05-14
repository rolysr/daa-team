import math
from Soluciones.graph import Graph
from Soluciones.dijkstra_floyd_warshall import floyd_warshall
from Soluciones.dijkstra_qe import dijkstra_qe


def dijkstra_v2_floyd_warshall(n, m, edges, useful_paths_tuples):
    if len(useful_paths_tuples) <= n and m <= n:
        return dijkstra_qe(n, m, edges, useful_paths_tuples)
    
    g = Graph(n, m, edges)
    useful_edge = [False for i in range(m)]
    node_dist = [None for i in range(n)]
    total_useful_edges = 0
    
    node_dist = floyd_warshall(n, edges)

    useful_paths_tuples_endpoint_nodes = get_useful_paths_tuples_endpoint_nodes(n, useful_paths_tuples)

    for i in range(n):
        endpoint_node = i
        if useful_paths_tuples_endpoint_nodes[endpoint_node] is None:
            continue
        # compute Dijkstra in O(v^2)
        ui_li_endpoint_node_list = useful_paths_tuples_endpoint_nodes[endpoint_node]
        new_g = create_multisource_graph_ui_li(ui_li_endpoint_node_list, g)
        source_node = new_g.n - 1
        min_dist = dijkstra_v2(source_node, new_g)
        
        # check useful edges
        for i in range(m):
            x, y, weight = edges[i]
            if min_dist[y] <= - node_dist[endpoint_node][x] - weight or  min_dist[x] <= - node_dist[endpoint_node][y] - weight:
                useful_edge[i] = True
                total_useful_edges += 1

    return total_useful_edges

def get_useful_paths_tuples_endpoint_nodes(n, useful_paths_tuples):
    useful_paths_tuples_endpoint_nodes = [[] for i in range(n)]
    for q in useful_paths_tuples:
        u, v, l = q
        if not v in useful_paths_tuples_endpoint_nodes[u]:
            if useful_paths_tuples_endpoint_nodes[u] is None:
                useful_paths_tuples_endpoint_nodes[u] = []
            useful_paths_tuples_endpoint_nodes[u].append((v, l))
        if not u in useful_paths_tuples_endpoint_nodes[v]:
            if useful_paths_tuples_endpoint_nodes[v] is None:
                useful_paths_tuples_endpoint_nodes[v] = []
            useful_paths_tuples_endpoint_nodes[v].append((u, l))
    return useful_paths_tuples_endpoint_nodes

def dijkstra_v2(node, g):
    dist = [math.inf for i in range(g.n)]
    dist[g.n - 1] = 0
    for ady in g.adyacents[g.n-1]:
        ui, weight = ady
        dist[ui] = weight
    
    visited = [False for i in range(g.n)]
    q = [(0, g.n-1)]

    while len(q) > 0:
        node_distance, node = extract_min(q)  # get node with minimum distance

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
                q.append((dist[adjacent_node], adjacent_node))
                
    return dist

def extract_min(q):
    min_value = None
    for tuple in q:
        if min_value is None:
            min_value = tuple
        elif min_value[0] > tuple[0]:
            min_value[0] = tuple[0]
            min_value[1] = tuple[1]
    q.remove(min_value)
    return min_value

def create_multisource_graph_ui_li(ui_li_endpoint_node_list, g):
    artificial_node = g.n
    new_edges = []
    for edge in g.edges:
        new_edges.append(edge)
    for ui_li in ui_li_endpoint_node_list:
        ui, li = ui_li
        new_edges.append((artificial_node, ui, -li))
    new_g = Graph(g.n + 1, g.m + len(ui_li_endpoint_node_list), new_edges)
    return new_g