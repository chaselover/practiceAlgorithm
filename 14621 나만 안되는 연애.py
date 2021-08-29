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
sex = [0] + list(input().split())
arr = []
parent = {i:i for i in range(1,N+1)}
level = {i:0 for i in range(1,N+1)}
for _ in range(M):
    u, v, d = map(int, input().split())
    arr.append([d,u,v])
arr.sort()
answer = 0
for i in range(M):
    dist,start,end = arr[i]
    if find(start) != find(end) and sex[start] != sex[end]:
        union(start,end)
        answer += dist
target = find(1)
for i in range(2,N+1):
    if target != find(i):
        print(-1)
        exit()
else:
    print(answer)