import sys
input = sys.stdin.readline
from collections import deque

dx=[0,1,0,-1]
dy=[1,0,-1,0]

N = int(input())
K = int(input())
snake=deque()
board = [[0 for _ in range(N)] for _ in range(N)]
for _ in range(K):
    a,b = map(int,input().split())
    board[a-1][b-1]=1
L = int(input())
# 최초 뱀 0,0 방향 오른쪽
snake.append([0,0])
dir=0
board[0][0]=2
t=0
commands=[]
for _ in range(L):
    commands.append(input().split())

for command in commands:
    c_time,direct = command
    last_time=t
    c_time=int(c_time)
    for _ in range(c_time-last_time):
        x,y=snake[0]
        nx=x+dx[dir]
        ny=y+dy[dir]
        if 0<=nx<N and 0<=ny<N and not board[nx][ny]==2:
            if board[nx][ny]==1:             # 사과일때
                board[nx][ny]=2
                snake.appendleft([nx,ny])
            else:
                board[nx][ny]=2              # 사과아닐때
                snake.appendleft([nx,ny])
                d_x,d_y = snake.pop()
                board[d_x][d_y]=0
        else:                                # 벽밖이거나 자기몸일때
            print(t+1)
            exit()
        t+=1
    if direct=='L':
        dir = (dir-1)%4
    else:
        dir = (dir+1)%4

while 1:
    x,y=snake[0]
    nx=x+dx[dir]
    ny=y+dy[dir]
    if 0<=nx<N and 0<=ny<N and not board[nx][ny]==2:
        if board[nx][ny]==1:             # 사과일때
            board[nx][ny]=2
            snake.appendleft([nx,ny])
        else:                            # 사과아닐때
            snake.appendleft([nx,ny])
            d_x,d_y = snake.pop()
            board[d_x][d_y]=0
    else:                                # 벽밖이거나 자기몸일때
        print(t+1)
        exit()
    t+=1