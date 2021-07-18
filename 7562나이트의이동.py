import sys
input = sys.stdin.readline
from collections import deque

T = int(input())

dx = [1,2,1,2,-1,-2,-1,-2]
dy = [-2,-1,2,1,2,1,-2,-1]
queue = deque()

def BFS(x,y):
    queue.append([x,y])
    while queue:
        x,y = queue.popleft()
        for i in range(8):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<l and 0<=ny<l and matrix[nx][ny] == 0:
                queue.append([nx,ny])
                matrix[nx][ny] = matrix[x][y]+1



for test in range(T):
    l = int(input())
    matrix=[[0]*l for _ in range(l)]
    x,y = map(int,input().split())
    ans_x,ans_y = map(int,input().split())
    if x==ans_x and y==ans_y:
        print(0)
    else:
        BFS(x,y)
        print(matrix[ans_x][ans_y])