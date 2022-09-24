import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

# 간선정보 정렬 완료.
edge = [list(map(int,input().split())) for _ in range(M)]
edge.sort(key = lambda x : x[2])

parent = [i for i in range(N+2)]

def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    x = find(x)
    y = find(y)

    parent[x] = y



# MST그리기.
cost = 0
for a,b,c in edge:
    if find(a) != find(b):
        union(a,b)
        cost += c

print(cost)