from typing import List


def search(nums: List[int], target: int) -> int:
    if not nums:
        return -1

    n = len(nums)
    left = 0
    right = n - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid

        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1

    return -1


arr = [2, 4, 5, 9, 11, 24, 70, 101]
print(2 == search(arr, 5))
