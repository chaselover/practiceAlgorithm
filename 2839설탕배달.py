N = int(input())
dp = [float('inf')]* 5001

dp[3] = 1
dp[5] = 1
for i in range(6,N+1):
    dp[i] = min(dp[i],dp[i-3]+1,dp[i-5]+1)

print(dp[N] if dp[N] != float('inf') else -1)