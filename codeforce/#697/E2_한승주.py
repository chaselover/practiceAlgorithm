import sys
input = sys.stdin.readline
from bisect import bisect_right
from math import factorial

MOD = int(1e9) + 7
for test in range(int(input())):
    n, m, k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    done = {}
    answer = 0
    for i in range(n - m + 1):
        if arr[i] not in done:
            right = bisect_right(arr, arr[i] + k)
            done[arr[i]] = right
        length = done[arr[i]] - i
        if length >= m:
            answer += (factorial(length - 1) // (factorial(m - 1) * factorial(length - m))) % MOD
    print(answer % MOD)
