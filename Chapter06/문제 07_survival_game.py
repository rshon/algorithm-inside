from typing import List


def update_next_state(board: List[List[int]]) -> None:
    dirs = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
    rows = len(board)
    cols = len(board[0])

    for y in range(rows):
        for x in range(cols):
            live_cnt = 0

            for oy, ox in dirs:
                ny = y + oy
                nx = x + ox

                if not (0 <= ny < rows and 0 <= nx < cols):
                    continue

                if abs(board[ny][nx]) != 1:
                    continue

                live_cnt += 1

            if board[y][x] == 0 and live_cnt == 3:
                board[y][x] = 2

            if board[y][x] == 1 and (live_cnt < 2 or live_cnt > 3):
                board[y][x] = -1

    for y in range(rows):
        for x in range(cols):
            if board[y][x] >= 1:
                board[y][x] = 1
            else:
                board[y][x] = 0


in_game = [
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]

update_next_state(in_game)
print(in_game)