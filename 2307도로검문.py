import sys
input = sys.stdin.readline
from heapq import heappop,heappush

# 가중치 있는 그래프.
# 최소 시간. 양수.
# 경찰 도로 검문(간선 가중치 무한대).(탈출 지연)
# 1진입 N탈출. -> 다익스트라.
# 경찰이 도로를 막았을때 지연시킬 수 있는 최대시간을 정수로 출력.
# 지연효과없으면 0, 못빠져나가게 할수있으면(최소시간이inf면) -1출력.
def dijkstra(a,b):
    dp_dists = {i:float('inf') for i in range(1,p_cnt+1)}
    heap = []
    dp_dists[1] = 0
    heappush(heap,[dp_dists[1],1])
    while heap:
        cur_dist,cur_node = heappop(heap)
        for next_node, next_dist in roads[cur_node]:
            if (cur_node ==a and next_node==b) or (cur_node==b and next_dist==a):
                continue
            if dp_dists[next_node] > cur_dist + next_dist:
                dp_dists[next_node] = cur_dist + next_dist
                heappush(heap,[dp_dists[next_node],next_node])
                if a==0:
                    optimal_path[next_node] = cur_node
    return dp_dists[p_cnt]


p_cnt,road_cnt = map(int,input().split())
roads = {i:[] for i in range(1,p_cnt+1)}
for _ in range(road_cnt):
    a,b,t = map(int,input().split())
    roads[a].append((b,t))
    roads[b].append((a,t))

optimal_path = {i:0 for i in range(1,p_cnt+1)}
no_police = dijkstra(0,0)

max_cost = 0
for path in optimal_path:
    a,b = optimal_path[path],path
    new_time = dijkstra(a,b)
    if max_cost<(new_time-no_police):
        max_cost = new_time-no_police

if max_cost==float('inf'):
    print(-1)
elif max_cost>=0:
    print(max_cost)
