import sys
input = sys.stdin.readline
from collections import deque

def bfs(i, j):
    q = deque()
    q.append([i, j])
    max_n = 0
    while q:
        a, b = q.popleft()
        for k in range(4):
            x = a + dx[k]
            y = b + dy[k]
            if 0 <= x < n and 0 <= y < m and visit[x][y] == 0 and matrix[x][y] != "W":
                visit[x][y] = 1
                matrix[x][y] = matrix[a][b] + 1
                max_n = max(max_n, matrix[x][y])
                q.append([x, y])
    return max_n


n, m = map(int, input().split())
matrix = [list(input().strip()) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

answer = 0
for i in range(n):
    for j in range(m):
        if matrix[i][j] != "W":
            visit = [[0] * m for _ in range(n)]
            matrix[i][j] = 0
            visit[i][j] = 1
            answer = max(answer, bfs(i, j))

print(answer)