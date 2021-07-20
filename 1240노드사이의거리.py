import sys
input = sys.stdin.readline
from collections import defaultdict,deque

def Distance(a,b):
    queue = deque()
    queue.append(a)
    visited = [False]*(N+1)
    visited[a] = True
    target_dist = [0]*(N+1)
    while queue:
        v = queue.popleft()
        if v==b:
            print(target_dist[v])
            return
        for next,dist in graph[v]:
            if not visited[next]:
                queue.append(next)
                visited[next] = True
                target_dist[next] += target_dist[v] +dist
                print(queue)



N,M = map(int,input().split())
graph = defaultdict(list)


for _ in range(N-1):
    a,b,dist = map(int,input().split())
    graph[a].append((b,dist))
    graph[b].append((a,dist))

for _ in range(M):
    a,b = map(int,input().split())
    Distance(a,b)