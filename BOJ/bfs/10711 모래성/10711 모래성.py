import sys
input = sys.stdin.readline
from collections import deque


def make_water(H, W):
    waters = deque()
    for i in range(H):
        for j in range(W):
            if sands[i][j].isnumeric():
                sands[i][j] = int(sands[i][j])
            else:
                sands[i][j] = 0
                waters.append((i, j))
                
    return waters


H, W = map(int, input().split())
sands = [list(map(str, input())) for _ in range(H)]
waters = make_water(H, W)

answer = 0
cnts = [[0] * W for _ in range(H)]
delta = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))

while waters:
    x, y = waters.popleft()
    for dx, dy in delta:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < H and 0 <= ny < W:
            if sands[nx][ny]:
                sands[nx][ny] -= 1
                if not sands[nx][ny]:
                    waters.append((nx, ny))
                    cnts[nx][ny] = cnts[x][y] + 1
                    answer = max(answer, cnts[nx][ny])

print(answer)