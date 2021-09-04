import sys
input = sys.stdin.readline
from collections import deque

def bfs(start,target):
    visited = {i: 0 for i in range(n+1)}
    visited[start] = 1
    q = deque()
    q.append(start)
    while q:
        cur_node = q.popleft()
        if cur_node==target:
            return visited[cur_node] -1
        for next_node in graph[cur_node]:
            if not visited[next_node]:
                visited[next_node] = visited[cur_node] + 1
                q.append(next_node)
    return -1

    
n = int(input())
a, b = map(int, input().split())
m = int(input())
graph = {i: [] for i in range(1,n+1)}
for _ in range(m):
    x, y = map(int, input().split())
    graph[y] += [x]
    graph[x] += [y]

print(bfs(a,b))

