import sys
input = sys.stdin.readline


MOD = 1000000009
# 숫자 n을 m개를 써서 만드는 경우의 수. n * n 까지 가능.
dp = [[0] * 1001 for _ in range(1001)]
dp[1][1] = 1

dp[2][1] = 1
dp[2][2] = 1

dp[3][1] = 1
dp[3][2] = 2
dp[3][3] = 1
for i in range(4, 1001):
    for j in range(1, i + 1):
        dp[i][j] = (dp[i - 1][j - 1] + dp[i - 2][j - 1] + dp[i - 3][j - 1]) % MOD


for _ in range(int(input())):
    n, m = map(int, input().split())

    print(sum(dp[n][:m + 1]) % MOD)