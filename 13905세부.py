import sys
input = sys.stdin.readline
from collections import deque

def is_possible(limit):
    queue = deque()
    queue.append(s)
    visited = {i: False for i in range(1,N+1)}
    visited[s] = True
    while queue:
        cur_node = queue.popleft()
        if cur_node == e:
            return True
        for next_node, next_limit in graph[cur_node]:
            if not visited[next_node] and limit <= next_limit:
                visited[next_node] = True
                queue.append(next_node)
    return False

N, M = map(int, input().split())
s, e = map(int, input().split())
graph = {i: [] for i in range(1,N+1)}
for _ in range(M):
    a,b,c = map(int, input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])
left = 1
right = 1000000
answer = 0
while left <= right:
    mid = (left + right)//2
    if is_possible(mid):
        left = mid + 1
        answer = mid
    else:
        right = mid - 1

print(answer)