import sys
input = sys.stdin.readline
from heapq import heappush, heappop

N = int(input())
buses = []
for _ in range(N):
    arrive, leave = input().split()
    a = int(''.join((''.join(arrive.split(':'))).split('.')))
    b = int(''.join((''.join(leave.split(':'))).split('.')))
    buses.append([a,b])
buses.sort()

heap = []
heappush(heap,buses[0][1])
for i in range(1,N):
    if buses[i][0] >= heap[0]:
        heappop(heap)
        heappush(heap, buses[i][1])
    else:
        heappush(heap, buses[i][1])
print(len(heap))