from copy import deepcopy
import math
from Soluciones.greedy_bs import solve
from Soluciones.greedy_bs import get_sum_array


def greedy_bs_ts(n: int, hi: list[int], c: int, e, m) -> int:
    """Greedy + Binary Search + Ternary Search Solution"""
    
    if n < 0 or n != len(hi) or c < 0 or e < 0 or m < 0:
        raise("Invalid problem instance")

    min_h = min(hi)
    max_h = max(hi)
    answer = math.inf
    hi.sort() # sort the heights
    hi_sum = get_sum_array(hi)

    for height in range(min_h, max_h + 1):
        result = solve(0, n-1, n, hi_sum, c, e, m, height)
        answer = min(result, answer)

    return answer

def ts_solve(h1, h2, n, hi_sum, c, e, m):
    if h1 == h2:
        return solve(0, n-1, n, hi_sum, c, e, m, h1)
    
    mid1 = h1 + (h2 - h1) // 3
    mid2 = h2 - (h2 - h1) // 3

    result_mid1 = solve(0, n-1, n, hi_sum, c, e, m, mid1)
    result_mid2 = solve(0, n-1, n, hi_sum, c, e, m, mid2)

    if result_mid1 == result_mid2:
        return ts_solve(mid1, mid2, n, hi_sum, c, e, m)

    elif result_mid1 < result_mid2:
        return ts_solve(h1, mid2, n, hi_sum, c, e, m)
    
    else:
        return ts_solve(mid1, h2, n, hi_sum, c, e, m)