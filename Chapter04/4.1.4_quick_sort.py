
def partition(nums, base, n):
    pivot = nums[base + n - 1]
    l = 0
    r = n - 2

    while l < r:
        while nums[base + l] < pivot:
            l += 1

        while nums[base + r] > pivot:
            r -= 1

        if l < r:
            nums[base + l], nums[base + r] = nums[base + r], nums[base + l]

    nums[base + n - 1], nums[base + l] = nums[base + l], nums[base + n - 1]
    return l


def quick_sort(nums, base, n):
    if n <= 1:
        return
    
    m = partition(nums, base, n)
    quick_sort(nums, base, m)
    quick_sort(nums, m + 1, n - m - 1)


nums = [3, 4, 2, 1, 5]
quick_sort(nums, 0, len(nums))
print(nums)
