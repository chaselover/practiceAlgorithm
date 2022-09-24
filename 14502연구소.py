import sys
input = sys.stdin.readline


def BFS():
    global max_result
    copy = [[0] * m for i in range(n)]
    for i in range(n):
        for j in range(m):
            copy[i][j] = s[i][j]
    result = 0
    arr = []
    for i in range(n):
        for j in range(m):
            if copy[i][j] == 2:
                arr.append([i, j])
    while arr:
        a, b = arr[0][0], arr[0][1]
        del arr[0]
        for i in range(4):
            ax = a + dx[i]
            ay = b + dy[i]
            if 0 <= ax and 0 <= ay and ax < n and ay < m:
                if copy[ax][ay] == 0:
                    copy[ax][ay] = 2
                    arr.append([ax, ay])
    for i in copy:
        for j in i:
            if j == 0:
                result += 1
    max_result = max(max_result, result)
# 벽 3개를 세우는 조합.
def DFS(cnt):
    if cnt == 3:
        BFS()
        return
    for i in range(n):
        for j in range(m):
            if s[i][j] == 0:
                s[i][j] = 1
                DFS(cnt + 1)
                s[i][j] = 0
n, m = map(int, input().split())
s = []
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
max_result = 0
for i in range(n):
    s.append(list(map(int, input().split())))

DFS(0)
print(max_result)