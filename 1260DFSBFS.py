import sys
input = sys.stdin.readline
from collections import defaultdict

N,M,V = list(map(int,input().split()))
graph = defaultdict(list)
check = [True] +[False]*(N)
stack = []

for _ in range(M):
    a,b = map(int,input().split())
    graph[a] +=[b]
    graph[b] +=[a]

for i in range(1,N+1):
    graph[i].sort()

def DFS(v):
    stack.append(v)
    check[v] = True
    for i in graph[v]:
        if check[i]==False:
            DFS(i)
    return stack

def BFS(v):
    queue = [v]
    stack.append(v)
    check[v] = True
    while queue:
        v = queue.pop(0)
        for i in graph[v]:
            if check[i] ==False:
                queue.append(i)
                stack.append(i)
                check[i] = True
    return stack

ans_DFS = DFS(V)
print(*ans_DFS)
check = [True] +[False]*(N)
stack = []
ans_BFS = BFS(V)
print(*ans_BFS)