import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
arr = sorted(map(int, input().split()))
left = 0
right = N - 1
answer = 0
while left < right:
    num = arr[left] + arr[right]
    if num == M:
        answer += 1
        left += 1
        right -= 1
    elif num > M:
        right -= 1
    else:
        left += 1
print(answer)