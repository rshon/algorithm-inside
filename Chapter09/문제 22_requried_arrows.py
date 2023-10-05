import collections


points = [[1, 5], [3, 6], [4, 5], [7, 13], [8, 14]]

points = collections.deque(sorted(points, key=lambda p: p[1]))
end = points[0][1]
cnt = 1

while points:
    if points[0][0] <= end:
        points.popleft()
    else:
        end = points[0][1]
        cnt += 1


print(cnt)