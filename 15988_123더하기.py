import sys
input = sys.stdin.readline

def findCase(n):
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    if n>3:
        for i in range(4,n+1):
            if dp[i]:
                continue
            dp[i] = (dp[i-1] + dp[i-2] + dp[i-3])%1000000009
    return dp[n]

T = int(input())
dp = [0] * 1000001

for test in range(T):
    n = int(input())
    
    print(findCase(n))