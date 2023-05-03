from Pruebas.test_cases_generator import generate_test_cases
from Soluciones.brute_force import brute_force


def test_solution(solution_function, test_function=brute_force):
    """
        Tester function to determine how good is a given
        solution function
    """
    if solution_function is None:
        raise ValueError("Invalid solution function type!")
    accepted_solution = True
    test_cases = generate_test_cases(number_test_cases=100)

    for test_case in test_cases:
        if solution_function(*test_case) != test_function(*test_case):
            accepted_solution = False
            break

    return "Accepted!!" if accepted_solution else "Wrong Answer!!"