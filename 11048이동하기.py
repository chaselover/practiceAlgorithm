import sys
input = sys.stdin.readline
from collections import deque

def BFS(i,j):
    candy_max = 0
    queue = deque()
    queue.append([i,j])
    visited_candy = [[-1 for _ in range(M)] for _ in range(N)]
    visited_candy[i][j] = maze[i][j]
    while queue:
        x,y = queue.popleft()
        if x==N-1 and y==M-1:
            if visited_candy[x][y] > candy_max:
                candy_max = visited_candy[x][y]
        for nx,ny in [(x+1,y),(x,y+1),(x+1,y+1)]:
            if 0<=nx<N and 0<=ny<M and visited_candy[x][y] + maze[nx][ny] > visited_candy[nx][ny]:
                visited_candy[nx][ny] = visited_candy[x][y] + maze[nx][ny]
                queue.append([nx,ny])
    else:
        return candy_max
        
N,M = map(int,input().split())
maze = [list(map(int,input().split())) for _ in range(N)]

print(BFS(0,0))
