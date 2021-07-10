
n,m = map(int,input().split())
parent = [0]*(n+1)

for i in range(n+1):
    parent[i] = i

def Union(a,b):
    a = Find(a)
    b = Find(b)

    if a==b:
        return
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
    z, x, y = map(int,input().split())
    if not z:
        Union(x,y)
    
    if z:
        if Find(x) == Find(y):
            print("YES")
        else:
            print("NO")
    