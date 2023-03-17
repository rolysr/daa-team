from random import randrange
from brute_force import brute_force

def check_results():
    best_height = 0
    for i in range(100):
        n = randrange(5, 20)
        c = randrange(0,20)
        e = randrange(0,20)
        m = randrange(0,20)
        hi = [randrange(0, 20) for i in range(n)]

        result = brute_force(n, hi, c, e, m)
        print(result)