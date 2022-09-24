import sys
input = sys.stdin.readline
from heapq import heappop,heappush

def kruskal():
    answer = 0
    while dists:
        ab_dists,star_a,star_b = heappop(dists)

        if find(star_a) !=find(star_b):
            answer += ab_dists
            union(star_a,star_b)
    return answer

def union(a,b):
    a = find(a)
    b = find(b)

    if a>b:
        parent[b] = a
    else:
        parent[a] = b

def find(x):
    if parent[x] ==x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

n=int(input())
# 거리가 최소가 되는 비용.
# 점을 다 연결한다.-> 간선 N-1 -> MST
matrix = [list(map(float,input().split())) for _ in range(n)]
parent = [i for i in range(n)]
dists = []
for i in range(n):
    for j in range(n):
        if i != j:
            heappush(dists,[round(((matrix[i][0] - matrix[j][0])**2 + (matrix[i][1] - matrix[j][1])**2)**0.5,2),i,j])


min_star_set = kruskal()

print(min_star_set)