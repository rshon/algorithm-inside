

def merge_sort(nums):
    if len(nums) < 2:
        return nums

    m = len(nums) // 2
    left = merge_sort(nums[:m])
    right = merge_sort(nums[m:])
    merged_nums = []

    lpos = 0
    rpos = 0

    while lpos < len(left) or rpos < len(right):
        if lpos < len(left) and rpos < len(right):
            if left[lpos] > right[rpos]:
                merged_nums += right[rpos],
                rpos += 1
            else:
                merged_nums += left[lpos],
                lpos += 1
        elif lpos < len(left):
            merged_nums += left[lpos],
            lpos += 1
        else:
            merged_nums += right[rpos],
            rpos += 1

    return merged_nums


nums = [3, 4, 2, 1, 5]
print(merge_sort(nums))
