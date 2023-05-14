class Graph:
    def __init__(self, n, m, edges) -> None:
        self.n = n
        self.m = m
        self.edges = edges
        self.adyacents = {}
        for i in range(n):
            self.adyacents[i] = []
        for edge in edges:
            node_x, node_y, edge_weight = edge
            self.adyacents[node_x].append((node_y, edge_weight))
            self.adyacents[node_y].append((node_x, edge_weight))