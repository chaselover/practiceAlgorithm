import sys
input = sys.stdin.readline
from heapq import heappop,heappush

def find(x):
    if parent[x]==x:
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

n, m = map(int, input().split())
parent = {i:i for i in range(1,n+1)}
level = {i: 0 for i in range(1,n+1)}
# 2~n번컴퓨터까지 MST를 만들어라?
for _ in range(m):
    x, y = map(int, input().split())
    if find(x) != find(y):
        union(x,y)

cost_matrix = [list(map(int, input().split())) for _ in range(n)]
costs = []
for i in range(1,n-1):
    for j in range(i+1,n):
        heappush(costs,(cost_matrix[i][j],i+1,j+1))

min_cost = 0
cnt = 0
coms = []
while costs:
    c, a, b = heappop(costs)
    if find(a) != find(b):
        union(a,b)
        min_cost += c
        cnt += 1
        coms.append([a,b])
print(min_cost, cnt)
for com in coms:
    print(*com)