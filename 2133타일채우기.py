import sys
input = sys.stdin.readline

N = int(input())
dp = [0]*31

dp[2] = 3
for i in range(4,N+1,2):
    dp[i] = dp[i-2]*3+2
    for j in range(4,i,2):
         dp[i] += dp[i-j]*2

print(dp[N])
