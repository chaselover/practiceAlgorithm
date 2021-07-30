import sys
input = sys.stdin.readline
from heapq import heappop,heappush

def dijkstra(start):
    heap = []
    dp_dists[start] = 0
    heappush(heap,[dp_dists[start],start])
    while heap:
        cur_dists,cur_node= heappop(heap)
        for next_dists,next_node in network[cur_node]:
            if dp_dists[next_node] > cur_dists + next_dists:
                dp_dists[next_node] = cur_dists + next_dists
                path[next_node] = cur_node
                heap.append([dp_dists[next_node],next_node])

N,M = map(int,input().split())
network = {i:[] for i in range(1,N+1)}
dp_dists = {i:float('inf') for i in range(1,N+1)}
path = {i:0 for i in range(1,N+1)}
for _ in range(M):
    A,B,C = map(int,input().split())
    network[A].append([C,B])
    network[B].append([C,A])

dijkstra(1)

print(N-1)
for i in range(2,N+1):
    print(i,path[i])