import sys
input = sys.stdin.readline
from heapq import heappop,heappush

N = int(input())
arr = []
for _ in range(N):
    x = int(input())
    if x:
        heappush(arr,(abs(x),x))
        continue
    try:
        print(heappop(arr)[1])
    except:
        print(0)
