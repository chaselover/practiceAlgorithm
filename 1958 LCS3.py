import sys
input = sys.stdin.readline

s1, s2, s3 = (input().rstrip() for _ in range(3))
n1, n2, n3 = len(s1), len(s2), len(s3)
dp = [[[0 for _ in range(n1+1)] for _ in range(n2+1)] for _ in range(n3+1)]

for i in range(n1):
    for j in range(n2):
        for k in range(n3):
            if s1[i] == s2[j] == s3[k]:
                dp[k+1][j+1][i+1] = dp[k][j][i] + 1
            else:
                dp[k+1][j+1][i+1] = max(dp[k][j+1][i+1], dp[k+1][j][i+1], dp[k+1][j+1][i])

print(dp[n3][n2][n1])