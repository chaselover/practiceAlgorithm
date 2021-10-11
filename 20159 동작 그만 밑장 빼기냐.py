import sys
input = sys.stdin.readline

N = int(input())
x = list(map(int, input().split()))
# 0, 2, 4 ... 밑장을 받거나 상대 주거나. 하고 홀수 idx를 받음.
even_sum, odd_sum = [0] * (N // 2), [0] * (N // 2)
even_sum[0], odd_sum[-1] = x[0], x[-1]
for i in range(1, N // 2):
    even_sum[i] = x[2 * i] + even_sum[i - 1]
    odd_sum[-i - 1] = x[-2 * i - 1] + odd_sum[-i]
max_sum = 0
for i in range(len(even_sum)):
    if not i == len(even_sum) - 1:
        max_sum = max(max_sum, even_sum[i] + odd_sum[i + 1])
    max_sum = max(max_sum, even_sum[i] + odd_sum[i] - x[-1])
max_sum = max(max_sum, odd_sum[0], even_sum[-1])
print(max_sum)