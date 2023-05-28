class Graph:
    def __init__(self, n, m, edges) -> None:
        self.n = n
        self.m = m
        self.edges = edges
        self.adyacents = {}
        for i in range(n):
            self.adyacents[i] = []
        for edge in edges:
            node_x, node_y = edge
            self.adyacents[node_x].append(node_y)
            self.adyacents[node_y].append(node_x)
    
    def delete_node(self , node):
        adyacent = self.adyacents[node]
        for i in self.edges:
            if i[0] == node or i[1] == node:
                self.edges.delete(i)
        self.adyacents.__delitem__(node)
        for i in adyacent:
            self.adyacents.__delattr__(node,i)