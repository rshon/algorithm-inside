
def get_num_of_1bits(n):
    dp = [0] * (n + 1)
    i = 0

    while i * 2 <= n:
        dp[i * 2] = dp[i]
        
        if i * 2 + 1 <= n:
            dp[i * 2 + 1] = dp[i] + 1

        i += 1

    return dp


print([0, 1, 1, 2] == get_num_of_1bits(n = 3))