N = int(input())
A = [0] + list(map(int, input().split()))
dp = [1]*(N+1)


for i in range(1,N+1):
    for j in range(1,i):
        if A[i]<A[j] and dp[i]<=dp[j]:
            dp[i] = dp[j] + 1
    

print(max(dp))
