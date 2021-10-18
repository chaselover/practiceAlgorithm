import sys
input = sys.stdin.readline


def dfs(x, y):

    # 아래 끝까지 내려 온 경우 0을 반환
    if x == n:
        return 0

    # 오른쪽 끝까지 이동한 경우 아래로 한 칸 내려가기
    if y == m:
        return dfs(x + 1, 0)
    result = 0

    # (x, y)를 기준으로 1번째 모양
    if x + 1 < n and y + 1 < m and v[x][y] + v[x][y + 1] + v[x + 1][y + 1] == 0:
        v[x][y] = v[x][y + 1] = v[x + 1][y + 1] = True
        result = max(result, dfs(x, y + 1) +
                     (board[x][y] + 2 * board[x][y + 1] + board[x + 1][y + 1]))
        v[x][y] = v[x][y + 1] = v[x + 1][y + 1] = False

    # (x, y)를 기준으로 2번째 모양
    if x + 1 < n and y + 1 < m and v[x][y + 1] + v[x + 1][y] + v[x + 1][y + 1] == 0:
        v[x][y + 1] = v[x + 1][y] = v[x + 1][y + 1] = True
        result = max(result, dfs(
            x, y + 1) + (board[x][y + 1] + board[x + 1][y] + 2 * board[x + 1][y + 1]))
        v[x][y + 1] = v[x + 1][y] = v[x + 1][y + 1] = False

    # (x, y)를 기준으로 3번째 모양
    if x + 1 < n and y + 1 < m and v[x][y] + v[x + 1][y] + v[x + 1][y + 1] == 0:
        v[x][y] = v[x + 1][y] = v[x + 1][y + 1] = True
        result = max(result, dfs(x, y + 1) +
                     (board[x][y] + 2 * board[x + 1][y] + board[x + 1][y + 1]))
        v[x][y] = v[x + 1][y] = v[x + 1][y + 1] = False

    # (x, y)를 기준으로 4번째 모양
    if x + 1 < n and y + 1 < m and v[x][y] + v[x][y + 1] + v[x + 1][y] == 0:
        v[x][y] = v[x][y + 1] = v[x + 1][y] = True
        result = max(result, dfs(x, y + 1) +
                     (2 * board[x][y] + board[x][y + 1] + board[x + 1][y]))
        v[x][y] = v[x][y + 1] = v[x + 1][y] = False

    # 현재 위치를 기준으로 부메랑을 만들지 않는 경우
    result = max(result, dfs(x, y + 1))
    return result


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
v = [[False] * m for _ in range(n)]

print(dfs(0, 0))



# 2
N, M = map(int, input().strip().split())
board = [list(map(int, input().strip().split())) for _ in range(N)]
used = [[0 for _ in range(M)] for _ in range(N)]
dy = [[0, 1], [0, -1], [-1, 0], [0, 1]]
dx = [[-1, 0], [-1, 0], [0, 1], [1, 0]]
answer = 0


def traverse(power, cy, cx):
    global answer

    for y in range(cy, N):
        for x in range(cx if y == cy else 0, M):
            if used[y][x] == 1:
                continue
            for i in range(4):
                flag = True
                for j in range(2):
                    ny, nx = y + dy[i][j], x + dx[i][j]

                    if 0 > ny or ny >= N or nx < 0 or nx >= M or used[ny][nx] == 1:
                        flag = False
                        break
                if flag is True:
                    total = 0
                    used[y][x] = 1
                    for j in range(2):
                        ny, nx = y + dy[i][j], x + dx[i][j]
                        used[ny][nx] = 1
                        total += board[ny][nx]
                    traverse(power + total + board[y][x] * 2, y if x + 1 < M else y + 1, x + 1 if x + 1 < M else 0)
                    for j in range(2):
                        ny, nx = y + dy[i][j], x + dx[i][j]
                        used[ny][nx] = 0
                    used[y][x] = 0
    answer = max(answer, power)

traverse(0, 0, 0)
print(answer)



# 3
import sys, copy

input = sys.stdin.readline


def dfs(dx, dy, sum_pre):
    global max_value
    if dy >= M - 1:
        dx += 1
        dy = 0
    if dx >= N - 1:
        max_value = max(max_value, sum_pre)
        return

    for Next in [s0, s1, s2, s3, s4]:
        if Next == 0:
            dfs(dx, dy + 1, sum_pre)
        else:
            flag = True
            total_sum = 0
            for k in range(2):
                for l in range(2):
                    if Next[k][l] != 0:
                        if flag and Next[k][l] * dp[dx + k][dy + l] != 0:
                            total_sum += Next[k][l] * dp[dx + k][dy + l]
                        else:
                            flag = False
                            total_sum = 0
            if flag:
                for k in range(2):
                    for l in range(2):
                        if Next[k][l] != 0:
                            dp[dx + k][dy + l] = 0
                dfs(dx, dy + 1, sum_pre + total_sum)
                for k in range(2):
                    for l in range(2):
                        if Next[k][l] != 0:
                            dp[dx + k][dy + l] = board[dx + k][dy + l]


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

s0 = 0
s1 = [[1, 2], [0, 1]]
s2 = [[0, 1], [1, 2]]
s3 = [[1, 0], [2, 1]]
s4 = [[2, 1], [1, 0]]

max_value = 0
dp = [row[:] for row in board]
dfs(0, 0, 0)

print(max_value)