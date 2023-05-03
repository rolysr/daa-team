from Soluciones.brute_force import brute_force


if __name__ == "__main__":
    n, m = input().split()
    n, m = int(n), int(m)
    
    edges = []
    for i in range(m):
        node_x, node_y, edge_weight = input().split()
        node_x, node_y, edge_weight = int(node_x), int(node_y), int(edge_weight)
        edges.append((node_x, node_y, edge_weight))

    q = int(input())

    useful_paths_tuples = []
    for i in range(q):
        u, v, l = input().split()
        u, v, l = int(u), int(v), int(l)
        useful_paths_tuples.append((u, v, l))

    print(brute_force(n, m, q, edges, useful_paths_tuples))