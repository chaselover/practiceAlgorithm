import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dp = [[float('inf')] * (int((2 * N)** 0.5) + 2) for _ in range(N + 1)] 
dp[1][0] = 0
stones = set([int(input()) for _ in range(M)])
for i in range(2, N + 1):
    if i in stones: continue
    for j in range(1, int((2 * i) ** 0.5) + 1):
        dp[i][j] = min(dp[i - j][j - 1], dp[i - j][j], dp[i - j][j + 1]) + 1

answer = min(dp[N])
print(answer if answer != float('inf') else -1)