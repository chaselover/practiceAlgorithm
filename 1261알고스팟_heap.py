from heapq import heappush, heappop

m, n = map(int, input().split())
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
s = []
visit = [[0] * m for i in range(n)]
for i in range(n):
    s.append(list(map(int, input())))
def bfs():
    heap = []
    heappush(heap, [0, 0, 0])
    visit[0][0] = 1
    while heap:
        c, a, b = heappop(heap)
        if a == n - 1 and b == m - 1:
            print(c)
            return
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < n and 0 <= y < m and visit[x][y] == 0:
                heappush(heap, [c + 1 if s[x][y] == 1 else c, x, y])
                visit[x][y] = 1
bfs()