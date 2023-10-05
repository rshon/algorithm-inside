
nums = [3, 4, 2, 3]

def is_increasing_array():
    allowed = True

    for i in range(1, len(nums)):
        if nums[i - 1] > nums[i]:
            if not allowed:
                return False

            allowed = False
            if i == 1:
                nums[i - 1] = nums[i]
            elif i > 1 and nums[i - 2] <= nums[i]:
                nums[i - 1] = nums[i]
            else:
                nums[i] = nums[i - 1]

    return True


print(is_increasing_array())