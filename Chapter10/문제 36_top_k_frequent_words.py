import collections


words = ["this", "is", "some", "good", "time", "to", "code", "some", "good", "code"]
r = 3


def pick_frequent_words(nums: [str], k: int) -> [str]:
    freq = collections.Counter(nums)
    freq = sorted(freq.items(), key=lambda p: (p[1], p[0]), reverse=True)

    words_in_freq = collections.defaultdict(list)

    for word, cnt in freq:
        words_in_freq[cnt] += word,

    res = []
    all_freqs = sorted(words_in_freq.keys(), reverse=True)
    
    for cur_freq in all_freqs:
        num_words = len(words_in_freq[cur_freq])

        if num_words <= k:
            res += sorted(words_in_freq[cur_freq])[:num_words]
            k -= num_words
        else:
            res += sorted(words_in_freq[cur_freq])[:k]
            k -= k
    
    return res


print(pick_frequent_words(words, r) == ['code', 'good', 'some'])