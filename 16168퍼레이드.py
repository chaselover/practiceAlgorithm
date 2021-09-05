import sys
input =sys.stdin.readline


def find(x):
    if parent[x] ==x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a = find(a)
    b = find(b)

    if level[a] >= level[b]:
        parent[b] = a
        if level[a]==level[b]:
            level[a] += 1
    else:
        parent[a] = b

V, E = map(int, input().split())

graph = {i: [] for i in range(1,V+1)}
parent = {i: i for i in range(1,V+1)}
level = {i: 0 for i in range(1,V+1)}
for _ in range(E):
    a, b = map(int, input().split())
    if find(a) != find(b):
        union(a,b)
    if a>b:
        a,b = b,a
    graph[a].append(b)
    graph[b].append(a)


pivot = find(1)
for node in range(2,V+1):
    if pivot != find(node):
        print("NO")
        exit()


cnt = 0
for start_node in range(1,V+1):
    if len(graph[start_node])&1:
        cnt += 1

print('YES' if not cnt or cnt==2 else 'NO')