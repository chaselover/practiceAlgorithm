MAX = 100000
mod = 1000000009
DP = [[0]*(3+1) for _ in range(MAX+1)]
 
DP[0] = [0, 0, 0, 0]
DP[1] = [0, 1, 0, 0]
DP[2] = [0, 0, 1, 0]
DP[3] = [0, 1, 1, 1]
 
for i in range(4, MAX + 1):
    DP[i][1] = (DP[i - 1][2] + DP[i - 1][3]) % mod
    DP[i][2] = (DP[i - 2][1] + DP[i - 2][3]) % mod
    DP[i][3] = (DP[i - 3][1] + DP[i - 3][2]) % mod
 
for _ in range(int(input())):
    N = int(input())
    print(sum(DP[N])% mod)