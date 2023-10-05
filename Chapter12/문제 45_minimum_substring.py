

s = "kuozkoz"
t = "koz"


def find_min_substring(s, t):
    m = len(s)
    n = len(t)

    dp = [[0]*(n + 1) for _ in range(m + 1)]

    for j in range(m + 1):
        dp[j][0] = j + 1
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = dp[i - 1][j]
    start = 0
    length = m + 1

    for i in range(1, m + 1):
        if dp[i][n] != 0:
            if i - dp[i][n] + 1 < length:
                start = dp[i][n] - 1
                length = i - dp[i][n] + 1

    return "" if length == m + 1 else s[start:start + length]


print(find_min_substring(s, t) == "koz")