
def get_num_of_combinations(nums, target):
    dp = [0]*(target + 1)
    dp[0] = 1

    for i in range(min(nums), target + 1):
        for num in nums:
            if num <= i:
                dp[i] += dp[i - num]

    return dp[-1]


res = get_num_of_combinations(nums = [1, 3, 4], target = 5)
assert(6 == res)
