import sys
input = sys.stdin.readline
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1
    
    while queue:
        x, y = queue.popleft()
        temp = 0
    
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
    
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if arr[nx][ny] != 0:
                    queue.append((nx, ny))
                    visited[nx][ny] = 1
                else:
                    temp += 1
    
        new_arr[x][y] -= temp
        new_arr[x][y] = max(0, new_arr[x][y])
    return


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
time = 0

while True:
    visited = [[0 for _ in range(m)] for _ in range(n)]
    new_arr = [row[:] for row in arr]
    cnt = 0

    for i in range(n):
        for j in range(m):
            if arr[i][j] != 0 and not visited[i][j]:
                bfs(i, j)
                cnt += 1
    if cnt >= 2:
        break
    elif cnt == 0:
        time = 0
        break
    
    arr = new_arr
    time += 1

print(time)