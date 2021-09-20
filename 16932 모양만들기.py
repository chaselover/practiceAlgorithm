from sys import stdin
from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

n,m = map(int, stdin.readline().strip().split())

board = [list(map(int, stdin.readline().strip().split())) for _ in range(n)]
candidate = []
area_size = [0,0]

def solve():
    num = 2
    for x in range(n):
        for y in range(m):
            if board[x][y] == 0:
                candidate.append((x,y))
            elif board[x][y] == 1:
                insert_num(x,y,num)
                num+=1

    ans = -1
    for x,y in candidate:
        visited = set()
        cnt = 1
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if not point_validator(nx, ny) or board[nx][ny] == 0:
                continue
            num = board[nx][ny]

            if num in visited:
                continue
            visited.add(num)
            cnt += area_size[num]
        ans = max(ans, cnt)
    print(ans)
def insert_num(sx,sy,num):
    global board, area_size
    q = deque()

    q.appendleft((sx,sy))
    board[sx][sy] = num
    size = 1

    while q:
        x,y = q.pop()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if not point_validator(nx,ny) or board[nx][ny] != 1:
                continue

            board[nx][ny] = num
            size += 1
            q.appendleft((nx,ny))

    area_size.append(size)
def point_validator(x,y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    return True

solve()