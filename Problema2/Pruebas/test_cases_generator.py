from random import randrange


def generate_test_cases(number_test_cases):
    test_cases = []

    for i in range(number_test_cases):
        n = randrange(10, 100)
        m = 0
        edges = []
        q = randrange(1, 2)
        useful_paths_tuples = []
        for j in range(n):
            for k in range(n):
                if j != k:
                    edge = (j, k, randrange(0, 100))
                    edges.append(edge)
                    m += 1

        for j in range(q):
            u = randrange(0, n)
            v = randrange(0, n)
            l = randrange(0, m*100)
            useful_paths_tuples.append((u, v, l))

        test_cases.append((n, m, edges, useful_paths_tuples))

    return test_cases
        