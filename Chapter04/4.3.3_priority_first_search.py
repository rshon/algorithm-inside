import heapq
import collections


edges = [
    ['A', 'B', 2],
    ['B', 'D', 5],
    ['B', 'C', 3],
    ['A', 'C', 4],
    ['C', 'D', 7],
    ['C', 'G', 3],
    ['D', 'E', 2],
    ['G', 'E', 1],
    ['E', 'F', 3],
    ['G', 'F', 4],
]


links = [
    ['A', 'B', 2],
    ['A', 'C', 4],
    ['B', 'C', 3],
    ['B', 'D', 5],
    ['C', 'D', 7],
    ['C', 'G', 3],
    ['G', 'E', 1],
    ['D', 'E', 2],
    ['F', 'E', 3],
    ['F', 'G', 4]
]



def prio_first_search(start_name, edges):
    g = collections.defaultdict(lambda: collections.defaultdict(int))

    for u, v, w in edges:
        g[u][v] = w
        g[v][u] = w

    q = [(0, start_name, start_name)]
    visited = set()
    edges = []

    while q:
        dist, src, u = heapq.heappop(q)
        if u in visited:
            continue

        visited.add(u)
        edges += (src, u),

        for v, w in g[u].items():
            heapq.heappush(q, (dist + w, u, v))

    return edges


edges = prio_first_search('A', edges)
for u, v in edges:
    print(u, v)
