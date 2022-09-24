import sys
input = sys.stdin.readline

G = int(input())
P = int(input())
parent = [i for i in range(G+1)] 

def find(v):
    if parent[v] == v:
        return v
    parent[v] = find(parent[v])
    return parent[v]

def union(a, b):
    a = find(a)
    b = find(b)
    parent[b] = a

arr = [int(input()) for _ in range(P)]

ans = 0

for v in arr:
    p = find(v)
    if p == 0:
        break
    ans += 1
    union(p-1, p) 

print(ans)