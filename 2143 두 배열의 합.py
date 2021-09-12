import sys
input = sys.stdin.readline
from collections import defaultdict


T = int(input())
n = int(input())
arr_a = list(map(int, input().split()))
check = defaultdict(int)
for k in range(1, n+1):
    left = 0
    s = 0
    for right in range(n):
        s += arr_a[right]
        if right - left == k-1:
            check[T - s] += 1
            s -= arr_a[left]
            left += 1
ans = 0
m = int(input())
arr_b = list(map(int, input().split()))
for k in range(1, m+1):
    left = 0
    s = 0
    for right in range(m):
        s += arr_b[right]
        if right - left == k-1:
            if s in check:
                ans += check[s]
            s -= arr_b[left]
            left += 1
print(ans)