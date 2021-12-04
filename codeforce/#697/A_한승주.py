import sys
input = sys.stdin.readline


for test in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    left, right = 0, n - 1
    answer = []
    while left <= right:
        answer.append(arr[left])
        if left == right:
            break
        answer.append(arr[right])
        left += 1
        right -= 1
    print(*answer)