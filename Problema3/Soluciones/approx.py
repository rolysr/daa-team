def approx_solution(n, m, edges):
    return n-3 if is_node_degree_3(n, m, edges) else 0

def is_node_degree_3(n, m, edges):
    degrees = [0 for i in range(n)]
    for i in range(m):
        node1, node2 = edges[i]
        degrees[node1] += 1
        degrees[node2] += 1
        if degrees[node1] >= 3 or degrees[node2] >= 3:
            return True
    return False