import sys
input = sys.stdin.readline

N, K = map(int, input().split())
dp = [[0]*5001 for _ in range(5001)]
# 결국 숫자1 N개를 K개의 칸에 분배하는 경우의 수.
# N-1개를 K개에 분배하는 경우의수에 1씩 더하는 경우 + N개를 K-1개에 분배하는 경우의수에서 0을 가지는 한칸을 더하는경우,
for i in range(1,N+1):
    for j in range(1,K+1):
        if i==1:
            dp[i][j] = j
        else:
            dp[i][j] = (dp[i-1][j] + dp[i][j-1])%1000000000
print(dp[N][K])
