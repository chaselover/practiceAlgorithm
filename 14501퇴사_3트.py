import sys
input = sys.stdin.readline

N = int(input())
T = []
P = []
dp=[]
for _ in range(N):
    t,p = map(int,input().split())
    T.append(t)
    P.append(p)
    dp.append(p)
dp.append(0)
for i in range(N-1,-1,-1):
    if i + T[i] > N:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1],dp[i+T[i]]+P[i])

print(dp[0])
    