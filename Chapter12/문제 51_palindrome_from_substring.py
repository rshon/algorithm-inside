import collections
from typing import List


s = "zaoza"
requests = [[1,2,0],[0,3,1],[0,4,1],[2,3,1]]


def can_make_palindrome(s: str, requests: List[List[int]]) -> List[bool]:
    dp = [collections.Counter()]
    
    for i in range(len(s)):
        dp += dp[-1] + collections.Counter(s[i]),
    
    res = []
    for l, r, k in requests:
        req = dp[r + 1] - dp[l]
        need = sum(v%2 for v in req.values())//2
        res += need <= k,
    
    return res


print(can_make_palindrome(s, requests) == [False, True, True, True])
