from copy import deepcopy
import math


def brute_force(n: int, hi: list[int], c: int, e, m) -> int:
    """Brute force solution by using Backtracking"""
    
    if n < 0 or n != len(hi) or c < 0 or e < 0 or m < 0:
        raise("Invalid problem instance")

    min_h = min(hi)
    max_h = max(hi)
    answer1 = math.inf
    answer2 = math.inf
    hi.sort() # sort the heights

    for height in range(min_h, max_h + 1):
        cpy = [x for x in hi]
        result1 = solve1(n, cpy, c, e, m, height)
        result2 = solve2(n, hi, c, e, m, height)

        if result1 < answer1:
            answer1 = result1
        
        if result2 < answer2:
            answer2 = result2

    return answer1, answer2


def solve1(n, hi, c, e, m, height):
    """Solve method"""
    result = 0

    for i in range(n):
        current_height = hi[i]

        if current_height == height:
            continue

        elif current_height < height:
            c1 = c*(height - current_height)
            c2 = 0
            new_hi = deepcopy(hi)
            if m < c + e:
                for j in range(i + 1, n):
                    next_height = new_hi[j]
                    if next_height > height:
                        if next_height - height >= height - new_hi[i]:
                            c2 += m*(height - new_hi[i])
                            new_hi[j] = new_hi[j] - (height - new_hi[i])
                            new_hi[i] = height
                            break
                        else:
                            c2 += m*(next_height - height)
                            new_hi[i] = new_hi[i] + next_height - height
                            new_hi[j] = height
                            if new_hi[i] == height:
                                break

            if new_hi[i] == height:
                result += c2
                hi = new_hi
            else:
                if c2 + c*(height - new_hi[i]) <= c1:
                    result += c2 + c*(height - new_hi[i])
                    hi = new_hi
                else:
                    result += c1
                    hi[i] = height

        else:
            result += (hi[i] - height)*e
            hi[i] = height
    
    return result

def solve2(n, hi, c, e, m, height):
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