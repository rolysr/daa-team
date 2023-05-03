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
    visited = {}
    for edge in edges:
        visited[edge] = False
        u, v, weight = edge
        visited[(v, u, weight)] = False
    get_paths(u, v, l, g, visited, 0, [], paths)
    
    for path in paths:
        for edge in path:
            useful_edges.add(edge)

    return useful_edges

def get_paths(u, v, l, g, visited, current_cost, current_path, total_paths):
    if current_cost > l:
        return

    if u == v and current_cost <= l:
        current_path_cpy = copy.deepcopy(current_path)
        total_paths.append(current_path_cpy)
        return
    
    for ady in g.adyacents[u]:
        node, weight = ady
        if not visited[(u, node, weight)] and not visited[(node, u, weight)] and current_cost + weight <= l:
            visited[(u, node, weight)] = True
            visited[(node, u, weight)] = True
            current_cost += weight
            current_path.append((u, node))
            get_paths(node, v, l, g, visited, current_cost, current_path, total_paths)
            visited[(u, node, weight)] = False
            visited[(node, u, weight)] = False
            current_cost -= weight
            current_path.pop()