import sys
input = sys.stdin.readline
from heapq import heappop,heappush


def go_masan(start):
    dp_visited = {i: float('inf') for i in range(1,V+1)}
    dp_visited[start] = 0
    heap = []
    heappush(heap,[dp_visited[start],start])
    while heap:
        cur_dist, cur_node = heappop(heap)
        if cur_node == V:
            return dp_visited[P],dp_visited[V]
        for next_dist, next_node in graph[cur_node]:
            if dp_visited[next_node] > cur_dist + next_dist:
                dp_visited[next_node] = cur_dist + next_dist
                heappush(heap,[dp_visited[next_node],next_node])

V, E, P = map(int, input().split())
graph = {i: [] for i in range(1,V+1)}
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))

p_dist, masan_dist = go_masan(1)
zero, p_to_masan = go_masan(P)
if p_dist + p_to_masan == masan_dist:
    print('SAVE HIM')
else:
    print('GOOD BYE')