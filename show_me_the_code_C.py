import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
li = []
for i in range(n):
    li.append(A[i] - B[i])
dp = []
dp.append(li[0])
for i in range(1, n):
    dp.append(dp[i - 1] + li[i])
print(dp)