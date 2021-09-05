import sys
input = sys.stdin.readline
from collections import deque

def remove(x,y):
    q = deque()
    q.append([x,y])
    matrix[x][y] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<2001 and 0<=ny<2001 and matrix[nx][ny]:
                q.append([nx,ny])
                matrix[nx][ny] = 0


def paint(s_x,s_y,t_x,t_y):
    # 윗변, 아랫변
    for y in range(s_y,t_y+1):
        matrix[t_x][y] = 1
        matrix[s_x][y] = 1
    # 왼쪽, 오른쪽
    for x in range(s_x,t_x+1):
        matrix[x][s_y] = 1
        matrix[x][t_y] = 1


N = int(input())
matrix = [[0]*2001 for _ in range(2001)]
for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    paint(2*(x1+500),2*(y1+500),2*(x2+500),2*(y2+500))

dx = [0,1,0,-1]
dy = [-1,0,1,0]

answer = -1 if matrix[1000][1000] else 0
for i in range(2001):
    for j in range(2001):
        if matrix[i][j]==1:
            remove(i,j)
            answer += 1
print(answer)