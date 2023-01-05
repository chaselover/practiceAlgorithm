import sys
import heapq

INF = sys.maxsize
input = sys.stdin.readline
N, M, K = map(int, input().split())
K += 1

# N * K 배열로 만듦
vstd = [[False] * K for _ in range(N)]
dist = [[INF] * K for _ in range(N)]

adj = [[] for _ in range(N)]

# 양방향 도로이기 때문에 u -> v, v -> u로 도로를 추가
for _ in range(M):
    u, v, w = map(int, input().split())
    adj[u - 1].append((v - 1, w))
    adj[v - 1].append((u - 1, w))

h = []
heapq.heappush(h, (0, 0, K - 1))

# 서울에서의 모든 시간은 0으로 초기화
for i in range(K):
    dist[0][i] = 0

while h:
    _, curr, k = heapq.heappop(h)
    
    #현재 도시에서 k번 포장한 최단거리를 이미 방문했다면 continue
    if vstd[curr][k]:
        continue
    vstd[curr][k] = True
    
    for nxt, d in adj[curr]:
        if dist[curr][k] + d < dist[nxt][k]:
            dist[nxt][k] = dist[curr][k] + d
            heapq.heappush(h, (dist[nxt][k], nxt, k))
            # 포장을 할 수 있고 다음 도로보다 시간이 짧다면 포장해줌
            if k > 0:
                if dist[nxt][k - 1] > dist[curr][k]:
                    dist[nxt][k - 1] = dist[curr][k]
                heapq.heappush(h, (dist[nxt][k - 1], nxt, k - 1))
                
# 포천에서의 1-k번 사용했을 때의 최소 시간 중 최소값이 결과값
print(min(dist[-1]))