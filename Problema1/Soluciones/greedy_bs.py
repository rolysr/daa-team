from copy import deepcopy
import math


def greedy_bs(n: int, hi: list[int], c: int, e, m) -> int:
    """Greedy + Binary Search Solution"""
    
    if n < 0 or n != len(hi) or c < 0 or e < 0 or m < 0:
        raise("Invalid problem instance")

    min_h = min(hi)
    max_h = max(hi)
    answer = math.inf
    hi.sort() # sort the heights

    for height in range(min_h, max_h + 1):
        cpy = [x for x in hi]
        cpy_sum = get_sum_array(cpy)
        result = solve(0, n-1, n, cpy_sum, c, e, m, height)
        answer = min(result, answer)

    return answer

def get_sum_array(array):
    """Compute the accumulative sum of a given array"""
    answer = [0 for x in array]
    answer[0] = array[0]
    for i in range(1, len(array)):
        answer[i] = answer[i-1] + array[i]

    return answer

def solve(a, b, n, hi_sum, c, e, m, height):
    """Binary Search Solve"""
    if a==b:
        count_ups = (a)*height - (hi_sum[a-1]) if a > 0 else 0
        count_downs = (hi_sum[n-1] - hi_sum[a-1]) - (n-a)*height if a > 0 else  hi_sum[n-1] - (n-a)*height
        result = 0

        if count_ups == count_downs and m <= c + e:
            result = count_ups*m

        elif count_ups < count_downs and m <= c + e:
            result = count_ups*m + (count_downs - count_ups)*e

        elif count_ups > count_downs and m <= c + e:
            result = count_downs*m + (count_ups - count_downs)*c

        else:
            result = count_ups*c + count_downs*e

        return result


    mid = int((a+b)/2)
    current_height = hi_sum[mid] - hi_sum[mid-1] if mid > 0 else hi_sum[mid]

    if current_height < height:
        return solve(mid + 1, b, n, hi_sum, c, e, m, height)
    
    else:
        return solve(a, mid, n, hi_sum, c, e, m, height)
    