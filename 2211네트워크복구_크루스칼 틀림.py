import sys
input = sys.stdin.readline

def find(x):
    if parents[x]==x:
        return x
    parents[x] = find(parents[x])
    return parents[x]

def union(a,b):
    a = find(a)
    b = find(b)

    if a>b:
        parents[a] = b
    else:
        parents[b] = a

# N개의 컴퓨터 네트워크.
# 회선은 성능차이가 있음.
N,M = map(int,input().split())
sercuits = []
parents = [i for i in range(N+1)]
for _ in range(M):
    A,B,C = map(int,input().split())
    sercuits.append([C,A,B])

sercuits.sort(reverse=True)

cnt=0
restore_line=[]
while sercuits:
    time,a,b = sercuits.pop()

    if find(a) != find(b):
        union(a,b)
        cnt+=1
        restore_line.append([a,b])

print(cnt)
for line in restore_line:
    print(*line)