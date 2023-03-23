from random import randrange
from Soluciones.greedy_bs_ts import greedy_bs_ts
from Pruebas.plotter import plot_problem
from Pruebas.tests import check_results
from Soluciones.greedy2 import *


if __name__ == "__main__":
    n = input()
    n = int(n)

    if n <= 0:
        raise Exception("Invalid number of columns")

    hi = input().split()
    if len(hi) != n:
        raise Exception("Invalid number of heights")
    
    hi = [int(h) for h in hi]

    for h in hi:
        if h < 0:
            raise Exception("Invalid height values")
        
    c = int(input())
    e = int(input())
    m = int(input())

    print(greedy_bs_ts(n, hi, c, e, m))
    
    # print(greedy2(n, hi, c, e, m))

    # check_results()

    # plot_problem(20, [randrange(0, 20) for i in range(20)], randrange(0, 20),  randrange(0, 20),  randrange(0, 20))