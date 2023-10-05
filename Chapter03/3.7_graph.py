import collections
from collections import defaultdict


n = 5
edges = [[1, 2], [2, 3], [2, 4], [2, 5]]
weighted_edges = [[1, 2, 2], [2, 3, 3], [2, 4, 1], [2, 5, 2]]


def adj_mat1():
    adj_mat = [[0]*n for _ in range(n)]

    for u, v in edges:
        adj_mat[u - 1][v - 1] = 1
        adj_mat[v - 1][u - 1] = 1

    for line in adj_mat:
        print(line)

    print(adj_mat[0][1])
    print(adj_mat[0][4])


def adj_mat2():
    adj_mat = [[0]*(n + 1) for _ in range(n + 1)]

    for u, v in edges:
        adj_mat[u][v] = 1
        adj_mat[v][u] = 1

    for line in adj_mat:
        print(line)

    print(adj_mat[1][2])
    print(adj_mat[1][5])


def weighted_adj_mat2():
    adj_mat = [[0]*(n + 1) for _ in range(n + 1)]

    for u, v, w in weighted_edges:
        adj_mat[u][v] = w
        adj_mat[v][u] = w

    for line in adj_mat:
        print(line)

    print(adj_mat[1][2])
    print(adj_mat[1][5])


def adj_list():
    adj_list = [[] for _ in range(n + 1)]

    for u, v in edges:
        adj_list[u] += v,
        adj_list[v] += u,

    for row in adj_list:
        print(row)

    def is_edge_exist(u, v):
        for vertex in adj_list[u]:
            if v == vertex:
                return True

        return False

    print(is_edge_exist(1, 2))
    print(is_edge_exist(1, 5))


def weighed_adj_list():
    adj_list = [[] for _ in range(n + 1)]

    for u, v, w in weighted_edges:
        adj_list[u] += (v, w),
        adj_list[v] += (v, u),

    for row in adj_list:
        print(row)

    def is_edge_exist(u, v):
        for vertex in adj_list[u]:
            if v == vertex[0]:
                return True

        return False

    print(is_edge_exist(1, 2))
    print(is_edge_exist(1, 5))


def adj_set():
    graph = [set() for _ in range(n + 1)]

    for u, v in edges:
        graph[u].add(v)
        graph[v].add(u)

    for row in graph:
        print(row)

    print(2 in graph[1])
    print(5 in graph[1])


def adj_dict():
    graph = {}

    for u, v in edges:
        if u not in graph:
            graph[u] = {}
        graph[u][v] = True

        if v not in graph:
            graph[v] = {}
        graph[v][u] = True

    for row in graph.items():
        print(row)

    print(2 in graph[1])
    print(5 in graph[1])


def weighted_adj_dict():
    graph = {}

    for u, v, w in weighted_edges:
        if u not in graph:
            graph[u] = {}
        graph[u][v] = w

        if v not in graph:
            graph[v] = {}
        graph[v][u] = w

    for row in graph.items():
        print(row)

    print(graph[1][2])
    print(graph[1][5])


def weighted_adj_dict_with_collections():
    graph = defaultdict(lambda: defaultdict(int))

    for u, v, w in weighted_edges:
        graph[u][v] = w
        graph[v][u] = w

    for row in graph.items():
        print(row)

    print(graph[1][2])
    print(graph[1][5])


weighted_adj_dict_with_collections()