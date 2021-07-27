import sys
input = sys.stdin.readline
from heapq import heappop,heappush

def find(a):
    if parents[a] == a:
        return a
    parents[a] = find(parents[a])
    return parents[a]

def union(a,b):
    a = find(a)
    b = find(b)

    if b>a:
        parents[b] = a
    else:
        parents[a] = b
        

# N개의 집 M개의 길(쌍방향) / 마을 분리.
# 나머지 길의 유지비 합 최소 / 마을 2개로 분리,길 최소로.
# 1번은 분리(유니온 파인드에서 마지막 하나만 연결 안하면 됨? ㅇㅇ 됨 )
# 그냥 크루스칼 돌리고 마지막 가중치 긴거 하나만 연결 안하면 됨ok.
N,M = map(int,input().split())
parents = [i for i in range(N+1)]
heap = []
for _ in range(M):
    A,B,C = map(int,input().split())
    heappush(heap,[C,A,B])

total_cost = 0
count = 0
while heap:
    cost,a,b = heappop(heap)
    if find(a) != find(b):
        union(a,b)
        total_cost +=cost
        count+=1
    if count==N-2:
        break
print(total_cost)