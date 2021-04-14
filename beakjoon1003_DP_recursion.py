import sys

T = int(sys.stdin.readline())

for test in range(1,T+1):
    n = int(sys.stdin.readline())
    dp = []

    dp.append([1,0])
    dp.append([0,1])

    for i in range(2, n+1):
        dp_x = dp[i-1][0]+dp[i-2][0]
        dp_y = dp[i-1][1]+dp[i-2][1]
        dp.append([dp_x,dp_y])
    print(f'{dp[n][0]} {dp[n][1]}')



