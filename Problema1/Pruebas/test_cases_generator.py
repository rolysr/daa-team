from random import randrange


def generate_test_cases(number_test_cases=1, max_n=20, max_height=20, max_cost_ops=20):
    """
        Method that generates random problem instance tuples
        with the format (n, hi, c, e, m, result)
    """
    test_cases = []
    for i in range(number_test_cases):
        n = randrange(5, max_n)
        c = randrange(0, max_cost_ops)
        e = randrange(0, max_cost_ops)
        m = randrange(0, max_cost_ops)
        hi = [randrange(0, max_height) for i in range(n)]
        test_cases.append((n,hi,c,e,m))
    return test_cases