import sys
input = sys.stdin.readline
from heapq import heappop,heappush

def dijkstra(start):
    heap = []
    heappush(heap,[start,0])
    visited = {i: float('inf') for i in range(1,n+1)}
    visited[start] = 0
    item_check = {i: False for i in range(1,n+1)}
    item_check[start] = True
    item_cnt = items[start]
    while heap:
        cur_node, total_dist = heappop(heap)
        for next_dist, next_node in graph[cur_node]:
            if total_dist + next_dist <= m and total_dist + next_dist < visited[next_node]:
                visited[next_node] = total_dist + next_dist
                heappush(heap,[next_node,visited[next_node]])
                if not item_check[next_node]:
                    item_cnt += items[next_node]
                    item_check[next_node] = True
    return item_cnt

n, m, r = map(int, input().split())
items = [0] + list(map(int, input().split()))
graph = {i: [] for i in range(1, n+1)}
for _ in range(r):
    a, b, c = map(int, input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))

max_item = 0
for i in range(1,n+1):
    max_item = max(dijkstra(i),max_item)
print(max_item)