import sys
input = sys.stdin.readline
from collections import defaultdict

for _ in range(3):
    N = int(input())
    coins = defaultdict(int)
    target = 0
    for _ in range(N):
        a, b = map(int, input().split())
        coins[a] += b
        target += a*b
    if target&1:
        print(0)
        continue
    target //= 2 