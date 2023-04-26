import copy


class Graph:
    def __init__(self, n, m, edges) -> None:
        self.n = n
        self.m = m
        self.adyacents = {}
        for i in range(n):
            self.adyacents[i] = []
        for edge in edges:
            node_x, node_y, edge_weight = edge
            self.adyacents[node_x].append((node_y, edge_weight))
            self.adyacents[node_y].append((node_x, edge_weight))

def brute_force(n, m, q, edges, useful_paths_tuples):
    g = Graph(n, m, edges)
    total_useful_edges = set()

    for useful_path_tuple in useful_paths_tuples:
        u, v, l = useful_path_tuple
        useful_edges = get_useful_edges(u, v, l, g)
        total_useful_edges = total_useful_edges.union(useful_edges)

    answer = len(total_useful_edges)
    return answer

def get_useful_edges(u, v, l, g):
    useful_edges = set()
    paths = []
    get_paths(u, v, l, g, [False for i in range(g.n)], 0, [], paths)
    
    for path in paths:
        for edge in path:
            useful_edges.add(edge)

    return useful_edges

def get_paths(u, v, l, g, visited, current_cost, current_path, total_paths):
    if u == v:
        if current_cost <= l:
            current_path_cpy = copy.deepcopy(current_path)
            total_paths.append(current_path_cpy)
        return
    
    for ady in g.adyacents[u]:
        node, weight = ady
        if not visited[node] and current_cost + weight <= l:
            visited[u] = True
            current_cost += weight
            current_path.append((u, node))
            get_paths(node, v, l, g, visited, current_cost, current_path, total_paths)
            visited[u] = False
            current_cost -= weight
            current_path.pop()