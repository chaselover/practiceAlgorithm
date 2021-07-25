from collections import deque


def solution(maps):
    return bfs(maps)


def bfs(maps):
    dy, dx = [1,-1,0,0], [0,0,1,-1]
    dist = [[-1] * len(maps[0]) for _ in range(len(maps))] 
    dist[0][0] = 1
    q = deque([(0, 0)])
    while q:
        cy, cx = q.popleft()
        for d in range(4):
            ny, nx = cy + dy[d], cx + dx[d]
            if 0 <= ny < len(maps) and 0 <= nx < len(maps[0]):
                if dist[ny][nx] == -1 and maps[ny][nx] == 1:
                    dist[ny][nx] = dist[cy][cx] + 1
                    q.append((ny, nx))
    return dist[-1][-1]