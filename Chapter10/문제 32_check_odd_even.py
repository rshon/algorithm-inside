from typing import List


nums = [5, 3, 8, 12]


def sort_even_odd(nums: List[int]) -> List[int]:
    l = 0
    r = 0
    
    while r < len(nums):
        if 0 == nums[r] % 2:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
        r += 1
    
    return nums


print([8, 12, 5, 3] == sort_even_odd(nums))