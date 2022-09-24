import sys
from collections import deque
input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
# 3차원 배열로 3차원 배열에 뚫을 수 잇으면 1 없으면 0으로 부여. 뚫은 좌표 로 쭉쭉 BFS펼치다가 가장먼저 도착지에 도착한게 최솟값.
# 벽을 뚫을때마다 bfs돌리면 절대 못감.
def bfs():
    q = deque()
    q.append([0, 0, 1])
    visit = [[[0] * 2 for _ in range(m)] for i in range(n)]
    visit[0][0][1] = 1
    while q:
        a, b, w = q.popleft()
        if a == n - 1 and b == m - 1:
            return visit[a][b][w]
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < n and 0 <= y < m:
                # 벽이있고 뚫을 능력이 있을때.
                if s[x][y] == 1 and w == 1:
                    visit[x][y][0] = visit[a][b][1] + 1
                    q.append([x, y, 0])
                # 벽이 없고 가보지 않은 곳.
                elif s[x][y] == 0 and visit[x][y][w] == 0:
                    visit[x][y][w] = visit[a][b][w] + 1
                    q.append([x, y, w])
    return -1
n, m = map(int, input().split())
s = []
for i in range(n):
    s.append(list(map(int, list(input().strip()))))
print(bfs())