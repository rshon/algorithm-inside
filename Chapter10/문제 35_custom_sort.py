import collections


order = "kqep"
input = "pekeqr"


def custom_sort_string(order: str, input: str) -> str:
    pos = collections.defaultdict(list)
    uniq = set(order)
    suffix = ''
    sorted = ''
    
    for i, letter in enumerate(input):
        if letter not in uniq:
            suffix += letter
            continue
    
        pos[letter] += i,

    for letter in order:
        for i in pos[letter]:
            sorted += input[i]
    
    sorted += suffix
    return sorted


print("kqeepr" == custom_sort_string(order, input))