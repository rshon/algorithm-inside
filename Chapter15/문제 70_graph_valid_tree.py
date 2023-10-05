import collections


links = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
n = 5


def is_no_cycle(n, edges):
    parents = collections.defaultdict(int)

    for u, v in edges:
        parents[u] = u
        parents[v] = v
        
    def get_root(parents, idx):
        while parents[idx] != idx:
            idx = parents[idx]
        return idx

    for u, v in edges:
        u_root = get_root(parents, u)
        v_root = get_root(parents, v)
        if u_root == v_root:
            return False
        
        parents[v_root] = u_root

    return len(edges) == n - 1


def is_no_cycle(n, edges):
    def is_reachable(u, v):
        visited = set()
        visited.add(u)
        q = collections.deque([u])

        while q:
            cur = q.popleft()

            if cur == v:
                return True

            for adj in g[cur]:
                if adj in visited:
                    continue

                q += adj,
                visited.add(adj)

        return False

    g = collections.defaultdict(list)
    for u, v in edges:
        if is_reachable(u, v):
            return False

        g[u] += v,
        g[v] += u,

    return len(edges) == n - 1


assert(False == is_no_cycle(n, links))