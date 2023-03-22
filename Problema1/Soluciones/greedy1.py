from copy import deepcopy
import math


def greedy1(n: int, hi: list[int], c: int, e, m) -> int:
    """Greedy solution 1"""
    
    if n < 0 or n != len(hi) or c < 0 or e < 0 or m < 0:
        raise("Invalid problem instance")

    min_h = min(hi)
    max_h = max(hi)
    answer = math.inf
    hi.sort() # sort the heights

    for height in range(min_h, max_h + 1):
        cpy = [x for x in hi]
        result = solve(n, cpy, c, e, m, height)
        answer = min(result, answer)

    return answer


def solve(n, hi, c, e, m, height):
    result = 0

    for i in range(n):
        current_height = hi[i]

        if current_height == height:
            continue

        elif current_height < height:
            c1 = c*(height - current_height)
            c2 = 0
            new_hi = [x for x in hi]
            if m <= c + e:
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
                            new_hi[i] = new_hi[i] + new_hi[j] - height
                            new_hi[j] = height

            if new_hi[i] == height:
                result += c2
                hi = new_hi
            else:
                if new_hi[i] > current_height and new_hi[i] < height and c2 + c*(height - new_hi[i]) <= c1:
                    result += c2 + c*(height - new_hi[i])
                    hi = new_hi
                    hi[i] = height
                else:
                    result += c1
                    hi[i] = height

        else:
            result += (current_height - height)*e
            hi[i] = height
    
    return result