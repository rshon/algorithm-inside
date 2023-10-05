

def compute_lps(pat, n, lps):
    left = 0
    right = 1

    while right < n:
        if pat[right] != pat[left]:
            if 0 < left:
                left = lps[left - 1]; 
            else:
                lps[right] = 0
                right += 1
            continue

        lps[right] = left + 1
        left += 1
        right += 1


def find_pattern_using_kmp(text, pattern):
    len_text = len(text)
    len_patt = len(pattern)
    lps = [0]*len_patt
    res = []

    compute_lps(pattern, len_patt, lps)

    i = 0
    j = 0

    while i < len_text:
        if text[i] == pattern[j]:
            i += 1
            j += 1

            if j == len_patt:
                res += i - j,
                j = lps[j - 1]
            continue

        if i < len_text:
            if j == 0:
                i += 1
            else:
                j = lps[j - 1]

    return res



print([10] == find_pattern_using_kmp("ABABDABACDABABCABAB", "ABABCABAB"))
print([2, 7] == find_pattern_using_kmp("kkabbzpabbq", "abb"))
print([1, 4] == find_pattern_using_kmp("caabaabaaad", "aabaa"))