import sys, heapq

N, K = map(int,sys.stdin.readline().split())


jew = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

bag = [int(sys.stdin.readline()) for _ in range(K)]

max_value = 0

jew = sorted(jew)
bag = sorted(bag)


max_heap = []
i=0

for j in range(K):
    while i<N and jew[i][0] <= bag[j]:
        heapq.heappush(max_heap,-jew[i][1])
        i+=1
    
    max_value += -heapq.heappop(max_heap)


print(max_value)

