from collections import deque

def bfs(y, x):
    q = deque()
    q.append((y, x))
    graph[y][x] = 0
    while q:
        y, x = q.popleft()
        for dy, dx in d:
            Y, X = y+dy, x+dx
            if (0 <= Y < N) and (0 <= X < N) and graph[Y][X] == -1:
                q.append((Y, X))
                graph[Y][X] = graph[y][x]+1

N = int(input())
sr, sc, er, ec = map(int, input().split())
graph = [[-1]*(N) for _ in range(N)]
d = [(-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1)]
bfs(sr, sc)
print(graph[er][ec])