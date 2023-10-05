
nums = [4, 8, 1, 2, 9, 3]


toggle = True

for i in range(len(nums)):
    if toggle:
        min_max = min(nums[i:]) 
    else:
        min_max = max(nums[i:])

    idx = nums[i:].index(min_max)
    nums[i], nums[i + idx] = nums[i + idx], nums[i]
    toggle = not toggle

print(nums)