from Soluciones.greedy2_ts import greedy2_ts
from Soluciones.greedy_bs_ts import greedy_bs_ts


def gbt_or_g2t(n, hi, c, e, m):
    """
        General case solution. If n <= k then apply
        greedy_bs_ts and apply greedy2_ts otherwise.
    """

    min_hi = min(hi)
    max_hi = max(hi)
    k = max_hi - min_hi

    if n <= k: # O(nlogn + logk*logn)
        return greedy_bs_ts(n, hi, c, e, m)
    
    # O(nlogk)
    return greedy2_ts(n, hi, c, e, m)