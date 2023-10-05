import collections
from typing import List
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))


def get_max_rank(n: int, roads: List[List[int]]) -> int:
    if not roads:
        return 0

    g = collections.defaultdict(list)
    for u, v in roads:
        g[u] += v,
        g[v] += u,
    
    most = sorted(g.items(), key=lambda p: len(p[1]), reverse=True)
    mx = 0
    i = 0

    while i < len(most) and len(most[i][1]) == len(most[0][1]):
        u = most[i][0]
        num_u = len(g[u])
        
        for v in range(n):
            if v == u:
                continue
            
            neis = len(g[v])
            if u in g[v]:
                neis -= 1
            
            mx = max(mx, num_u + neis)

        i += 1

    return mx


rank = get_max_rank(n=5, roads=[[0, 2], [2, 1], [2, 3], [1, 4], [1, 5]])
assert(5 == rank)
