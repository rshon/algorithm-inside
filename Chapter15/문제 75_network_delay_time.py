import collections
import heapq
from typing import List
from typing import Optional
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.list import ListNode, create_linked_list_from_nums, list_get_nums
from common.tree import TreeNode, deserialize, traverse_level


def get_min_delay(links: List[List[int]], n: int, start_node: int) -> int:
    g = collections.defaultdict(dict)
    for u, v, w in links:
        g[u][v] = w
    
    q = [(0, start_node)]
    visited = set()

    while q:
        inc, u = heapq.heappop(q)
        visited.add(u)

        if len(visited) == n:
            return inc
        
        for v, w in g[u].items():
            if v in visited:
                continue
            
            heapq.heappush(q, (inc + w, v))
    
    return -1


delay = get_min_delay([[1,2,3],[1,3,5],[2,3,2],[2,4,1],[4,3,3],[3,5,3],[4,5,8]], 5, 1)
assert(8 == delay)
