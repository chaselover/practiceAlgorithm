from collections import deque
import sys
input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
def bfs():
    while q:
        x, y, key, cnt = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and s[nx][ny] != "#" and not visit[nx][ny][key]:
                if s[nx][ny] == ".":
                    visit[nx][ny][key] = 1
                    q.append([nx, ny, key, cnt + 1])
                elif s[nx][ny] == "1":
                    return cnt + 1
                else:
                    if s[nx][ny].isupper():
                        if key & 1 << (ord(s[nx][ny]) - 65):
                            visit[nx][ny][key] = 1
                            q.append([nx, ny, key, cnt + 1])
                    elif s[nx][ny].islower():
                        nc = key | (1 << ord(s[nx][ny]) - 97)
                        if visit[nx][ny][nc] == 0:
                            visit[nx][ny][nc] = 1
                            q.append([nx, ny, nc, cnt + 1])
    return -1
n, m = map(int, input().split())
q = deque()
visit = [[[0] * 64 for i in range(m)] for i in range(n)]
s = list(list(input().rstrip()) for _ in range(n))
for i in range(n):
    for j in range(m):
        if s[i][j] == "0":
            q.append([i, j, 0, 0])
            s[i][j] = "."
            visit[i][j][0] = 1
print(bfs())