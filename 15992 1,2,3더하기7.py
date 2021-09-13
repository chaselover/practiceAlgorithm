
dp = {j:{} for j in range(1001)}
dp[1][1] = 1
dp[2][1] = 1
dp[3][1] = 1 

def solve(n,m):
    if m<1 or n<1: # basis
        return 0
    if m in dp[n].keys():
        return dp[n][m]
    else:  # optimal substructure
        dp[n][m] = solve(n-3, m-1) + solve(n-2, m-1) + solve(n-1, m-1)
        return dp[n][m]

import sys 
sys.setrecursionlimit(1000000)
T = int(sys.stdin.readline())
for i in range(T):
    n,m = map(int, sys.stdin.readline().strip().split())
    print(solve(n,m)%1000000009)