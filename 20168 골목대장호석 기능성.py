import heapq
import sys
input = sys.stdin.readline


def dijkstra(mid):
    dist = [float('inf')] * (N + 1)
    dist[start] = 0
    H = [(0, start)]
    while H:
        dist, cur_node = heapq.heappop(H)
        if dist[cur_node] < dist:
            continue
        for next_node, cost in graph[cur_node]:
            if cost > mid: 
                continue
            if dist[next_node] > dist + cost:
                dist[next_node] = dist + cost
                heapq.heappush(H, (dist + cost, next_node))
    return dist[end] <= cost

N, mid, start, end, cost = map(int, input().split())
graph = {i: [] for i in range(1, N + 1)}
costs = set()
for i in range(mid):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
    costs.add(c)
costs = sorted(costs)
left = 0
right = len(costs)
while left < right:
    mid = (left + right) // 2
    if dijkstra(costs[mid]): 
        right = mid
    else: 
        left = mid + 1
print(costs[left] if left < len(costs) else -1)