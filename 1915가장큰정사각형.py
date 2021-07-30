import sys
input = sys.stdin.readline

N,M = map(int,input().split())
square = [list(map(int,list(input().rstrip()))) for _ in range(N)]
dp = [[0]*(M+1) for _ in range(N+1)]
# 위 왼 대각 왼쪽 위가 0이면 1부터 다시 시작함.
# 어디 하나라도 짧으면 그 길이가 최대길이로 저장됨.(정사각형을 만들수있는 최대길이.)
max_length = 0
for i in range(1,N+1):
    for j in range(1,M+1):
        if square[i-1][j-1]:
            dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
            if dp[i][j] > max_length:
                max_length = dp[i][j]

print(max_length**2)