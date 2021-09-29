import sys
input = sys.stdin.readline
from heapq import heappush, heappop


def dijkstra(start):
    visited[start] = 0
    heap = []
    heappush(heap,[visited[start], start])
    while heap:
        time, cur_node = heappop(heap)
        if visited[cur_node] < time:
            continue
        for next_time, next_node in edges[cur_node]:
            if visited[next_node] > time + next_time:
                visited[next_node] = time + next_time
                heappush(heap, [visited[next_node], next_node])


N, M = map(int, input().split())
# arr가 1이면 못지나감.
arr = list(map(int, input().split()))
edges = {i: [] for i in range(N)}
visited = {i: float('inf') for i in range(N)}
for __ in range(M):
    a, b, t = map(int, input().split())
    if a != N-1 and b != N-1 and (arr[a] or arr[b]):
        continue
    edges[a].append((t, b))
    edges[b].append((t, a))
dijkstra(0)
print(visited[N-1] if visited[N-1] != float('inf') else -1)