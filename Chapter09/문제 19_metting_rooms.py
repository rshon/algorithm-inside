
intervals = [(6, 15), (13, 20), (6, 17)]
cnt = 0
mx = 0
times = []

for start, end in intervals:
    times += (start, 1),
    times += (end, -1),

times.sort(key=lambda p: p[0])

for time, inc in times:
    cnt += inc
    mx = max(mx, cnt)


print(mx)
