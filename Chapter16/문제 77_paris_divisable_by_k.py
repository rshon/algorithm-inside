import collections
import math
from typing import List


nums = [2, 4, 7, 3, 6, 1]
k = 4


def count_pairs(nums: List[int], k: int) -> int:
    res = 0
    freq = collections.defaultdict(int)
    for num in nums:
        freq[math.gcd(num, k)] += 1

    freq = [[num, freq] for num, freq in freq.items()]

    for i in range(len(freq)):
        for j in range(i, len(freq)):
            if freq[i][0] * freq[j][0] % k == 0:
                if i == j:
                    res += freq[i][1] * (freq[i][1] - 1) // 2
                else:
                    res += freq[i][1] * freq[j][1]

    return res


assert(6 == count_pairs(nums, k))