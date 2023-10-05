import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))


graph = [[1, 2], [], [1, 3], [0]]


def find_save_vertices(graph):
    WHITE, GRAY, BLACK = 0, 1, 2
    n = len(graph)
    state = [WHITE] * n

    def dfs(node):
        state[node] = GRAY
        
        for adj in graph[node]:
            if state[adj] == BLACK:
                continue
            if state[adj] == GRAY:
                return False

            if False == dfs(adj):
                return False

        state[node] = BLACK
        return True
    
    res = []
    for node in range(n):
        ret = False
        if state[node] == WHITE:
            ret = dfs(node)
        elif state[node] == BLACK:
            ret = True
        
        if True == ret:
            res += node,

    return res


assert([1] == find_save_vertices(graph))