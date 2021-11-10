from collections import deque

def bfs(y, x):
    q = deque()
    q.append((y, x))
    graph[y][x] = 0
    while q:
        y, x = q.popleft()
        for dy, dx in d:
            Y, X = y+dy, x+dx
            if 0 <= Y < N and 0 <= X < N and graph[Y][X] == -1:
                q.append((Y, X))
                graph[Y][X] = graph[y][x]+1

N, M = map(int, input().split())
graph = [[-1]*N for _ in range(N)]
sy, sx = map(int, input().split())
e_li = [list(map(int, input().split())) for _ in range(M)]    
d = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
bfs(sy-1, sx-1)
for y, x in e_li:
    print(graph[y-1][x-1], end=' ')
print()