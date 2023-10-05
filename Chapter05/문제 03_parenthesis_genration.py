

def generate(open_cnt, close_cnt, sequence, results):
    if open_cnt == n and close_cnt == n:
        results += sequence,
        return

    if open_cnt < n:
        generate(open_cnt + 1, close_cnt, sequence + '(', results)
    
    if close_cnt < open_cnt:
        generate(open_cnt, close_cnt + 1, sequence + ')', results)

n = 2
results = []
generate(0, 0, '', results)
print(results)
