import sys
input = sys.stdin.readline
from collections import deque


def BFS(x,y,h):
    global result
    queue = deque()
    queue.append([x,y])
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    out_rain = False
    cnt = 1
    visited[x][y] = True
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<R and 0<=ny<C:
                if not visited[nx][ny]:
                    if Rain[nx][ny]<=h:
                        queue.append([nx,ny])
                        cnt+=1
                        visited[nx][ny] = True
            else:
                out_rain = True
                return
    if not out_rain:
        result+=cnt
    return

result = 0
R,C = map(int,input().split())
Rain = [list(map(int,input().split())) for _ in range(R)]
for height in range(0,10000):
    visited = [[False]*C for _ in range(R)]
    for i in range(1,R-1):
        for j in range(1,C-1):
            if not visited[i][j] and Rain[i][j]<=height:
                BFS(i,j,height)
print(result)
