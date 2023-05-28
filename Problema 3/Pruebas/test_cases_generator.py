from random import randrange


def generate_test_cases1(number_test_cases):
    test_cases = []

    for i in range(number_test_cases):
        n = randrange(10, 100)
        m = 0
        edges = []
        for j in range(n):
            for k in range(n):
                if j != k:
                    edge = (j, k,)
                    edges.append(edge)
                    m += 1

        test_cases.append((n, m, edges))

    return test_cases

def generate_test_cases(number_test_cases):
    test_cases = []
    n = 5
    m = 20
    edges = []
    edges.append(0,1)
    edges.append(1,0)
    edges.append(0,2)
    edges.append(2,0)
    edges.append(0,3)
    edges.append(3,0)
    edges.append()
    
    test_cases.append((n, m, edges))

    return test_cases
        