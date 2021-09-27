import sys
input = sys.stdin.readline

N, M = map(int, input().split())
H = list(map(int, input().split()))
save = [0] * (N+1)
for _ in range(M):
    a, b, k = map(int, input().split())
    save[a-1] += k
    save[b] -= k

dp = [0] * (N+1)
dp[0] = save[0]
for i in range(1,N+1):
    dp[i] = dp[i-1] + save[i]

for i in range(N):
    print(H[i] + dp[i], end=' ')