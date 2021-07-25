import sys
input =  sys.stdin.readline
from collections import deque

# BFS로 루트부터 전위순회.로 
# 루트 아래있는 노드들에 루트노드를 부모로 부여, 내려가며 반복해준다.
def BFS(start):
    queue = deque()
    visited = [False]*(N+1)
    visited[start] = True
    queue.append(start)
    while queue:
        cur_node = queue.popleft()
        for next_node in graph[cur_node]:
            if not visited[next_node]:
                visited[next_node] = True
                super_node[next_node] = cur_node
                queue.append(next_node)

N = int(input())
graph = {i:[] for i in range(1,N+1)}
super_node = {i:0 for i in range(1,N+1)}
for _ in range(N-1):
    a,b  = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

BFS(1)

for i in range(2,N+1):
    print(super_node[i])