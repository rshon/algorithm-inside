from typing import List


def get_largest_square_size(grid: List[List[str]]) -> int:
    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    grid = [[int(grid[y][x]) for x in range(cols)] for y in range(rows)]

    for y in range(1, rows):
        for x in range(1, cols):
            if 0 == grid[y][x]:
                continue

            grid[y][x] = min(grid[y - 1][x], 
               grid[y][x - 1], 
               grid[y - 1][x - 1]) + 1

    return max([max(line) for line in grid])**2


assert(9 == get_largest_square_size(
         [["0","0","0","1"],
          ["1","1","0","1"],
          ["1","1","1","1"],
          ["0","1","1","1"],
          ["0","1","1","1"]]))

