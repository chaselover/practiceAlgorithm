import sys
from collections import deque, defaultdict
input = sys.stdin.readline


def find_continent(x, y):
    q = deque()
    q.append((x, y))
    matrix[x][y] = numbering
    while q:
        x, y = q.popleft()
        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                if matrix[nx][ny] == 1:
                    matrix[nx][ny] = numbering
                    q.append((nx, ny))
                elif not matrix[nx][ny]:
                    matrix[nx][ny] = numbering
                    water.append((nx, ny))
                    dists[(nx, ny)] = 1


def find_another_continent():
    min_val = float('inf')
    while water:
        for _ in range(len(water)):
            x, y = water.popleft()
            for dx, dy in delta:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < N:
                    if not matrix[nx][ny]:
                        matrix[nx][ny] = matrix[x][y]
                        water.append((nx, ny))
                        dists[(nx, ny)] = dists[(x, y)] + 1
                    else:
                        if matrix[x][y] != matrix[nx][ny]:
                            min_val = min(min_val, dists[(nx, ny)] + dists[(x, y)])
        if min_val != float('inf'):
            return min_val


N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

numbering = 2
delta = ((1, 0), (0, 1), (-1, 0), (0, -1))

water = deque()
dists = defaultdict(int)
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1:
            find_continent(i, j)
            numbering += 1
print(find_another_continent())
