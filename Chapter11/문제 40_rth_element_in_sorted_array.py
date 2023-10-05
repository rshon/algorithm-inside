

mat = [[1,2,5],[9,14,21],[15,16,25]]
r = 3


def find_rth_element(matrix: [[int]], k: int) -> int:
    def count(matrix, target):
        cnt = 0
        for line in matrix:
            for val in line:
                if val <= target:
                    cnt += 1
        return cnt

    l = matrix[0][0]
    r = matrix[-1][-1]

    while l <= r:
        m = (l + r)//2
        cnt = count(matrix, m)
        if cnt < k:
            l = m + 1
        else:
            r = m - 1

    return l


print(5 == find_rth_element(mat, r))