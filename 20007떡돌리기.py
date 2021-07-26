import sys
input = sys.stdin.readline
from heapq import heappop,heappush

# 1. 0번에서 각 집에 가는 최소거리. -> 다익스트라
def dijkstra(start):
    heap = []
    dp_dists[start] = 0
    heappush(heap,[dp_dists[start],start])
    while heap:
        cur_dist,cur_node = heappop(heap)
        for next_node,next_dists in graph[cur_node]:
            dists = cur_dist + next_dists
            if dp_dists[next_node] > dp_dists[cur_node] + dists:
                dp_dists[next_node] = dp_dists[cur_node] + dists
                heappush(heap,[dp_dists[next_node],next_node])


# 떡 한번에 하나씩. 집들 사이에 총 M개의 양방향 도로
# 하루에 X이상 가지 않음. 가까운 집부터 방문. 왕복할 수 없으면 미룸.
# N-1개의 이웃집에 떡돌리려면 몇 일?
# 집은 0~N-1번까지.
N,M,X,Y = map(int,input().split())
graph = {i:[] for i in range(N)}
dp_dists = {i:float('inf') for i in range(N)}

for _ in range(M):
    a,b,c = map(int,input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])

dijkstra(0)

# 2. 최소거리*2가 X이상이면 -1출력
for house in dp_dists.values():
    if house > 2*X:
        print(-1)
        exit()


# 3. 최소거리*2의 합이 X이하인 조합의 최소갯수.
# 4. 내림차순 정렬하고 아래로 타고 내려가면서 X까지 채우는 식으로. 냅색 0-1문제이므로 2차원 dp활용?
