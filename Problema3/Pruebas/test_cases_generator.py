from random import randrange

def generate_test_cases(number_test_cases):
    test_cases = []

    for i in range(number_test_cases):
        n = randrange(5,6) 
        m = 0
        edges = []
        for j in range(n-1):
            for k in range(1, n):
                if j != k and randrange(0, 2):
                    edge = (j, k)
                    edges.append(edge)
                    m += 1
        test_cases.append((n, m, edges))

    return test_cases

def generate_test_cases1(number_test_cases):
    test_cases = []
    n = 7
    m = 6
    edges = []
    edges.append((0,1))
    edges.append((0,2))
    edges.append((0,3))
    edges.append((4,5))
    edges.append((0,6))
    edges.append((6,1))
    test_cases.append((n, m, edges))

    return test_cases
        
def generate_test_cases2(number_test_cases):
    test_cases = []
    n = 7
    m = 8
    edges = []
    edges.append((0,1))
    edges.append((0,2))
    edges.append((0,3))
    edges.append((4,5))
    edges.append((0,6))
    edges.append((6,1))
    edges.append((2,1))
    edges.append((6,2))
    
    test_cases.append((n, m, edges))

    return test_cases