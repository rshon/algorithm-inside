import collections


sentence1 = "I have an expensive doll"
sentence2 = "I have an adorable doll"


def find_uncommon_words():
    def update_frequency(sentence, freq):
        for word in sentence.split():
            if word not in freq:
                freq[word] = 0

            freq[word] += 1

    freq = {}
    update_frequency(sentence1, freq)
    update_frequency(sentence2, freq)

    res = []
    for item, num in freq.items():
        if 1 == num:
            res.append(item)

    return res


def find_uncommon_words2():
    freq = collections.Counter(sentence1.split()) + collections.Counter(sentence2.split())
    return [item for item, num in freq.items() if num == 1]


print(["expensive", "adorable"] == find_uncommon_words())