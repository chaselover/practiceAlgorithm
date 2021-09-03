import sys
input = sys.stdin.readline

N = int(input())
nodes = set([i for i in range(N)])
childs = {i: [] for i in range(-1,N)}
parents = list(map(int, input().split()))
parent_node = set()
for i in range(N):
    childs[parents[i]].append(i)
    parent_node.add(parents[i])
leafs = nodes - parent_node
del_node = int(input())
q = [del_node]
while q:
    x = q.pop()
    if x in leafs:
        leafs.discard(x)
    for child in childs[x]:
        q.append(child)
print(len(leafs)+1 if parents[del_node] != -1 and len(childs[parents[del_node]])==1 else len(leafs))