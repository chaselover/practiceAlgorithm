import sys
input = sys.stdin.readline

N = int(input())
house = [list(map(int, input().split())) for _ in range(N)]
# 오른쪽에서 오거나 왼쪽에서 오거나 대각선으로 오는 경우의 dp
dp = [[[0,0,0] for _ in range(N)] for _ in range(N)]
for i in range(N):
    if house[0][i]:
        break
    dp[0][i][0] = 1
for i in range(1,N):
    for j in range(2,N):
        if not house[i][j]:
            dp[i][j][0] = dp[i][j-1][0] + dp[i][j-1][1]
            if not house[i-1][j] and not house[i][j-1]:
                dp[i][j][1] = sum(dp[i-1][j-1])
            dp[i][j][2] = dp[i-1][j][1] + dp[i-1][j][2]
print(sum(dp[N-1][N-1]))
