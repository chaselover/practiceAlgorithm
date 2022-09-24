import sys

T = int(sys.stdin.readline())
dp = [0 for _ in range(11)]
for i in range(4,11):
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
for test in range(T):
    N = int(sys.stdin.readline())

    print(dp[N])





