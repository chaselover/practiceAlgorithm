import sys
input = sys.stdin.readline
from heapq import heappop, heappush
from collections import defaultdict



# 각 친구들 위치에서 모든 방에 대해 최소거리 배열 출력.
# 최소 거리 찾는 것이므로 나중에 min쓸꺼 대비해 누적거리는 inf부터 시작함.
def dijkstra(start):
    global dp_dists
    dp_dists = [float('inf')] * (N + 1)
    heap = []
    dp_dists[start] = 0
    heappush(heap, [dp_dists[start], start])
    while heap:
        cur_dist, cur_node = heappop(heap)
        if dp_dists[cur_node] < cur_dist:
            continue
        for next_node, next_dist in graph[cur_node]:
            dist = next_dist + cur_dist
            if dist < dp_dists[next_node]:
                dp_dists[next_node] = dist
                heappush(heap, [dist, next_node])
    return dp_dists


# N개의 방(1~N번)
# M개의 통로(양방향), 가중치
# 친구 K명
for test in range(int(input())):
    N,M = map(int,input().split())
    graph = defaultdict(list)

    for _ in range(M):
        a,b,dist = map(int,input().split())
        graph[a].append((b,dist))
        graph[b].append((a,dist))
    

    # 모든 친구들은 최단 경로를 이용해서 방으로 모일것임.
    K = int(input())
    friends_start = list(map(int,input().split()))
    sum_dists = [0]*(N+1)
    for start in friends_start:
        dijkstra(start)
        for i in range(len(dp_dists)):
            sum_dists[i] += dp_dists[i]

    # 모임장소는 모든 친구들의 이동경로 합이 최소가 되는 방.
    for i in range(1,N+1):
        if sum_dists[i] ==min(sum_dists):
            print(i)
            break