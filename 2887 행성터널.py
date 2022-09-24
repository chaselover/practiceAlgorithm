import sys
input = sys.stdin.readline
from heapq import heappop,heappush

def kruskal():
    min_dists = 0
    while dists:
        dist,a,b = heappop(dists)
        if find(a) != find(b):
            union(a,b)
            min_dists+=dist
    return min_dists

def find(x):
    if parents[x] == x:
        return x
    parents[x] = find(parents[x])
    return parents[x]

def union(a,b):
    a = find(a)
    b = find(b)

    if a<b:
        parents[b] = a
    else:
        parents[a] = b

# MST
N = int(input())
matrix = [list(map(int,input().split())) + [i] for i in range(N)]
parents =[i for i in range(N)]
dists = []
# 좌표별로 정렬해서 가장 가까운 하나씩만 계산하고 버린다.(index0은 1이랑 1은 2랑..해서 좌표당 N-1개씩 *3 
# 3(N-1)간선만 딱 계산하고 버림.)
# 결국 거리계산에서 N^2연산을 쳐내는게 중요.
# 시간복잡도는 결국 가장 연산이 큰걸따라감.
for i in range(3):
    matrix.sort(key=lambda x:x[i])
    for j in range(1,N):
        heappush(dists,[abs(matrix[j-1][i]-matrix[j][i]),matrix[j-1][3],matrix[j][3]])

answer = kruskal()

print(answer)