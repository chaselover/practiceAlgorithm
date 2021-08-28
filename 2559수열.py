import sys
input = sys.stdin.readline


N, K = map(int, input().split())
arr = list(map(int, input().split()))

left = 0
sum_arr = 0
max_sum = -float('inf')
for right in range(N):
    sum_arr += arr[right]
    if right-left+1 == K:
        max_sum = max(max_sum,sum_arr)
        sum_arr -= arr[left]
        left += 1
print(max_sum)
