from Pruebas.test_cases_generator import generate_test_cases
from Soluciones.brute_force import brute_force_bitmask, brute_force_recursive
from Soluciones.metaheuristic import metaheuristic_solution


def check_results():
    test_cases = generate_test_cases(10)
    for test_case in test_cases:
        result1 = brute_force_bitmask(*test_case)
        result2 = brute_force_recursive(*test_case)
        result3 = metaheuristic_solution(*test_case)
        print(result1, result2, result3)