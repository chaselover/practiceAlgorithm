import sys
input = sys.stdin.readline
from collections import deque

def bfs(x,y):
    queue = deque()
    queue.append([x,y,0])
    visited = [[[0]*(K+1) for _ in range(M)] for _ in range(N)]
    visited[x][y][0] = 1
    while queue:
        x,y,b_cnt = queue.popleft()
        if x==N-1 and y==M-1:
            return visited[x][y][b_cnt]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<M:
                if not visited[nx][ny][b_cnt]:
                    if maps[nx][ny] and b_cnt < K:
                        visited[nx][ny][b_cnt+1] = visited[x][y][b_cnt]+1
                        queue.append([nx,ny,b_cnt+1])
                    elif not maps[nx][ny]:
                        visited[nx][ny][b_cnt] = visited[x][y][b_cnt]+1
                        queue.append([nx,ny,b_cnt])

    return -1

N, M, K = map(int, input().split())
maps = [list(map(int, list(input().rstrip()))) for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
print(bfs(0,0))