import sys
input = sys.stdin.readline
from heapq import heappop, heappush

n = int(input())

heap = []
count = 0
for _ in range(n):
    num, start, end = map(int, input().split())
    heappush(heap, [start,end,num])

classroom = []
start, end, num = heappop(heap)
heappush(classroom, end)
while heap:
    start, end, num = heappop(heap)
    if classroom[0] <= start:
        heappop(classroom)
    heappush(classroom, end)
print(len(classroom))