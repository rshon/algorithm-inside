import collections


def maze(maze, sy, sx, dy, dx):
    rows = len(maze)
    cols = len(maze[0])
    visited = {(sy, sx)}
    queue = collections.deque([(sy, sx)])

    while queue:
        y, x = queue.popleft()
        if y == dy and x == dx:
            return True
        
        for oy, ox in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            my = y
            mx = x

            while (0 <= my + oy < rows and 
                   0 <= mx + ox < cols and 
                   maze[my + oy][mx + ox] == 0):
                my += oy
                mx += ox
            
            if (my, mx) not in visited:
                visited.add((my, mx))
                queue.append((my, mx))
    
    return False


grid = [
    [1, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 0, 1],
    [0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 0, 0]
]

print(maze(grid, 0, 1, len(grid) - 1, len(grid[0]) - 1))