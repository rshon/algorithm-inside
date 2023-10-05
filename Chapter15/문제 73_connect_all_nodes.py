import collections
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))


n = 6
cables = [[0, 1], [0, 2], [0, 3], [1, 2], [2, 3]]


def get_cable_move(n: int, cables: [[int]]) -> int:
    if len(cables) < n - 1:
        return -1
    
    g = collections.defaultdict(set)
    for u, v in cables:
        g[u].add(v)
        g[v].add(u)

    visited = set()

    def dfs(node):
        q = [node]
        while q:
            node = q.pop()
            visited.add(node)
            
            for adj in g[node]:
                if adj in visited:
                    continue
                q += adj,
            
        return 1

    move = 0
    for node in range(n):
        if node not in visited:
            move += dfs(node)

    return move - 1


assert(2 == get_cable_move(n, cables))