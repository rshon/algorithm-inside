from typing import List


residuals = [2,3,-6,-2]
low_limit = -3
high_limit = 7


def get_num_of_sequences(residuals: List[int], low_limit: int, high_limit: int) -> int:
    scope = high_limit - low_limit
    mn = 0
    mx = 0
    inc = 0
    
    for diff in residuals:
        inc += diff
        mn = min(mn, inc)
        mx = max(mx, inc)
    
    in_scope = mx - mn
    
    return scope - in_scope + 1 if scope >= in_scope else 0


res = get_num_of_sequences(residuals, low_limit, high_limit)
assert(3 == res)