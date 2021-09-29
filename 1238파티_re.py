import sys
input = sys.stdin.readline
from heapq import heappop, heappush

def dijkstra(start):
    heap = []
    visited = {i: float('inf') for i in range(1, N + 1)}
    visited[start] = 0
    heappush(heap, (0, start))
    while heap:
        time, cur_node = heappop(heap)
        if visited[cur_node] < time:
            continue
        for next_node, next_time in graph[cur_node]:
            if visited[next_node] > time + next_time:
                visited[next_node] = time + next_time
                heappush(heap, (visited[next_node], next_node))
    return visited
N, M, X = map(int, input().split())
graph = {i: [] for i in range(1, N + 1)}
for __ in range(M):
    s, e, t = map(int, input().split())
    graph[s].append((e, t))

max_dist = 0
dist_X = dijkstra(X)
for i in range(1, N + 1):
    if i == X: continue
    each = dijkstra(i)
    max_dist = max(max_dist, dist_X[i] + each[X])
print(max_dist)