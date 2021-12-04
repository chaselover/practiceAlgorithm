import sys
input = sys.stdin.readline
from bisect import bisect_right
from math import factorial

for test in range(int(input())):
    n, m, k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    done = {}
    answer = 0
    m -= 1
    for i in range(n - m):
        if arr[i] not in done:
            right = bisect_right(arr, arr[i] + k)
            done[arr[i]] = right
        length = done[arr[i]] - i
        if length >= m:
            length -= 1
            answer += factorial(length) // (factorial(m) * factorial(length - m))
    print(answer)
