import sys
input = sys.stdin.readline

str1, str2 = (input().rstrip() for _ in range(2))
n, m = len(str1), len(str2)
dp = [[0]*(m+1) for _ in range(n+1)]
max_v = 0
for i in range(1,n+1):
    for j in range(1,m+1):
        if str1[i-1] == str2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
            if dp[i][j] > max_v:
                max_v = dp[i][j]
print(max_v)