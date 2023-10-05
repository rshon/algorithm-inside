
import collections


links = [[1, 3], [2, 5], [4, 5], [3, 6], [5, 6], [6, 8], [7, 8]]


def visit_in_topological_order(links):
    g = collections.defaultdict(list)
    indegree = collections.defaultdict(int)
    for u, v in links:
        g[u] += v,
        indegree[u] = indegree[u]
        indegree[v] += 1

    q = collections.deque([vertex for vertex, degree in indegree.items() if 0 == degree])

    visit_trace = []
    visited = set()

    for vertex in q:
        visited.add(vertex)

    while q:
        u = q.popleft()
        visit_trace += u,

        for v in g[u]:
            indegree[v] -= 1
            if 0 == indegree[v] and v not in visited:
                q += v,
                visited.add(v)

    return visit_trace


trace = visit_in_topological_order(links)
print(trace)





