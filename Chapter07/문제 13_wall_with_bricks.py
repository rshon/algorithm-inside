from typing import List
import collections


def find_num_bricks_to_break(wall: List[List[int]]) -> int:
    holes = collections.defaultdict(int)

    for row in wall:
        pos = 0
        for i in range(len(row) - 1):
            pos += row[i]
            holes[pos] += 1

    return len(wall) - max(holes.values()) if holes.values() else len(wall)


print(find_num_bricks_to_break([
    [2,1,1,2],
    [1,3,2],
    [2,3,1],
    [2,1,3],
    [4,1]])
)
   