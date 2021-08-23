import sys
input = sys.stdin.readline
from collections import deque

def BFS(start_x,start_y,start_time):
    queue = deque()
    queue.append((start_x,start_y,start_time))
    while queue:
        x, y, turn = queue.popleft()
        for dx,dy in move:
            nx = x + dx
            ny = y + dy
            if 0<=nx<8 and 0<=ny<8 and not maze[nx-turn][ny]=='#' and not maze[nx-turn-1][ny]=='#':
                if nx-turn < 0:
                    return 1
                queue.append([nx,ny,turn+1])
    return 0


maze=[list(input().rstrip()) for _ in range(8)]
move = [[0,0],[0,-1],[0,1],[-1,0],[1,0],[-1,-1],[1,-1],[1,1],[-1,1]]
print(BFS(7,0,0))

