import collections


def update_matrix(grid):
    rows = len(grid)
    cols = len(grid[0])
    q = collections.deque()
    visited = set()

    for y in range(rows):
        for x in range(cols):
            if 0 == grid[y][x]:
                q += (y, x, 0),
                visited.add((y, x))

    while q:
        y, x, dist = q.popleft()

        for ny, nx in [(y + 1, x), (y - 1, x), (y, x + 1), (y, x + -1)]:
            if not (0 <= ny < rows and 0 <= nx < cols):
                continue

            if (ny, nx) not in visited or \
                ((ny, nx) in visited and grid[ny][nx] > dist + 1):
                visited.add((ny, nx))
                grid[ny][nx] = dist + 1
                q.append((ny, nx, dist + 1))

    return grid


res = update_matrix([
    [0, 0, 0],
    [0, 1, 0],
    [1, 1, 1]])

for line in res:
    print(line)

