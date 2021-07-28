import sys
input = sys.stdin.readline
from collections import deque

def topological_sort():
    queue=deque()
    for i in range(1,N+1):
        if not level[i]:
            queue.append(i)
            answer.append(i)
    while queue:
        cur_node=queue.popleft()
        for next_node in graph[cur_node]:
            level[next_node] -=1
            if not level[next_node]:
                queue.append(next_node)
                answer.append(next_node)

N,M = map(int,input().split())
graph = {i:[] for i in range(1,N+1)}
level = {i:0 for i in range(1,N+1)}
answer = []
for _ in range(M):
    a,b=map(int,input().split())
    graph[a] += [b]
    level[b] += 1
    
topological_sort()

print(*answer)