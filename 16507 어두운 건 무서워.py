#어두운건 무서워
import sys
R,C,Q = map(int,sys.stdin.readline().split())
A = [list(map(int,sys.stdin.readline().split())) for _ in range(R)]
dp = [[0 for _ in range(C+1)] for _ in range(R+1)]

for i in range(1,R+1):
    for j in range(1,C+1):
        dp[i][j] = -dp[i-1][j-1]+dp[i-1][j]+dp[i][j-1]+A[i-1][j-1]
# print(dp)

for i in range(Q):
    R1,C1, R2,C2 =  map(int,sys.stdin.readline().split())
    ans = dp[R2][C2] - dp[R1-1][C2] - dp[R2][C1-1] + dp[R1-1][C1-1]
    num = ((R2-R1)+1)*((C2-C1)+1) 
    print(ans//num)
