import copy


def wshall(adj_matrix, n):
    path = [[0]*n for _ in range(n)]
    dists = copy.deepcopy(adj_matrix)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dists[i][j] > dists[i][k] + dists[k][j]:
                    dists[i][j] = dists[i][k] + dists[k][j]
                    path[i][j] = k

    return dists, path


edges = [
    [1, 2, 2], [1, 5, 3], [2, 3, 1], [2, 4, 3], [2, 5, -1], 
    [3, 1, 4], [3, 4, 1], [4, 5, 1], [5, 2, 2], [5, 3, 4]
]
 
n = 5
adj_matrix = [[float('inf')]*n for _ in range(n)]
for i in range(n):
    adj_matrix[i][i] = 0

for u, v, w in edges:
    adj_matrix[u - 1][v - 1] = w
res, path = wshall(adj_matrix, len(adj_matrix))

for i in range(len(res)):
    print(res[i])
print()

for i in range(len(path)):
    print(path[i])

