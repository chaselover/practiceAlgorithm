import sys
input = sys.stdin.readline

dp = [[1 if j==0 else i if j==1 else 0 for i in range(2001)] for j in range(15)]
for i in range(2,15):
    for j in range(1,2001):
        dp[i][j] = dp[i-1][j//2] + dp[i][j-1]

for _ in range(int(input())):
    n,m = map(int,input().split())
    sys.stdout.write(str(dp[n][m]) +'\n')