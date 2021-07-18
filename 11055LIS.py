N = int(input())
A = [0] + list(map(int, input().split()))
dp = [0]*(N+1)


for i in range(1,N+1):
    s = [0]
    for j in range(1,i):
        if A[i]>A[j]:
            s.append(dp[j])
    dp[i] = max(s)+A[i]

print(max(dp))
