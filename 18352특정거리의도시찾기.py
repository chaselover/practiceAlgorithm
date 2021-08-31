import sys
input = sys.stdin.readline
from collections import deque

def dijkstra(start):
    queue = deque()
    queue.append([0,start])
    visited = {i: float('inf') for i in range(1,N+1)}
    visited[start] = 0
    while queue:
        cur_dist,cur_node = queue.popleft()
        for next in graph[cur_node]:
            if visited[next] > cur_dist+1:
                visited[next] = cur_dist+1
                queue.append([visited[next], next])
    return visited
N, M, K, X = map(int, input().split())
graph = {i: [] for i in range(1,N+1)}
for _ in range(M):
    a, b = map(int, input().split())
    graph[a] += [b]

dists_table = dijkstra(X)
flag=0
for i in range(1,N+1):
    if dists_table[i]==K:
        print(i)
        flag=1
if not flag:
    print(-1)