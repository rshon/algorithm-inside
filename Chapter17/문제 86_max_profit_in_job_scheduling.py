import bisect
from typing import List


def find_max_profit(intervals: List[int]) -> int:
    intervals.sort(key=lambda p: p[1])
    dp = [[0, 0]]

    for start, end, profit in intervals:
        i = bisect.bisect_left(dp, [start + 1, 0])

        if dp[i - 1][1] + profit > dp[-1][1]:
            dp += [end, dp[i - 1][1] + profit],

    return dp[-1][1]


res = find_max_profit([[0, 3, 15], [2, 4, 20], [4, 7, 30]])
print(50 == res)
