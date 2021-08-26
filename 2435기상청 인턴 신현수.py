import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
left = 0
prefix_sum = 0
answer = -float('inf')
for right in range(N):
    prefix_sum += arr[right]
    while right-left+1 >= M:
        answer = max(answer, prefix_sum)
        prefix_sum -= arr[left]
        left += 1
print(answer)