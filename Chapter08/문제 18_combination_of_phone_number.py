import collections


keys = collections.defaultdict(list)
keys['2'] = ['a', 'b', 'c']
keys['3'] = ['d', 'e', 'f']
keys['4'] = ['g', 'h', 'i']
keys['5'] = ['j', 'k', 'l']
keys['6'] = ['m', 'n', 'o']
keys['7'] = ['p', 'q', 'r', 's']
keys['8'] = ['t', 'u', 'v']
keys['9'] = ['w', 'x', 'y', 'z']


def permutate(digits, k, start, seq, res):
    if k == 0:
        res += seq,
        return
    
    for i in range(len(keys[digits[start]])):
        permutate(digits, k - 1, start + 1, seq + keys[digits[start]][i], res)


digits = "56"
res = []
permutate(digits, len(digits), 0, '', res)
print(res)
