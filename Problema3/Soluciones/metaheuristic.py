from Soluciones.brute_force import is_valid_graph


def metaheuristic_solution(n, m, edges):
    bitmask = [True for i in range(m)]
    if m == 0 or is_valid_graph(n, m, edges, bitmask):
        return True
    else:
        return metaheuristic_solve(n, m, edges, bitmask)

def metaheuristic_solve(n, m, edges, bitmask):
    if bitmask == [False for i in range(m)]:
        return False
    
    if is_valid_graph(n, m, edges, bitmask):
        return True
    
    valid_edge_indexes = get_valid_indexes(bitmask)
    sorted_indexes_by_quality = get_sorted_indexes_by_quality(valid_edge_indexes, n, m, edges, bitmask)
    for value in sorted_indexes_by_quality:
        _, index = value
        bitmask[index] = False
        if metaheuristic_solve(n, m, edges, bitmask):
            return True
        bitmask[index] = True
    return False

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
