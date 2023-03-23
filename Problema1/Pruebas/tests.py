from copy import deepcopy
from random import randrange
from Soluciones.greedy_bs_ts import greedy_bs_ts
from Soluciones.greedy1 import greedy1
from Soluciones.greedy2 import greedy2
from Soluciones.greedy_bs import greedy_bs

def check_results():
    for i in range(100):
        n = randrange(5, 20)
        c = randrange(0,20)
        e = randrange(0,20)
        m = randrange(0,20)
        hi = [randrange(0, 20) for i in range(n)]

        result1 = greedy_bs(n, deepcopy(hi), c, e, m)
        result2 = greedy1(n, deepcopy(hi), c, e, m)
        result3 = greedy2(n, deepcopy(hi), c, e, m)
        result4 = greedy_bs_ts(n, deepcopy(hi), c, e, m)

        print(result1, result2, result3, result4)