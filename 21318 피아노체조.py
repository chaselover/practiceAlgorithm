import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
dp = [0]*N
for i in range(1,N):
    if arr[i-1] <= arr[i]:
        dp[i] = dp[i-1] + 1
    else:
        dp[i] = dp[i-1]
Q = int(input())
for _ in range(Q):
    x, y = map(int, input().split())
    print((y-x) - (dp[y-1] - dp[x-1]))