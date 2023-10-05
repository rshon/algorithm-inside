import collections


intervals = [[2,3],[4,5],[6,7],[8,9],[1,6]]
intervals = collections.deque(sorted(intervals))
res = []
pre = intervals.popleft()

while intervals:
    cur = intervals.popleft()
    if pre[1] >= cur[0] and pre[0] <= cur[1]:
        pre[0] = min(pre[0], cur[0])
        pre[1] = max(pre[1], cur[1])
    else:
        res += pre,
        pre = cur

res += pre,

print(res == [[1, 7], [8, 9]])
