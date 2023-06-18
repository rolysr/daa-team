from Soluciones.brute_force import is_valid_graph


def metaheuristic_solution(n, m, edges):
    bitmask = [True for i in range(m)]
    if m == 0 or is_valid_graph(n, m, edges, bitmask):
        return n
    else:
        maximum = [0]
        metaheuristic_solve(n, m, edges, bitmask, maximum)
        return maximum[0]

def metaheuristic_solve(n, m, edges, bitmask, maximum):
    if bitmask == [False for i in range(m)]:
        return
    
    if is_valid_graph(n, m, edges, bitmask):
        maximum = [n]
        return
    
    valid_edge_indexes = get_valid_indexes(bitmask)
    sorted_indexes_by_quality = get_sorted_indexes_by_quality(valid_edge_indexes, n, m, edges, bitmask)
    _, index = sorted_indexes_by_quality[0]
    bitmask[index] = False
    maximum[0] = max(maximum[0], get_state_quality(n, m, edges, bitmask))
    return metaheuristic_solve(n, m, edges, bitmask, maximum)

def get_valid_indexes(bitmask):
    indexes = []
    for i in range(len(bitmask)):
        if bitmask[i]:
            indexes.append(i)
    return indexes

def get_sorted_indexes_by_quality(valid_edge_indexes, n, m, edges, bitmask):
    answer = []
    for index in valid_edge_indexes:
        bitmask[index] = False
        quality = get_state_quality(n, m, edges, bitmask)
        answer.append((quality, index))
        bitmask[index] = True
    answer.sort()
    return answer

def get_state_quality(n, m, edges, bitmask):
    number_valid_nodes = 0
    degree_vertex = [0 for i in range(n)]

    for i in range(m):
        if bitmask[i]:
            a, b = edges[i]
            degree_vertex[a] += 1
            degree_vertex[b] += 1
    for d in degree_vertex:
        if d == 3 or d == 0:
            number_valid_nodes += 1
    return number_valid_nodes
