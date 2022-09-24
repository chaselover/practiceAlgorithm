import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def DFS(v):
    visited[v]=1
    for next in graph[v]:
        if not visited[next]:
            DFS(next)
            visited[v]+=visited[next]
    return

# 리프에 1을 깔고 올라오면서 자기만큼 더해준다.
N,R,Q = map(int,input().split())
graph = {i:[] for i in range(1,N+1)}
visited = {i:0 for i in range(1,N+1)}
for _ in range(N-1):
    a,b = map(int,input().split())
    graph[a] += [b]
    graph[b] += [a]

DFS(R)

for _ in range(Q):
    query = int(input())
    print(visited[query])