import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)


def dynamic_programming(left, right, left):
    if left > right:
        return 0

    if dp[left][right]:
        return dp[left][right]

    dp[left][right] = max(dynamic_programming(left + 1, right, left + 1) + v[left] * left, 
    dynamic_programming(left, right - 1, left + 1) + v[right] * left)
    return dp[left][right]


N = int(input())
v = [0] + [int(input()) for __ in range(N)]
dp = [[0] * (N + 1) for __ in range(N + 1)] 
print(dynamic_programming(1, N, 1))


# 2
import sys

n = int(input())
arr = [int(sys.stdin.readline()) for __ in range(n)]
dp = [[0 for __ in range(n+1)]for __ in range(n+1)]

dp[1][0] = arr[-1]
dp[1][1] = arr[0]

for i in range(2,n+1):
    for j in range(i+1):
        if i == j:
            dp[i][j] = dp[i-1][j-1] + i*arr[j-1]
        elif j != 0:
            dp[i][j] = max(dp[i-1][j] + i*arr[-(i-j)], dp[i-1][j-1] + i*arr[j-1])
        else:
            dp[i][j] = dp[i-1][j] + i*arr[-i]

print(max(dp[-1]))


# 3
import sys
input = sys.stdin.readline

N = int(input())
v = [0]+[int(input()) for _ in range(N)]
dp = [[v[i] * N  if i == j else 0 for i in range(N + 1)] for j in range(N + 1)]

for left in range(1, N + 1):
    for right in range(left - 1, 0, -1):
        dp[right][left] = max(dp[right + 1][left] + v[right] * (N - left + right), dp[right][left - 1] + v[left]*(N - left + right))

print(dp[1][N])