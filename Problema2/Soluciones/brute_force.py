import copy
from Soluciones.graph import Graph

def brute_force(n, m, edges, useful_paths_tuples):
    g = Graph(n, m, edges)
    total_useful_edges = set()

    for useful_path_tuple in useful_paths_tuples:
        u, v, l = useful_path_tuple
        useful_edges = get_useful_edges(u, v, l, g, edges)
        total_useful_edges = total_useful_edges.union(useful_edges)

    answer = len(total_useful_edges)
    return answer

def get_useful_edges(u, v, l, g, edges):
    useful_edges = set()
    paths = []
    get_paths(u, v, l, g, 0, [], paths)
    
    for path in paths:
        for edge in path:
            useful_edges.add(edge)

    return useful_edges

def get_paths(u, v, l, g, current_cost, current_path, total_paths):
    if current_cost > l:
        return

    if u == v and current_cost <= l:
        current_path_cpy = copy.deepcopy(current_path)
        total_paths.append(current_path_cpy)
    
    for ady in g.adyacents[u]:
        node, weight = ady
        if current_cost + weight <= l:
            current_cost += weight
            current_path.append((u, node))
            get_paths(node, v, l, g, current_cost, current_path, total_paths)
            current_cost -= weight
            current_path.pop()
