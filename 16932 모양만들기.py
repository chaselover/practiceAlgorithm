import sys
input = sys.stdin.readline
from collections import deque

def bfs(x,y):
    q = deque()
    visited[x][y] = True
    q.append((x,y))
    cnt = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and matrix[nx][ny]:
                visited[nx][ny] = True
                q.append((nx,ny))
                cnt += 1
    return cnt

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

dx = [0,0,-1,1]
dy = [1,-1,0,0]

max_ans = 0
for i in range(N):
    for j in range(M):
        if not matrix[i][j]:
            visited = [[False]*M for _ in range(N)]
            matrix[i][j] = 1
            max_ans = max(max_ans,bfs(i,j))
            matrix[i][j] = 0
print(max_ans)