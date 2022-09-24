import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
dp = [[0] * 21 for _ in range(N)]
dp[0][arr[0]] = 1
for i in range(1, N - 1):
    for pre_value in range(21):
        if dp[i - 1][pre_value]:
            if 0 <= pre_value + arr[i] <= 20: 
                dp[i][pre_value + arr[i]] += dp[i - 1][pre_value]
            if 0 <= pre_value - arr[i] <= 20: 
                dp[i][pre_value - arr[i]] += dp[i - 1][pre_value]
print(dp[N - 2][arr[-1]])