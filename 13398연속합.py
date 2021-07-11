n = int(input())
lst = list(map(int, input().split()))

dp = [[0, 0] for _ in range(n)]
dp[0] = [lst[0], -999999999]

for i in range(1, n):
    dp[i][0] = max(dp[i - 1][0] + lst[i], lst[i])
    dp[i][1] = max(dp[i - 1][0], dp[i - 1][1] + lst[i])

ans = -999999999
for i in range(n):
    ans = max(ans, max(dp[i]))
print(ans)
