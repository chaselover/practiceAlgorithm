import sys
input = sys.stdin.readline
from collections import deque


def rotate_dust():
    up_cycle = deque()
    down_cycle = deque()
    up_cycle_down, down_cycle_up = air_clear[0][0], air_clear[1][0]

    # 0, 공기청정기 x 작은 좌표, 좌, 우 -> rotate(-1)
    for i in range(C):
        up_cycle.append(matrix[0][i])
    for i in range(1, up_cycle_down):
        up_cycle.append(matrix[i][C-1])
    for i in range(C-1, -1, -1):
        up_cycle.append(matrix[up_cycle_down][i])
    for i in range(up_cycle_down-1, 0, -1):
        up_cycle.append(matrix[i][0])
    up_cycle.rotate(-1)
    for i in range(C):
        matrix[0][i] = up_cycle.popleft()
    for i in range(1, up_cycle_down):
        matrix[i][C-1] = up_cycle.popleft()
    for i in range(C-1, -1, -1):
        matrix[up_cycle_down][i] = up_cycle.popleft()
    for i in range(up_cycle_down-1, 0, -1):
        matrix[i][0] = up_cycle.popleft()
    matrix[air_clear[0][0]][air_clear[0][1]] = 0

    # R, 공기청정기 x 큰 좌표, 좌, 우 -> rotate(1)
    for i in range(C):
        down_cycle.append(matrix[down_cycle_up][i])
    for i in range(down_cycle_up + 1, R):
        down_cycle.append(matrix[i][C-1])
    for i in range(C-2, -1, -1):
        down_cycle.append(matrix[R-1][i])
    for i in range(R - 2, down_cycle_up, -1):
        down_cycle.append(matrix[i][0])
    down_cycle.rotate(1)
    for i in range(C):
        matrix[down_cycle_up][i] = down_cycle.popleft()
    for i in range(down_cycle_up + 1, R):
        matrix[i][C-1] = down_cycle.popleft()
    for i in range(C-2, -1, -1):
        matrix[R-1][i] = down_cycle.popleft()
    for i in range(R - 2, down_cycle_up, -1):
        matrix[i][0] = down_cycle.popleft()
    matrix[air_clear[1][0]][air_clear[1][1]] = 0



def spread_dust(dusts):
    new_dusts = []

    for dust in dusts:
        x, y = dust
        init_dust = matrix[x][y]
        cnt = 0
        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            if 0 <= nx < R and 0 <= ny < C and not (nx, ny) in air_clear:
                new_dusts.append((nx, ny, init_dust//5))
                cnt += 1
        new_dusts.append((x, y, init_dust - cnt * (init_dust//5)))
        matrix[x][y] = 0

    for dust in new_dusts:
        x, y, a = dust
        matrix[x][y] += a


delta = ((0, -1), (1, 0), (-1, 0), (0, 1))

R, C, T = map(int, input().split())
matrix = []
air_clear = []
dusts = []
for i in range(R):
    row = list(map(int, input().split()))
    for j in range(C):
        if row[j] == -1:
            air_clear.append((i,j))
            row[j] = 0
        elif row[j]:
            dusts.append((i,j))
    matrix.append(row)

for __ in range(T):
    # 1. 미세먼지 확산.
    spread_dust(dusts)
    # 2. 공기청정기 작동. 원 2개 순환.
    rotate_dust()

    answer = 0
    dusts = []
    for i in range(R):
        for j in range(C):
            if matrix[i][j]:
                dusts.append((i,j))
                answer += matrix[i][j]
print(answer)