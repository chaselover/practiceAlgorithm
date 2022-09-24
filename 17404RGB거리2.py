import sys
input = sys.stdin.readline

# 삘 초 파로 칠하는 모든 경우의 수를 계산.
N = int(input())
price = [list(map(int,input().split())) for _ in range(N)]
dp = [[1001,1001,1001] for _ in range(N+1)]
ans = []

for init in range(3):
    dp[1][init] = price[0][init]
    dp[1][(init+1)%3] = 3001
    dp[1][(init+2)%3] = 3001

    for i in range(2,N+1):
        dp[i][0] = min(dp[i-1][1]+price[i-1][0],dp[i-1][2]+price[i-1][0])
        dp[i][1] = min(dp[i-1][0]+price[i-1][1],dp[i-1][2]+price[i-1][1])
        dp[i][2] = min(dp[i-1][0]+price[i-1][2],dp[i-1][1]+price[i-1][2])

    dp[N][init] = 1000001
    ans.append(min(dp[N]))

print(min(ans))