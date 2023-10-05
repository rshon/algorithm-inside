import collections


def dfs(g, u):
    q = [u]
    visited = {u}

    while q:
        u = q.pop()
        print('visit = ', u)

        for v in g[u]:
            if v in visited:
                continue

            visited.add(v)
            q += v,


g = collections.defaultdict(list)

edges = [(1, 2), (1, 3), (3, 5), (1, 4), (4, 6)]

for u, v in edges:
    g[u] += v,

dfs(g, 1)