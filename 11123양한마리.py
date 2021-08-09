import sys
input = sys.stdin.readline
from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def BFS(i,j):
    queue = deque()
    queue.append([i,j])
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<H and 0<=ny<W and maps[nx][ny]:
                maps[nx][ny] = 0
                queue.append([nx,ny])

for test in range(1,int(input())+1):
    H,W = map(int,input().split())
    maps = []
    for _ in range(H):
        row = input().rstrip()
        rows=[]
        for yang in row:
            if yang == '#':
                rows.append(1)
            else:
                rows.append(0)
        maps.append(rows)
    cnt=0
    for i in range(H):
        for j in range(W):
            if maps[i][j]:
                maps[i][j]=0
                BFS(i,j)
                cnt+=1
    print(cnt)