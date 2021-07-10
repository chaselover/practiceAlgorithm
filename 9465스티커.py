import sys
input = sys.stdin.readline


for test in range(int(input())):
    n = int(input())
    value = [list(map(int,input().split())) for _ in range(2)]
    dp = [[0]*n for _ in range(2)]
    dp[0][0] = value[0][0]
    dp[1][0] = value[1][0]
    dp[0][1] = dp[1][0] + value[0][1]
    dp[1][1] = dp[0][0] + value[1][1]
    for j in range(n):
        for i in range(2):
            dp[i][j] = max(dp[(i+1)%2][j-2],dp[(i+1)%2][j-1])+value[i][j]
    print(max(dp[0] + dp[1]))