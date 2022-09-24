import sys
input = sys.stdin.readline

# 소 N마리
N,Q = map(int,input().split())
A = list(map(int,input().split()))
dp = [0]*N
# 미리계산.
for i in range(N):
    dp[i] = A[i]*A[i-1]*A[i-2]*A[i-3]

Qs = list(map(int,input().split()))
# 미리계산
ex_sum = sum(dp)
for idx in Qs:
    for i in range(4):
        new_idx = (idx-1+i)%N
        dp[new_idx] = -dp[new_idx]
        ex_sum+=2*dp[new_idx]
    print(ex_sum)