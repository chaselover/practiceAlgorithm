import sys
input = sys.stdin.readline
from collections import defaultdict
from heapq import heappop,heappush

def dijkstra(v):
    global min_dists
    # 힙큐만들고(거리기준 최소큐)
    heap = []
    # 거리 누적(여러군데 돌아서 누적)
    min_dists = [float('inf')]*(N+1)
    # 최초 0
    min_dists[v] = 0
    # 첫번째 v1입장
    heappush(heap,[min_dists[v],v])
    # 힙큐를 이용 내 현재 가중치(dist로 넣은 내 가중치 보다 작은 가중치의 경로를 먼저 탐색하게 함.)
    while heap:
        # v1거리, 노드(다음부터는 최소 거리를 갖는 노드(인접노드)가 제일 먼저나옴(그리디))
        v_dist,v_node = heappop(heap)
        # 돌아온 거리보다 직접오는거리가 더 클때(직접 안오고 돌아간다(continue))
        # 즉 일단 방문하기로 생각하면 갈지말지 정함(보통 dp는 방문안했으면 무한대이므로 if문으로 잘 안들어감. 
        # 혹은 이미 갔었을 경우 직접가는거보다 갔엇을때 더 작은값이었으면 갈 필요없음.(왔지만 최신화할 필요가 없음.)
        # 이건 직접 가는게 아니라 꺼낸 노드의 저장된 최소거리가 지금 꺼낸 놈의 가중치보다 작으면 검사를 안함.
        if min_dists[v_node] < v_dist:
            continue
        # 가기로했으면 다음꺼 검사.
        for next_node,next_dist in graph[v_node]:
            # 지금 온 거리+다음가는거리 = 가야할거리
            # 해당 노드를 거쳐갈때 다음노드까지의 거리.(다음노드를 계산해야 그 노드까지의 이동을 또 판단할수 있음.)
            dist = v_dist + next_dist
            # 가야할 거리가 다음 노드의 dp_dist보다 작으면 간다(next_node의 dp가 무한대거나 이미갔었는데 기록된 값이 커서 최신화가 필요할 경우.)
            if dist < min_dists[next_node]:
                # dist가 더 최소거리라 가야하면 next_node dp에 가야할 거리값 넣고 heap에 nextnode배치하고 다음 queue로 넘어감.
                min_dists[next_node] = dist
                heappush(heap, [dist, next_node])
    return min_dists

N,E = map(int,input().split())
graph = defaultdict(list)

for _ in range(E):
    a,b,c = map(int,input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])

v1,v2 = map(int,input().split())


results = min(dijkstra(1)[v1]+dijkstra(v1)[v2]+dijkstra(v2)[N],dijkstra(1)[v2]+dijkstra(v2)[v1]+dijkstra(v1)[N])
if results == float('inf'):
    print(-1)
else:
    print(results)