import sys
input = sys.stdin.readline
from collections import deque
from itertools import combinations


def bfs(q):
    visited = [[False] * N for _ in range(N)]
    for x, y in q:
        visited[x][y] = True
    time = -1
    cnt = len(q)
    while q:
        for _ in range(len(q)):
            x, y = q.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and not matrix[nx][ny] == 1:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    cnt += 1
        time += 1
    return cnt, time

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

N, M = map(int, input().split())
matrix = []
# 모든 빈칸에 바이러스가 있게되는 최소 시간.
initial_points = []
wall = 0
for i in range(N):
    a = list(map(int, input().split()))
    for j in range(N):
        if a[j] == 2:
            initial_points.append((i,j))
        elif a[j] == 1:
            wall += 1
    matrix.append(a)

min_count = float('inf')
for virus_set in combinations(initial_points, M):
    q = deque()
    for virus in virus_set:
        q.append(virus)
    cnt, time = bfs(q)
    if cnt + wall == N**2:
        min_count = min(min_count, time)
if min_count == float('inf'):
    min_count = -1
print(min_count)