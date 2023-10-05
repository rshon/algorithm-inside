
s = "ziveii"


def find_min_num_letters(s: str) -> int:
    n = len(s)
    dp = [[0]*(n + 1) for i in range(n + 1)]
    rs = s[::-1]
    
    for i in range(n):
        for j in range(n):
            if s[i] == rs[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])
    
    return n - dp[-1][-1]


print(3 == find_min_num_letters(s))