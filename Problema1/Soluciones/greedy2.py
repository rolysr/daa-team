from copy import deepcopy
import math


def greedy2(n: int, hi: list[int], c: int, e, m) -> int:
    """Greedy solution 2"""
    
    if n < 0 or n != len(hi) or c < 0 or e < 0 or m < 0:
        raise("Invalid problem instance")

    min_h = min(hi)
    max_h = max(hi)
    answer = math.inf

    for height in range(min_h, max_h + 1):
        cpy = [x for x in hi]
        result = solve(n, cpy, c, e, m, height)
        answer = min(result, answer)

    return answer

def solve(n, hi, c, e, m, height):
    count_ups, count_downs = 0, 0
    result = 0

    for i in range(n):
        if hi[i] == height:
            continue

        if hi[i] < height:
            count_ups += (height-hi[i])
        
        else:
            count_downs += (hi[i]-height)

    if count_ups == count_downs and m <= c + e:
        result = count_ups*m

    elif count_ups < count_downs and m <= c + e:
        result = count_ups*m + (count_downs - count_ups)*e

    elif count_ups > count_downs and m <= c + e:
        result = count_downs*m + (count_ups - count_downs)*c

    else:
        result = count_ups*c + count_downs*e

    return result