import sys
input = sys.stdin.readline
sys.setrecursionlimit(50000)
from collections import deque

N,M = map(int,input().split())

matrix = [list(map(lambda x :int(x),list(map(str,input().rstrip())))) for _ in range(N)]
queue = deque()
dx = [-1,1,0,0]
dy = [0,0,1,-1]

def BFS(x,y):
    queue.append([x,y])
    matrix[x][y] = 1
    while queue:
        x,y = queue.popleft()
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            if 0<=nx<N and 0<=ny<M and matrix[nx][ny]==1:
                matrix[nx][ny] =matrix[x][y]+1
                queue.append([nx,ny])
BFS(0,0)
print(matrix[N-1][M-1])
