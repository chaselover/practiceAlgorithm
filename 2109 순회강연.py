import sys
input = sys.stdin.readline
from heapq import heappop,heappush

n=int(input())
arr=[list(map(int, input().split())) for _ in range(n)]
arr.sort(key=lambda x: x[1])

heap=[]
for i in arr:
    heappush(heap, i[0])
    if (len(heap)>i[1]):
        heappop(heap)
print(sum(heap))