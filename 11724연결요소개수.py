import sys
input = sys.stdin.readline
from collections import defaultdict
sys.setrecursionlimit(1000)

N,M = map(int,input().split())
graph = defaultdict(list)
check = [0]*(N+1)

for _ in range(M):
    u,v = map(int,input().split())
    graph[u] += [v]
    graph[v] += [u]

def DFS(v,cnt):
    check[v] = cnt
    for i in graph[v]:
        if check[i] ==0:
            check[i] = cnt
            DFS(i,cnt)

for i in range(1,N+1):
    if check[i] ==0:
        DFS(i,i)
count = len(set(check))
print(count-1)
