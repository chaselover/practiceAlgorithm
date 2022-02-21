import sys
input = sys.stdin.readline
from collections import deque

def rotate(i, d):
    new_board = []
    if d:
        for n in range(k, M):
            new_board.append(round_boards[i][n])
        for n in range(k):
            new_board.append(round_boards[i][n])
    else:
        for n in range(M - k, M):
            new_board.append(round_boards[i][n])
        for n in range(M - k):
            new_board.append(round_boards[i][n])
    round_boards[i] = new_board


def bfs(x, y):
    q = deque()
    q.append((x, y))
    check_list[x][y] = True
    pivot = round_boards[x][y]
    flag = 0
    while q:
        x, y = q.popleft()
        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            if ny == -1:
                ny = M - 1
            elif ny == M:
                ny = 0
            if 0 <= nx < N and not check_list[nx][ny] and pivot == round_boards[nx][ny]:
                check_list[nx][ny] = True
                round_boards[x][y] = 0
                round_boards[nx][ny] = 0
                q.append((nx, ny))
                flag = 1
    if flag:
        return 1
    return 0
                


N, M, T = map(int, input().split())
round_boards = [list(map(int, input().split())) for _ in range(N)]

delta = ((0, 1), (1, 0), (0, -1), (-1, 0))

for _ in range(T):
    x, d, k = map(int, input().split())
    k %= M
    if k:
        for i in range(x - 1, N, x):
            rotate(i, d)
    check_list = [[False] * M for _ in range(N)]
    change_zero = 0
    for i in range(N):
        for j in range(M):
            if round_boards[i][j]:
                change_zero += bfs(i, j)
    if not change_zero:
        points = []
        sum_all = 0
        cnt = 0
        for i in range(N):
            for j in range(M):
                if round_boards[i][j]:
                    points.append((i, j))
                    cnt += 1
                    sum_all += round_boards[i][j]
        if cnt:
            avg = sum_all / cnt
            for x, y in points:
                if round_boards[x][y] > avg:
                    round_boards[x][y] -= 1
                elif round_boards[x][y] < avg:
                    round_boards[x][y] += 1
answer = 0
for i in range(N):
    for j in range(M):
        answer += round_boards[i][j]
print(answer)
    