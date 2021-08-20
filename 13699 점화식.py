import sys
input = sys.stdin.readline

def t(n):
    if not n:
        return 1
    if not dp[n]:
        for i in range(n):
            dp[n] += t(i)*t(n-1-i)
    return dp[n]


n = int(input())
dp = [0]*36
print(t(n))