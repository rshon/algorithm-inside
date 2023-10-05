import collections


def bfs(g, visited, u):
    q = collections.deque([u])
    visited = {u}

    while q:
        u = q.popleft()
        print('visit = ', u)

        for v in g[u]:
            if v in visited:
                continue

            visited.add(v)
            q.append(v)


g = collections.defaultdict(list)

edges = [(1, 2), (1, 3), (3, 5), (1, 4), (4, 6)]

for u, v in edges:
    g[u] += v,

bfs(g, set(), 1)