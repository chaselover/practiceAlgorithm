
from sys import stdin
from heapq import heappush, heappop
input = stdin.readline


def out(x, y):
    return x < 0 or x >= n or y < 0 or y >= m

def dijkstra():
    while q:
        d, x, y = heappop(q)
        if b[x][y] == 'F':
            print(dist[x][y]//G, dist[x][y]%G)
            return
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if out(nx, ny):
                continue
            nd = d+a[nx][ny]
            if dist[nx][ny] > nd:
                dist[nx][ny] = nd
                heappush(q, (nd, nx, ny))


n, m = map(int, input().split())
b = [list(input().strip()) for _ in range(n)]
a = [[0]*m for _ in range(n)]
dist = [[1e9]*m for _ in range(n)]
dx, dy, G = (-1, 0, 1, 0), (0, 1, 0, -1), 2500
q = []


for i in range(n):
    for j in range(m):
        if b[i][j] == 'S':
            heappush(q, (0, i, j))
            dist[i][j] = 0
        elif b[i][j] == 'g':
            a[i][j] = G
            for k in range(4):
                ni, nj = i+dx[k], j+dy[k]
                if not out(ni, nj) and b[ni][nj] == '.':
                    a[ni][nj] = 1
dijkstra()