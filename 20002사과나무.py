import sys
input = sys.stdin.readline

N = int(input())
maps = [list(map(int,input().split())) for _ in range(N)]
dp = [[0]*(N+1) for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,N+1):
        dp[i][j] = dp[i-1][j]+dp[i][j-1]-dp[i-1][j-1]+maps[i-1][j-1]

max_profit=dp[1][1]
for k in range(N):
    for i in range(1,N-k+1):
        for j in range(1,N-k+1):
            cur_profit = dp[i+k][j+k]-dp[i-1][j+k]-dp[i+k][j-1]+dp[i-1][j-1]
            if max_profit < cur_profit:
                max_profit=cur_profit

print(max_profit)



