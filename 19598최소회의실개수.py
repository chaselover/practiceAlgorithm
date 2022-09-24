import sys
input = sys.stdin.readline
from heapq import heappop,heappush

N = int(input())
meeting_schedule = [list(map(int,input().split())) for _ in range(N)]
meeting_schedule.sort()

cnt = 0
heap = []
for start,end in meeting_schedule:
    if not heap or heap[0] > start :
        cnt +=1
        heappush(heap,end)
    else:
        heappop(heap)
        heappush(heap,end)

print(cnt)