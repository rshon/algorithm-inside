import collections
import heapq


def turn_cost(grid):
    m = len(grid)
    n = len(grid[0])
    q = [(0, 0, 0)]
    turn_cost = collections.defaultdict(lambda: float('inf'))

    while q:
        cost, y, x = heapq.heappop(q)

        if (y, x) == (m - 1, n - 1):
            return cost

        for direction, ny, nx in [(1, y, x + 1), (2, y, x - 1), (3, y + 1, x), (4, y - 1, x)]:
            if not (0 <= ny < m and 0 <= nx < n):
                continue

            next_cost = cost if direction == grid[y][x] else cost + 1
        
            if turn_cost[(ny, nx)] <= next_cost:
                continue

            heapq.heappush(q, (next_cost, ny, nx))
            turn_cost[(ny, nx)] = next_cost
    
    return -1
    
    