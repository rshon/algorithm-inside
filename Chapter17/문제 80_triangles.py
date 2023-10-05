from typing import List


triangle = [
     [3],
    [4,5],
   [1,7,5],
  [2,4,2,8]]


def get_min_path_topdown(triangle):
    rows = len(triangle)

    for i in range(1, rows):
        for j in range(len(triangle[i])):
            if j == 0:
                triangle[i][j] += triangle[i - 1][j]
            elif j == len(triangle[i]) - 1:
                triangle[i][j] += triangle[i - 1][j - 1]
            else:
                triangle[i][j] += min(triangle[i - 1][j - 1], triangle[i - 1][j])

    return min(triangle[-1])


# be careful for that you put triangle that is already modified
def get_min_path_bottomup(triangle: List[List[int]]) -> int:
    mat = triangle
    if len(mat) == 1:
        return mat[0][0]

    for row in range(len(mat) - 2, -1, -1):
        for col in range(len(mat[row])):
            mat[row][col] += min(mat[row + 1][col], mat[row + 1][col + 1])

    return mat[0][0]


print(get_min_path_topdown(triangle))