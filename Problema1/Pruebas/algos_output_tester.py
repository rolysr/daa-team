from copy import deepcopy
from random import randrange
from Soluciones.gbt_or_g2t import gbt_or_g2t
from Soluciones.greedy2_ts import greedy2_ts
from Soluciones.greedy_bs_ts import greedy_bs_ts
from Soluciones.greedy1 import greedy1
from Soluciones.greedy2 import greedy2
from Soluciones.greedy_bs import greedy_bs
from time import time


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
        result5 = greedy2_ts(n, deepcopy(hi), c, e, m)
        result6 = gbt_or_g2t(n, deepcopy(hi), c, e, m)

        print(result1, result2, result3, result4, result5, result6)