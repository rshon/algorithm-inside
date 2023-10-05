import collections


unique_set = "9e1 3p"
words = ["staple", "perk", "peep", "feed"]


def shortest_containing_word(unique_set: str, words: [str]) -> str:
    req = collections.Counter([ch.lower() for ch in unique_set if ch.isalpha()])
    mn = float('inf')
    mn_word = ''

    for word in words:
        freq = collections.Counter(word.lower())

        for ch, num in req.items():
            if freq[ch] < num:
                break
        else:
            if mn > len(word):
                mn = len(word)
                mn_word = word

    return mn_word


print("perk" == shortest_containing_word(unique_set, words))