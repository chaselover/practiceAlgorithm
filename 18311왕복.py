import sys
input = sys.stdin.readline

N, K = map(int,input().split())
cources =  list(map(int,input().split()))
dp = [0]*(2*N)
dp[0] = cources[0]
if K < dp[0]:
    print(1)
    exit()

for i in range(1,2*N):
    if i<N:
        dp[i] = dp[i-1] + cources[i]
        if dp[i] > K:
            print(i+1)
            exit()
    if i>=N:
        dp[i] = dp[i-1] + cources[N-i%N-1]
        if dp[i] > K:
            print(N-i%N)
            exit()