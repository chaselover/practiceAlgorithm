import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n,m = map(int,input().split())
parent = [i for i in range(n+1)]

def Union(a,b):
    a = Find(a)
    b = Find(b)

    if a>b:
        parent[a] = b
    else:
        parent[b] = a

def Find(u):
    if parent[u]==u:
        return u
    parent[u] = Find(parent[u])
    return parent[u]



for _ in range(m):
    flag, x, y = map(int,input().split())

    if flag:
        if Find(x) == Find(y):
            print("YES")
        else:
            print("NO")
    else:
        Union(x,y)
    