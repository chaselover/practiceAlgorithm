import sys
input = sys.stdin.readline
from collections import deque

def spread_water():
    new_water = []
    while water:
        x, y = water.pop()
        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            if 0 <= nx < R and 0 <= ny < C and maps[nx][ny] == '.':
                maps[nx][ny] = '*'
                new_water.append((nx, ny))
    while new_water:
        water.append(new_water.pop())

def bfs(x, y):
    visited = [[False] * C for _ in range(R)]
    visited[x][y] = True
    q = deque()
    q.append((x,y))
    time = 0
    while q:
        spread_water()
        for __ in range(len(q)):
            x, y = q.popleft()
            for dx, dy in delta:
                nx, ny = x + dx, y + dy
                if 0 <= nx < R and 0 <= ny < C:
                    if maps[nx][ny] == '.' and not visited[nx][ny]:
                        visited[nx][ny] = True
                        q.append((nx, ny))
                    elif maps[nx][ny] == 'D':
                        return time + 1
        time += 1
    return 'KAKTUS'

R, C = map(int, input().split())
maps = [list(input().rstrip()) for _ in range(R)]
water = []
for i in range(R):
    for j in range(C):
        if maps[i][j] == 'D':
            cave = (i, j)
        elif maps[i][j] == 'S':
            dochi = [i, j]
            maps[i][j] = '.'
        elif maps[i][j] == '*':
            water.append((i, j))
delta = ((0, 1), (0, -1), (1, 0), (-1, 0))
print(bfs(*dochi))
