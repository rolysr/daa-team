from Soluciones.brute_force import brute_force


if __name__ == "__main__":
    n, m = input().split()
    n, m = int(n), int(m)
    
    edges = []
    for i in range(m):
        node_x, node_y = input().split()
        node_x, node_y = int(node_x), int(node_y)
        edges.append((node_x, node_y))

    print(brute_force(n, m, edges))