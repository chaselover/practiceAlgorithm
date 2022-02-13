import sys
input = sys.stdin.readline
from collections import defaultdict

m, n = map(int, input().split())
universe = defaultdict(int)
for _ in range(m):
    planets = list(map(int, input().split()))
    keys = sorted(list(set(planets)))
    ranks = {keys[i]: i for i in range(len(keys))}
    add = tuple([ranks[x] for x in planets])
    universe[add] += 1

ans = 0
for cnt in universe.values():
    ans += cnt * (cnt - 1) // 2
print(ans)