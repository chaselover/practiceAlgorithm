import sys
input = sys.stdin.readline
from collections import deque
from itertools import combinations


def bfs(q):
    for x, y in q:
        visited[x][y] = True
        times[x][y] = 0
    cnt = len(q)
    while q:
        for _ in range(len(q)):
            x, y = q.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and not matrix[nx][ny] == 1:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    times[nx][ny] = times[x][y] + 1
                    cnt += 1
    return cnt

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
    visited = [[False] * N for _ in range(N)]
    times = [[-1] * N for _ in range(N)]
    for virus in virus_set:
        q.append(virus)
    cnt = bfs(q)
    max_time = 0
    for i in range(N):
        for j in range(N):
            if not matrix[i][j]:
                max_time = max(max_time, times[i][j])
    if cnt + wall == N**2:
        min_count = min(min_count, max_time)
if min_count == float('inf'):
    min_count = -1
print(min_count)