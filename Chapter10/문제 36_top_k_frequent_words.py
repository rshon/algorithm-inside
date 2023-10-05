import collections


words = ["this", "is", "some", "good", "time", "to", "code", "some", "good", "code"]
r = 3


def pick_frequent_words(nums: [str], k: int) -> [str]:
    freq = collections.Counter(nums)
    freq = sorted(freq.items(), key=lambda p: (p[1], p[0]), reverse=True)
    return sorted([item[0] for item in freq[:k]])


print(pick_frequent_words(words, r) == ['code', 'good', 'some'])