from typing import List
import collections


def find_elapse_time(grid: List[List[int]]) -> int:
    rows = len(grid)
    cols = len(grid[0])

    q = collections.deque()
    visited = set()
    elapse = 0

    for y in range(rows):
        for x in range(cols):
            if 2 == grid[y][x]:
                q += (y, x, 0),
                visited.add((y, x))

    while q:
        y, x, elapse = q.popleft()

        for ay, ax in [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)]:
            if (ay, ax) in visited:
                continue

            if not (0 <= ay < rows and 0 <= ax < cols):
                continue

            if 1 == grid[ay][ax]:
                q += (ay, ax, elapse + 1),
                grid[ay][ax] = 2
                visited.add((ay, ax))

    if any([1 == cell for line in grid for cell in line]):
        return -1

    return elapse


grid = [
    [1,0,0],
    [2,1,1],
    [0,1,0]
]

print(find_elapse_time(grid))