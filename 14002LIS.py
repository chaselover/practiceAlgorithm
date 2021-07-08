# 1~1000
N = int(input())
A = list(map(int,input().split()))
dp = [0]*N

# A수열에 대해 LIS를 구하라.
# A[i]보다 작은 값을 가지면서 dp가 i번째보다 작은것은 dp값을 이어받는다.

for i in range(N):
    for j in range(i):
        if A[i] > A[j] and dp[i] <dp[j]:
            dp[i] = dp[j]
    dp[i]+=1

print(max(dp))

