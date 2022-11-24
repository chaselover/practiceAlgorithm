import heapq
import sys
input = sys.stdin.readline
INF = sys.maxsize
n, m, k = map(int, input().split())

graph = [[] for _ in range(n+1)]
distance = [[INF for _ in range(k+1)] for _ in range(n+1)] # 도로를 몇개 포장했는지 확인하기 위해서 이중리스트로 만든다.
for i in range(m):
    x,y,z = map(int,input().split())
    graph[x].append((z,y))
    graph[y].append((z,x))

def dijkstra(start):
    queue = []
    cnt = 0
    distance[start][cnt] = 0
    heapq.heappush(queue, (0, start, cnt))

    while queue:
        wei, now, cnt = heapq.heappop(queue)
        if distance[now][cnt] < wei:
            continue
        for w, next_node in graph[now]:
            next_wei = w + wei
            if distance[next_node][cnt] > next_wei:
                distance[next_node][cnt] = next_wei
                heapq.heappush(queue, (next_wei, next_node,cnt))
                
            # elif로 안하고 if로 하는 이유는 모든곳을 돌아 도로포장을 했을때 가장 작은 값을 찾기 위해서이다.
            if cnt < k and distance[next_node][cnt+1] > wei: 
            # 도로포장 횟수가 남았고 현재까지 distance[next_node][cnt+1](next_node 까지 가중치)가 wei(now 노드까지 가중치)보다 크다면 
            # next_node까지 움직이는 w(now에서 next_node까지 가중치)를 무시하고 wei를 넣어준다.
                distance[next_node][cnt+1] = wei
                heapq.heappush(queue, (wei, next_node, cnt+1))


dijkstra(1)
print(min(distance[n]))