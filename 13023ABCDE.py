import sys
from collections import defaultdict
input = sys.stdin.readline

N,M = map(int, input().split())
check = [False]*N
graph = defaultdict(list)
cnt = 0

for _ in range(M):
    a,b = map(int,input().split())
    graph[a] += [b]
    graph[b] += [a]

def DFS(v,h):
    if h==4:
        print(1)
        exit()
    for i in graph[v]:
        if check[i]==False:
            check[i] = True
            DFS(i, h+1)
            check[i]=False

for i in range(N):
    check[i] = True
    DFS(i,0)
    check[i]= False
    
print(0)