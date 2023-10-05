from typing import List


mat = [[9,7,2,3],[0,3,8,1],[3,3,9,4]]


def sort_diagonal_elements(mat: [[int]]) -> [[int]]:
    def sort_diag(mat, sy, sx):
        y = sy
        x = sx
        diag = []

        while y < m and x < n:
            diag += mat[y][x],
            y += 1
            x += 1
        
        diag.sort()

        i = 0
        y = sy
        x = sx

        while y < m and x < n:
            mat[y][x] = diag[i]
            i += 1
            y += 1
            x += 1

    m = len(mat)
    n = len(mat[0])
    
    for sy in range(m):
        sort_diag(mat, sy, 0)

    for sx in range(1, n, 1):
        sort_diag(mat, 0, sx)
    
    return mat


print([[3, 4, 1, 3], [0, 9, 7, 2], [3, 3, 9, 8]] == sort_diagonal_elements(mat))