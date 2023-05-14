from Soluciones.dijkstra_v2_floyd_warshall import dijkstra_v2_floyd_warshall
from Pruebas.test_cases_generator import generate_test_cases
from Soluciones.brute_force import brute_force
from Soluciones.dijkstra_qe import dijkstra_qe
from Soluciones.dijkstra_floyd_warshall import dijsktra_floyd_warshall
from Soluciones.dijsktra_foreach_qe import dijkstra_foreach_qe


def check_results():
    test_cases = generate_test_cases(10)
    for test_case in test_cases:
        result1 = dijsktra_floyd_warshall(*test_case)
        result2 = dijkstra_foreach_qe(*test_case)
        result3 = dijkstra_qe(*test_case)
        result4 = dijkstra_v2_floyd_warshall(*test_case)
        print(result1, result2, result3, result4)