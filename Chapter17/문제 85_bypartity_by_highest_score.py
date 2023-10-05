from typing import List


def get_max_profit_position(nums: List[int]) -> List[int]:
    n = len(nums)
    zeros = [0] * (n + 1)
    ones = [0] * (n + 1)
    
    for i in range(1, len(nums) + 1):
        zeros[i] = zeros[i - 1]
        if 0 == nums[i - 1]:
            zeros[i] += 1
    
    for i in range(len(nums) - 1, -1, -1):
        ones[i] = ones[i + 1]
        if 1 == nums[i]:
            ones[i] += 1
    
    mx = 0
    for i in range(n + 1):
        mx = max(mx, ones[i] + zeros[i])
    
    res = []
    for i in range(n + 1):
        if mx == ones[i] + zeros[i]:
            res.append(i)
    
    return res


res = get_max_profit_position([0, 0, 1, 0])
print(res)
