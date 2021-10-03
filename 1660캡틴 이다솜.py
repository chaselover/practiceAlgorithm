import sys
input = sys.stdin.readline

N = int(input())
nums = []
num = 0
idx = 1
while num < N:
    num += (idx * (idx + 1)) // 2
    nums.append(num)
    idx += 1
dp = [float('inf')] * (N + 1)
for i in range(1, N + 1):
    for num in nums:
        if num == i:
            dp[i] = 1
            break
        if num > i: break
        dp[i] = min(dp[i], 1 + dp[i - num])
print(dp[N])