import sys
input = sys.stdin.readline
from collections import deque

def move(x,y):
    q = deque()
    q.append([x,y,0])
    visited[x][y] = True
    while q:
        x,y,cnt = q.popleft()
        if x==Fr-1 and y==Fc-1:
            return cnt
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx and nx+H-1<N and 0<=ny and ny+W-1<M and not visited[nx][ny] and check(nx,ny):
                q.append([nx,ny,cnt+1])
    return -1


def check(x,y):
    visited[x][y] = True
    for i in range(x,x+H):
        for j in range(y,y+W):
            if board[i][j]:
                return False
    return True


N , M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
H, W, Sr, Sc, Fr, Fc = map(int, input().split())
visited = [[0]*M for _ in range(N)]

dx = [0,0,-1,1]
dy = [1,-1,0,0]

print(move(Sr-1,Sc-1))