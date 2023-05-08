from Soluciones.dijkstra_floyd_warshall import dijsktra_floyd_warshall
from Pruebas.algos_output_tester import check_results
from Soluciones.brute_force import brute_force
from Soluciones.dijkstra_qe import dijkstra_qe
from Soluciones.dijsktra_foreach_qe import dijkstra_foreach_qe
from Pruebas.tester import test_solution


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

    print(dijkstra_qe(n, m, edges, useful_paths_tuples))

    # print(test_solution(solution_function=dijsktra_floyd_warshall, test_function=dijkstra_qe))