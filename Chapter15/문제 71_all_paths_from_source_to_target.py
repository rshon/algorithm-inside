import collections
from typing import List
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))


graph = [[1, 2, 3], [2, 3], [3], []]


def get_all_paths(graph: List[List[int]]) -> List[List[int]]:
    n = len(graph)
    q = collections.deque([(0, [0])])
    res = []

    while q:
        u, trace = q.popleft()

        for v in graph[u]:
            q += (v, trace + [v]),

        if u == n - 1:
            res += trace,

    return res


assert([[0, 3], [0, 1, 3], [0, 2, 3], [0, 1, 2, 3]] == get_all_paths(graph))