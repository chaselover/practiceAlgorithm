import sys
input = sys.stdin.readline

N,M = map(int,input().split())

matrix = [list(map(int,input().split())) for _ in range(N)]
dp = [[0]*N for _ in range(N)]




for i in range(N):
    for j in range(N):
        dp[0][0] = matrix[0][0]
        if i==0 and j>0:
            dp[i][j] = dp[i][j-1]+matrix[i][j]
        elif j==0 and i>0:
            dp[i][j] = dp[i-1][j]+matrix[i][j]
        else:
            dp[i][j] = dp[i-1][j]+dp[i][j-1] + matrix[i][j] - dp[i-1][j-1]


for _ in range(M):
    x1,y1,x2,y2 = map(int,input().split())
    if x1==1 and y1 !=1:
        answer = dp[x2-1][y2-1] - dp[x2-1][y1-2]
    elif y1==1 and x1 !=1:
        answer = dp[x2-1][y2-1] - dp[x1-2][y2-1]
    elif x1==1 and x1==1:
        answer = dp[x2-1][y2-1]
    else:
        answer = dp[x2-1][y2-1] - dp[x2-1][y1-2] - dp[x1-2][y2-1] + dp[x1-2][y1-2]
    print(answer)