import sys
input = sys.stdin.readline

def bellman_ford(start):
    dp_dists[start] = 0

# 모든 정점 수만큼 검사
    for i in range(N):
        # 매 정점마다 모든 간선 검사(그 점에서 타 점까지)
        for cur_node in graph:
            for next_node, dist in graph[cur_node]:
                # 방문 안했거나 다음점보다 지금 가는 경로가 더 짧으면 갱신
                if dp_dists[cur_node] !=float('inf') and dp_dists[next_node] > dp_dists[cur_node]+dist:
                    dp_dists[next_node] = dp_dists[cur_node]+dist
                    # N-1번째 순회일때 최단거리 갱신이 된다면 음의 사이클 존재.
                    if i==N-1:
                        return True

    return False




N,M = map(int,input().split())
graph = {i:[] for i in range(1,N+1)}
dp_dists = [float('inf') for _ in range(N+1)]

for _ in range(M):
    a,b,c = map(int,input().split())
    graph[a].append([b,c])


negative_cycle = bellman_ford(1)

if negative_cycle:
    print(-1)
else:
    # 1번말고 다른 노드들로 가는dp값 출력.
    for i in range(2,N+1):
        if dp_dists[i] == float('inf'):
            print(-1)
        else:
            print(dp_dists[i])
