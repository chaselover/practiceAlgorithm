import sys
from collections import deque,defaultdict
input = sys.stdin.readline

n = int(input())
graph = defaultdict(list)

for _ in range(n-1):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))



def bfs(v):
    visited = [-1] * (n + 1)
    queue = deque()
    queue.append(v)
    visited[v] = 0
    max_node = [0, 0]

    while queue:
        t = queue.popleft()
        for e, w in graph[t]:
            if visited[e] == -1:
                visited[e] = visited[t] + w
                queue.append(e)
                if max_node[0] < visited[e]:
                    max_node = visited[e], e

    return max_node


dist, node = bfs(1)
dist, node = bfs(node)
print(dist)

# 트리의 지름(그래프 간 가장 먼 노드 사이의 거리) = 아무 노드에서 최장 노드, 그 노드에서 다시한번 최장노드 = 지름