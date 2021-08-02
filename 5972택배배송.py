import sys
input = sys.stdin.readline
from heapq import heappop,heappush

def dijkstra(start):
    min_dists[start] = 0
    heap = []
    heappush(heap,[0,start])
    while heap:
        cur_dists, cur_node = heappop(heap)
        for next_node,next_dist in graph[cur_node]:
            if min_dists[next_node] > cur_dists + next_dist:
                min_dists[next_node] = cur_dists + next_dist
                heappush(heap,[min_dists[next_node],next_node])


N,M = map(int,input().split())
graph = {i:[] for i in range(1,N+1)}
min_dists = {i:float('inf') for i in range(1,N+1)}
for _ in range(M):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

dijkstra(1)

print(min_dists[N])