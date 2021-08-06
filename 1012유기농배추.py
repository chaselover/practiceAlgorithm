import sys
input = sys.stdin.readline
from collections import deque

dx=[0,1,0,-1]
dy=[1,0,-1,0]

def BFS(x,y):
    queue=deque()
    queue.append([x,y])
    radish[x][y]=0
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<N and 0<=ny<M and radish[nx][ny]:
                radish[nx][ny]=0
                queue.append([nx,ny])

for test in range(1,int(input())+1):
    M,N,K = map(int,input().split())
    radish = [[0 for _ in range(M)] for _ in range(N)]
    for _ in range(K):
        x,y=map(int,input().split())
        radish[y][x]=1
    cnt=0
    for i in range(N):
        for j in range(M):
            if radish[i][j]==1:
                BFS(i,j)
                cnt+=1
    print(cnt)