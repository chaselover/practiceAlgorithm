import sys
input = sys.stdin.readline

N = int(input())
nodes = set([i for i in range(N)])
childs = {i: [] for i in range(-1,N)}
parents = list(map(int, input().split()))
for i in range(N):
    childs[parents[i]].append(i)
parent_node = set(parents)
leafs = nodes - parent_node
q = [int(input())]
while q:
    x = q.pop()
    if not childs[x]:
        leafs -= {x}
    for child in childs[x]:
        q.append(child)
print(len(leafs))