import sys
input = sys.stdin.readline
from bisect import bisect_left
 
for test in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    done = {}
    answer = 0
    for i in range(n - 2):
        if arr[i] not in done:
            right = bisect_left(arr, arr[i] + 3)
            done[arr[i]] = right
        length = done[arr[i]] - i
        if length > 2:
            length -= 2
            answer += length * (length + 1) // 2
    print(answer)