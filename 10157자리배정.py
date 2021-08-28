import sys
input = sys.stdin.readline

C, R = map(int, input().split())
K = int(input())
movie = [[0 for _ in range(R)] for _ in range(C)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

queue = []
dir = 0
queue.append([0,0])
movie[0][0] = 1
while queue:
    x,y = queue.pop()
    if movie[x][y] == K:
        print(x+1,y+1)
        exit()
    nx = x + dx[dir]
    ny = y + dy[dir]
    if 0 <= nx < C and 0 <= ny < R and not movie[nx][ny]:
        movie[nx][ny] = movie[x][y] + 1
        queue.append([nx,ny])
        continue
    else:
        dir = (dir+1)%4
        nx = x + dx[dir]
        ny = y + dy[dir]
        if 0 <= nx < C and 0 <= ny < R and not movie[nx][ny]:
            movie[nx][ny] = movie[x][y] + 1
            queue.append([nx,ny])
            continue
print(0)