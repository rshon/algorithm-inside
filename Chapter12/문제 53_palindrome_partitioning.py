
s = "uoupp"


def get_palindrome_partitions(s: str):
    def permutate(s, seq, res):
        if not s:
            res += seq,
            return

        for i in range(1, len(s) + 1):
            if s[:i] == s[:i][::-1]:
                permutate(s[i:], seq + [s[:i]], res)

    res = []
    permutate(s, [], res)
    return res


print(get_palindrome_partitions(s) == [['u', 'o', 'u', 'p', 'p'], ['u', 'o', 'u', 'pp'], ['uou', 'p', 'p'], ['uou', 'pp']])