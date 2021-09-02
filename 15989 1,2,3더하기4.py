import sys
input = sys.stdin.readline

T = int(input())
dp = [0]*10001
dp[0] = 1
dp[1] = 1
dp[2] = 2
dp[3] = 3
for i in range(4,10001):
    dp[i] = dp[i-1] + dp[i-2] - dp[i-3]
    if not i % 3:
        dp[i] += 1
for _ in range(T):
    print(dp[int(input())])