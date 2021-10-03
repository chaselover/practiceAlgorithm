import sys
input = sys.stdin.readline
from heapq import heappush, heappop


def dijkstra():
    heap = []
    heappush(heap, [0, 0, 0])
    visited[0][0] = 1
    while heap:
        cost, x, y = heappop(heap)
        if x == n - 1 and y == n - 1:
            return cost
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                visited[nx][ny] = True
                if maze[nx][ny] == 0:
                    heappush(heap, [cost + 1, nx, ny])
                else:
                    heappush(heap, [cost, nx, ny])


n = int(input())
maze = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

print(dijkstra())
