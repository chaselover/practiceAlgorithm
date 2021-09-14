import sys
input = sys.stdin.readline
from collections import deque


def rotate_each(x,y,d,m):
    q = deque()
    for i in range(y-d,y+d+1):
        q.append(m[x-d][i])
    for i in range(x-d+1,x+d+1):
        q.append(m[i][y+d])
    for i in range(y+d-1,y-d-1,-1):
        q.append(m[x+d][i])
    for i in range(x+d-1,x-d,-1):
        q.append(m[i][y-d])    
    q.rotate(1)
    for i in range(y-d,y+d+1):
        m[x-d][i] = q.popleft()
    for i in range(x-d+1,x+d+1):
        m[i][y+d] = q.popleft()
    for i in range(y+d-1,y-d-1,-1):
        m[x+d][i] = q.popleft()
    for i in range(x+d-1,x-d,-1):
        m[i][y-d] = q.popleft()
    return m


def rotate_matrix(command_set):
    global min_value
    new_matrix = [row[:] for row in matrix]
    for command in command_set:
        r, c, s = command
        for i in range(1,s+1):
            new_matrix = rotate_each(r-1,c-1,i,new_matrix)
    for row in new_matrix:
        min_value = min(min_value,sum(row))


def dfs(arr):
    if len(arr) == K:
        rotate_matrix(arr)
    for i in range(K):
        if not visited[i]:
            visited[i] = True
            dfs(arr + [rotate_data[i]])
            visited[i] = False


N, M, K = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
visited = {i: False for i in range(K)}
rotate_data = []
min_value = float('inf')
for _ in range(K):
    r, c, s = map(int, input().split())
    rotate_data.append((r,c,s))
for i in range(K):
    visited[i] = True
    dfs([rotate_data[i]])
    visited[i] = False
print(min_value)