
def traverse_spiral_order(matrix: [[int]]) -> [int]:
    rows = len(matrix)
    cols = len(matrix[0])
    
    visited = set()
    res = [matrix[0][0]]
    y = 0
    x = 0
    
    while True:
        visited.add((y, x))
        cnt = 0
        
        for oy, ox in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            while (0 <= y + oy < rows and 0 <= x + ox < cols):
                if (y + oy, x + ox) in visited:
                    break

                y += oy
                x += ox

                visited.add((y, x))
                res += matrix[y][x],
                cnt += 1

        if not cnt:
            break

    return res


print(traverse_spiral_order([[1,2,3],[8,9,4],[7,6,5]]))