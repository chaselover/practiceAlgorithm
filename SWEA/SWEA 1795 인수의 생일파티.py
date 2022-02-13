import sys
sys.stdin = open('input.txt')
from heapq import heappop, heappush


def dijkstra(graph, start):
    dp_dists = {i: float('inf') for i in range(1, N + 1)}
    dp_dists[start] = 0
    heap = []
    heappush(heap, (0, start))
    while heap:
        cur_dists, cur_node = heappop(heap)
        for next_node, next_dist in graph[cur_node]:
            dists = cur_dists + next_dist
            if dp_dists[next_node] > dists:
                dp_dists[next_node] = dists
                heappush(heap, (dists, next_node))
    return dp_dists


for test in range(1, int(input()) + 1):
    N, M, X = map(int, input().split())
    graph = {i: [] for i in range(1, N + 1)}
    reverse_graph = {i: [] for i in range(1, N + 1)}

    for _ in range(M):
        x, y, c = map(int, input().split())
        graph[x].append((y, c))
        reverse_graph[y].append((x, c))
    dist_set = dijkstra(graph, X)
    re_dist_set = dijkstra(reverse_graph, X)

    max_distance = 0
    for i in range(1, N + 1):
        max_distance = max(max_distance, dist_set[i] + re_dist_set[i])

    print(f'#{test} {max_distance}')