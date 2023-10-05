from typing import List


nums = [2, 4, 6, 8, 9, 3, 1]


def search_peak_index(nums):
    if not nums:
        return

    n = len(nums)
    if 1 == n:
        return 0

    nums = [nums[0] - 1] + nums + [nums[n - 1] - 1]
    peaks = []

    for i in range(1, n + 1):
        if nums[i - 1] < nums[i] and nums[i + 1] < nums[i]:
            peaks.append(i - 1)

    if not peaks:
        return 0

    return peaks[0]


def search_peak_index(nums: List[int]) -> int:
    if not nums:
        return 0

    nums = [nums[0] - 1] + nums + [nums[-1] -1]

    l = 1
    r = len(nums) - 2

    while l <= r:
        m = (l + r)//2
        if nums[m - 1] < nums[m] > nums[m + 1]:
            return m - 1

        if nums[m - 1] < nums[m + 1]:
            l = m + 1
        else:
            r = m - 1

    return l - 1


print(search_peak_index(nums))