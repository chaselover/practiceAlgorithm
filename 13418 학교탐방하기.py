import sys
input = sys.stdin.readline
def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a = find(a)
    b = find(b)

    if level[a] >= level[b]:
        parent[b] = a
        if level[a]==level[b]:
            level[a] +=1
    else:
        parent[a] = b

N, M = map(int, input().split())
parent = {i:i for i in range(N+1)}
level = {i:0 for i in range(N+1)}
edges = []
for _ in range(M+1):
    a, b, c = map(int, input().split())
    edges.append([c,a,b])
edges.sort()
ascend = 0
for i in range(M+1):
    cost, a, b = edges[i]
    if find(a) != find(b):
        union(a,b)
        ascend += cost
parent = {i:i for i in range(N+1)}
level = {i:0 for i in range(N+1)}
decend = 0
for i in range(M,-1,-1):
    cost, a, b = edges[i]
    if find(a) != find(b):
        union(a,b)
        decend += cost
print((N-ascend)**2 - (N-decend)**2)