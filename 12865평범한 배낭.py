import sys
input = sys.stdin.readline

N, K = map(int, input().split())
wei_cost = [[0,0]]
dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

for _ in range(N):
    wei_cost.append(list(map(int, input().split())))


for i in range(1, N + 1):
    for j in range(1, K + 1):
        weight = wei_cost[i][0] 
        cost = wei_cost[i][1]
        if j < weight:
            dp[i][j] = dp[i - 1][j] 
        else:
            dp[i][j] = max(cost + dp[i - 1][j - weight], dp[i - 1][j])

print(dp[N][K])
