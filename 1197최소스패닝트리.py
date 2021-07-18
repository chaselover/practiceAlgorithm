import sys

input = sys.stdin.readline
V, S = map(int, input().split())

# s크루스칼 알고리즘은 sort를 써야하므로 간선 list안에 튜플을 담아준다.
edge = []
for _ in range(S):
    a, b, w = map(int, input().split())
    edge.append((w, a, b))
# 간선을 에 따라 오름차순 정렬
edge.sort(key=lambda x: x[0])

# 부모노드를 각 노드idx에 맞춰 생성, 매칭해준다.
parent = list(range(V + 1))

# union 알고리즘 구현 각 노드가 속한 집합의 대푯값(루트노드)을 구하고 합쳐준다.
def union(a, b):
    a = find(a)
    b = find(b)

    if b < a:
        parent[a] = b
    else:
        parent[b] = a

# 루트노드를 찾기위해 재귀로 찾아준다.
def find(a):
    if a == parent[a]:
        return a
    parent[a] = find(parent[a])  # 경로 압축
    return parent[a]

# 간선을 가중치 낮은것부터 하나씩 꺼내 둘이 다른 집합이라면 MST집합에 이어주고 가중치 값을 더해준다.
sum = 0
for w, s, e in edge:
    if find(s) != find(e):
        union(s, e)
        sum += w

print(sum)