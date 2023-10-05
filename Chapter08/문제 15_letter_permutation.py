
def permutate(s, idx, seq, res):
    if idx == len(s):
        res += seq,
        return

    if not s[idx].isalpha():
        permutate(s, idx + 1, seq + s[idx], res)
        return
    
    permutate(s, idx + 1, seq + s[idx].lower(), res)
    permutate(s, idx + 1, seq + s[idx].upper(), res)
    

res = []
permutate('a1b2', 0, '', res)
print(res)