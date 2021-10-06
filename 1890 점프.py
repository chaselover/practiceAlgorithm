import sys
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]
dp[0][0] = 1

for row in range(N):
    for col in range(N):
        if not board[row][col]:
            continue
        jump = board[row][col]
        if col + jump < N:
            dp[row][col + jump] += dp[row][col]
        if row + jump < N:
            dp[row + jump][col] += dp[row][col]
print(dp[N - 1][N - 1])