N = int(input())
P = [0] + list(map(int,input().split()))
dp = [0]*(N+1)

dp[1] = P[1]


# dp[i]랑 dp k 전에꺼 + k개 들어있는 팩의 값
for i in range(2,N+1):
    for k in range(1,i+1):
        dp[i] = max(dp[i],dp[i-k]+P[k])

print(dp[N])