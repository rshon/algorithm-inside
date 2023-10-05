import collections
from typing import List


coordinates = [[0,0],[3,3],[4,9],[6,4],[7,3]]


def get_min_cost_for_coorinates(coordinates: List[List[int]]) -> int:
    links = []

    n = len(coordinates)
    for i in range(n - 1):
        for j in range(i + 1, n):
            w = abs(coordinates[i][0] - coordinates[j][0]) + \
                abs(coordinates[i][1] - coordinates[j][1])
            links += (i, j, w),

    links = collections.deque(sorted(links, key=lambda p: p[2]))
    
    union = [i for i in range(n)]
    
    def find_root(key):
        while union[key] != key:
            key = union[key]
        return key
    
    cost = 0
    cnt = 0

    while links and cnt < n - 1:
        u, v, w = links.popleft()
        uroot = find_root(u)
        vroot = find_root(v)
        
        if uroot != vroot:
            union[vroot] = uroot
            cost += w
            cnt += 1
    
    return cost


assert(19 == get_min_cost_for_coorinates(coordinates))