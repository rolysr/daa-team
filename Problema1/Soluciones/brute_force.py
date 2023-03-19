from copy import deepcopy
import math


def brute_force(n: int, hi: list[int], c: int, e, m) -> int:
    """Brute force solution by using Backtracking"""
    
    if n < 0 or n != len(hi) or c < 0 or e < 0 or m < 0:
        raise("Invalid problem instance")

    min_h = min(hi)
    max_h = max(hi)
    answer = [math.inf]
    hi.sort() # sort the heights

    for height in range(min_h, max_h + 1):
        solve(0, n, hi, c, e, m, height, 0, answer)

    answer = int(answer[0])
    return answer


def solve(s, n, hi, c, e, m, height, current_cost, best):
    """Solve method"""

    if s == n:
        best[0] = min(best[0], current_cost)
        return

    current_height = hi[s]

    if current_height == height:
        solve(s+1, n, hi, c, e, m, height, current_cost, best)
        return

    elif hi[s] < height:
        c1 = c*(height - current_height)
        c2 = math
        new_hi = deepcopy(hi)
        if m < c + e:
            c2 = 0
            for i in range(s + 1, n):
                next_height = new_hi[i]
                if next_height > height:
                    if next_height - height >= new_hi[s]:
                        c2 += m*(height - new_hi[s])
                        new_hi[i] = new_hi[i] - (height - new_hi[s])
                        new_hi[s] = height
                        break
                    else:
                        c2 += m*(next_height - height)
                        new_hi[s] = new_hi[s] + next_height - height
                        new_hi[i] = height
                        if new_hi[s] == height:
                            break
                        else:
                            continue

        if new_hi[s] == height:
            current_cost += c2
            hi = new_hi
        else:
            current_cost += c1
            hi[s] = height
        solve(s+1, n, hi, c, e, m, height, current_cost, best)
        return

    else:
        current_cost += (hi[s] - height)*e
        hi[s] = height
        solve(s+1, n, hi, c, e, m, height, current_cost, best)