import math
import matplotlib.pyplot as plt
from Soluciones.greedy_bs import get_sum_array, solve


def plot_problem(n, hi, c, e, m):
    """
        Plotter for the problem for discovering new properties
    """
    min_h = min(hi)
    max_h = max(hi)
    hi.sort() # sort the heights
    X, Y = [], []

    for height in range(min_h, max_h + 1):
        cpy = [x for x in hi]
        cpy_sum = get_sum_array(cpy)
        result = solve(0, n-1, n, cpy_sum, c, e, m, height)
        X.append(height)
        Y.append(result)

    plt.plot(X, Y)
    plt.scatter(X, Y)
    # naming the x axis
    plt.xlabel('Heights - axis')
    # naming the y axis
    plt.ylabel('Result - axis')

    plt.title('Problem graph. c:{}, e:{}, m:{}'.format(c, e, m))

    # function to show the plot
    plt.show()