import sys
input = sys.stdin.readline

n = int(input())
dp = [[0]*(n+1) for _ in range(n+1)]
dp[2][1] = 2
for i in range(3,n+1):
    for j in range(1,i):
        dp[i][j] = (dp[i-1][j]*2 + dp[i-1][j-1] + dp[i-1][j+1])%10007
sum_n = 0
for i in range(1,n):
    sum_n += dp[n][i]
print(sum_n%10007)