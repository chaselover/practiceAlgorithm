import sys
input = sys.stdin.readline
from collections import deque

def bfs(i,j):
    q = deque()
    q.append((i,j))
    visited[i][j] = 1
    while q:
        x, y = q.popleft()
        for d in delta:
            nx, ny = x + d[0], y + d[1]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and not island[nx][ny]=='1':
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx,ny))
                if island[nx][ny] in goal:
                    print('TAK')
                    print(visited[x][y])
                    exit()
    print('NIE')
    exit()


n, m = map(int, input().split())
island = [list(input().rstrip()) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
delta = ((1,0),(0,1),(-1,0),(0,-1))
goal = {'3', '4', '5'}
for i in range(n):
    for j in range(m):
        if island[i][j]=='2':
            bfs(i,j)
            