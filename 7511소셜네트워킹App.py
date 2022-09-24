import sys
input = sys.stdin.readline

def union(a,b): #집합이 다를경우 합침
    a=find(a)
    b=find(b)
    if a<b: parent[b]=a
    else: parent[a]=b

def find(x): # 루트 노드를 찾아감
    if parent[x]==x:
        return x
    parent[x]=find(parent[x])
    return parent[x]

T = int(input())
for test in range(1,T+1): #case수 반복.
    n=int(input())
    k=int(input())
    parent = {i:i for i in range(n)} # initialize 자기가 루트노드
    for _ in range(k): # 루트노드가 다르면 union으로 tree병합
        a,b = map(int,input().split())
        if find(a)!=find(b):
            union(a,b)
    m=int(input())
    print(f'Scenario {test}:')
    for _ in range(m): # u랑v랑 집합 같으면 1, 틀리면 0출력.
        u,v = map(int,input().split())
        # 경로 압축 한다고 해서 rank가 바로 2가 되는건 아니다.
        if find(u)==find(v):
            print(1)
        else:
            print(0)
    print()