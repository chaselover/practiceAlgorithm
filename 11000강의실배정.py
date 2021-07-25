import heapq
import sys

N = int(input())

timeTable = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
timeTable.sort(key=lambda x: x[0])

queue = []
heapq.heappush(queue,timeTable[0][1])

for i in range(1,N):
    # last_time이 들어오는 시작시간보다 크면?(queue[0]은 가장 작은 last_time)
    # 방하나 늘어남
    if queue[0] > timeTable[i][0]:
        heapq.heappush(queue,timeTable[i][1])
    # 가장 작은 last_time보다 시작시간이 크면 작은거 pop하고 새로운거 넣는다.
    # 방 고대로(pop하고 넣고 반복.)
    else:
        heapq.heappop(queue)
        heapq.heappush(queue,timeTable[i][1])

print(len(queue))
