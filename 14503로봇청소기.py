import sys
input =sys.stdin.readline
from collections import deque

def BFS(r,c,d):
    queue =deque()
    queue.append([r,c,d])
    cnt=1 # 현재 위치를 청소한다.
    areas[r][c]=2
    while queue:
        x,y,dir = queue.popleft()
        for n_dir in ((dir-1)%4,(dir-2)%4,(dir-3)%4,dir): #  현재위치에서 왼쪽부터 차례대로 인접한 칸을 탐색한다.
            nx=x+dx[n_dir]                                #  왼쪽에 청소할공간 없다면 다시 회전
            ny=y+dy[n_dir]
            if not areas[nx][ny]: # 청소 안했으면 그 방향으로 회전한다음 한칸 전진하고 1번.
                areas[nx][ny]=2
                cnt+=1
                queue.append([nx,ny,n_dir])
                break
        else:                   # 네방향 아무데도 진입 못한경우.
            nx=x-dx[dir]
            ny=y-dy[dir]
            if areas[nx][ny]==1:# 뒤쪽 벽. 작동 정지.
                print(cnt)
                return
            else:               # 벽 아니면 후진
                queue.append([nx,ny,dir])

dx=[-1,0,1,0]
dy=[0,1,0,-1]

N,M = map(int,input().split())
r,c,d = map(int,input().split())
areas = [list(map(int,input().split())) for _ in range(N)]

BFS(r,c,d)

