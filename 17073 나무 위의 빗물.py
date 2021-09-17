import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(cur_node, water):
    visited[cur_node] = True
    n = len(tree[cur_node])-1
    if not n:
        ans.append(water)
        return
    unit = water/n
    for next_node in tree[cur_node]:
        if not visited[next_node]:
            dfs(next_node,unit)


N, W = map(int, input().split())
tree = {i: [] for i in range(1, N+1)}
visited = {i: False for i in range(1, N+1)}
ans = []
for _ in range(N-1):
    U, V = map(int, input().split())
    tree[U] += [V]
    tree[V] += [U]
visited[1] = True
for next_node in tree[1]:
    dfs(next_node, W/len(tree[1]))
print(sum(ans)/len(ans))
# 리프노드들에 고인 물의 평균. 노드수 50만. 