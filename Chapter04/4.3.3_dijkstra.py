import collections
import heapq


edges = [[1, 2, 4], [1, 3, 2], [2, 5, 3], [3, 4, 1], [4, 5, 3], [4, 6, 5], [5, 7, 4], [6, 7, 5]]
g = collections.defaultdict(lambda: collections.defaultdict(int))

for u, v, w in edges:
    g[u][v] = w

start = 1


def dijkstra2(g, start):
    dists = collections.defaultdict(lambda: float('inf'))
    dists[start] = 0
    q = [(0, start, [start])]

    while q:
        dist, u, trace = heapq.heappop(q)

        if dists[u] < dist:
            continue

        for v, w in g[u].items():
            if dist + w < dists[v]:
                print('dists[{}] = {}, trace = {}'.format(v, dist + w, trace + [v]))
                dists[v] = dist + w
                heapq.heappush(q, (dist + w, v, trace + [v]))

    return dists


def dijkstra(g, start):
    q = [(0, start)]

    dists = collections.defaultdict(lambda: float('inf'))
    dists[start] = 0

    while q:
        dist, u = heapq.heappop(q)

        if dists[u] < dist:
            continue

        for v, weight in g[u].items():
            if weight + dist < dists[v]:
                heapq.heappush(q, (weight + dist, v))
                dists[v] = weight + dist
        
    return dists


dists = dijkstra(g, start)
print('dists = ', dists)