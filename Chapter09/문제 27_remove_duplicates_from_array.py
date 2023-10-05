from typing import List


nums = [0, 1, 1, 1, 2, 2, 2, 3]


def remove_continuous_duplicates(nums: List[int]) -> int:
    if not nums:
        return 0

    l = 0
    r = 1
    dup = 0

    while r < len(nums):
        if nums[l] != nums[r]:
            l += 1
            nums[l] = nums[r]
            dup = 0
        elif dup == 0:
            l += 1
            nums[l] = nums[r]
            dup += 1

        r += 1

    return l + 1


print(remove_continuous_duplicates(nums))