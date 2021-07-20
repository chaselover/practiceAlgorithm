import sys
from collections import deque,defaultdict

input = sys.stdin.readline
V = int(input())
graph = defaultdict(list)

for _ in range(V):
    c = list(map(int, input().split()))
    for e in range(1, len(c) - 2, 2):
        graph[c[0]].append(c[e:e + 2])


def bfs(v):
    visited = [-1] * (V + 1)
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