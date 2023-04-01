from Pruebas.test_cases_generator import generate_test_cases
from Soluciones.greedy2 import greedy2


def test_solution(solution_function, test_function=greedy2):
    """
        Tester function to determine how good is a given
        solution function
    """
    if solution_function is None:
        raise ValueError("Invalid solution function type!")
    accepted_solution = True
    test_cases = generate_test_cases(number_test_cases=1000)

    for test_case in test_cases:
        if solution_function(*test_case) != test_function(*test_case):
            accepted_solution = False
            break

    return "Accepted!!" if accepted_solution else "Wrong Answer!!"