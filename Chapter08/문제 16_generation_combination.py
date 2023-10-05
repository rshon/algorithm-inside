
def generate_combination(start, inc, seq, res):
    if inc > target:
        return
    
    if inc == target:
        res += seq,
        return
    
    for i in range(start, len(candidates)):
        generate_combination(i, inc + candidates[i], seq + [candidates[i]], res)


candidates = [2, 3, 6, 7]
target = 7
res = []
generate_combination(0, 0, [], res)
print(res)