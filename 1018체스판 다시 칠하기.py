import sys
input = sys.stdin.readline

N,M = map(int,input().split())
chess = [list(input().rstrip()) for _ in range(N)]

dp = [[0]*M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if i%2 == j%2:
            if chess[0][0] != chess[i][j]:
                dp[i][j]=1
        else:
            if chess[0][0] == chess[i][j]:
                dp[i][j]=1

min_change = float('inf')
for i in range(N-7):
    for j in range(M-7):
        sum_count = 0
        for k in range(i,i+8):
            sum_count += sum(dp[k][j:j+8])
        if sum_count > 32:
            sum_count = 64 - sum_count
        if min_change > sum_count:
            min_change = sum_count

print(min_change)