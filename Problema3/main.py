from Soluciones.brute_force import brute_force_recursive
from Pruebas.tester import test_solution
from Pruebas.algos_output_tester import check_results
from Soluciones.brute_force import brute_force_bitmask


if __name__ == "__main__":
    n, m = input().split()
    n, m = int(n), int(m)
    
    edges = []
    for i in range(m):
        node_x, node_y = input().split()
        node_x, node_y = int(node_x), int(node_y)
        edges.append((node_x, node_y))

    print(brute_force_recursive(n, m, edges))

    # check_results()
    # print(test_solution(brute_force_bitmask))