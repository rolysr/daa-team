class Graph:
    def __init__(self, n, m, edges) -> None:
        self.n = n
        self.m = m
        self.nodes = [i for i in range(n)]
        self.edges = edges
        self.adyacents = {}
        for i in range(n):
            self.adyacents[i] = []
        for edge in edges:
            node_x, node_y = edge
            if not self.adyacents[node_x].__contains__(node_y):
                self.adyacents[node_x].append(node_y)
                self.adyacents[node_y].append(node_x)
    