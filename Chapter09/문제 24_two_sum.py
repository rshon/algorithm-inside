
nums = [1, 2, 3, 6]
target = 5

def twosum():
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if target == nums[i] + nums[j]:
                return [i, j]

    return [-1, -1]


def twosum_2(nums):
    l = 0
    r = len(nums) - 1

    nums = [(nums[i], i) for i in range(len(nums))]
    nums.sort(key=lambda p: p[0])

    while l < r:
        tot = nums[l][0] + nums[r][0]
        if target == tot:
            return sorted([nums[l][1], nums[r][1]])

        if target < tot:
            r -= 1
        else:
            l += 1

    return sorted([nums[l][1], nums[r][1]])


def twosum_3(nums):
    def search(nums, l, target):
        r = len(nums) - 1
        
        while l <= r:
            m = (l + r)//2
            if nums[m][0] == target:
                return m
            
            if nums[m][0] > target:
                r = m - 1
            else:
                l = m + 1
        
        return -1

    snums = [(num, i) for i, num in enumerate(nums)]
    snums.sort(key=lambda p:p[0], reverse=False)

    for i, num in enumerate(snums):
        m = search(snums, i + 1, target - num[0])
        if -1 != m:
            return [snums[i][1], snums[m][1]]

    return [-1, -1]


print(twosum_2(nums))