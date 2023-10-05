
s = "pokijokpq"
p = "kop"


def find_anagrams(s: str, p: str) -> [int]:
    def get_idx(ch):
        return ord(ch) - ord('a')

    def is_same(a, b):
        return all([False if a[i] != b[i] else True for i in range(num_alphabet)])

    m = len(s)
    n = len(p)
    if m < n:
        return []

    num_alphabet = 26
    wnd = [0]*num_alphabet
    ans = [0]*num_alphabet

    for i, ch in enumerate(p):
        ans[get_idx(ch)] += 1

    for i in range(n):
        wnd[get_idx(s[i])] += 1

    res = []
    if is_same(ans, wnd):
        res += 0,

    for i in range(n, m):
        wnd[get_idx(s[i - n])] -= 1
        wnd[get_idx(s[i])] += 1

        if is_same(ans, wnd):
            res += i - n + 1,

    return res


print(find_anagrams(s, p) == [0, 5])