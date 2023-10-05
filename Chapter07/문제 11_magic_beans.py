from typing import List


def get_min_magic_bean(beans: List[int]) -> int:
    n = len(beans)
    diffs = []
    
    for i, num in enumerate(sorted(beans)):
        diffs += (n - i) * num,
    
    return sum(beans) - max(diffs)


print(get_min_magic_bean([4, 2, 1, 3]))