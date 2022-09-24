import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
matrix = [list(map(int,list(map(str,input().rstrip())))) for _ in range(N)]
queue = deque()
cnt = 1
dx = [1,-1,0,0]
dy = [0,0,1,-1]
ans = []

def BFS(x,y,cnt):
    matrix[x][y] = cnt
    count = 1
    queue.append([x,y])
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<N and 0<=ny<N and matrix[nx][ny]==1:
                matrix[nx][ny] = cnt
                queue.append([nx,ny])
                count +=1
    ans.append(count)


for i in range(N):
    for j in range(N):
        if matrix[i][j]==1:
            cnt +=1
            BFS(i,j,cnt)
            

print(cnt-1)
ans.sort()
for i in range(cnt-1):
    print(ans[i])