import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def dfs(cur_node, pre_node):
    global ans
    max_d = 0
    for next_node in graph[cur_node]:
        if next_node != pre_node:
            max_d = max(max_d,dfs(next_node, cur_node))
    if max_d >= D:
        ans += 1
    return max_d + 1


N, S, D = map(int, input().split())
graph = {i: [] for i in range(1,N+1)}
visited = [0] * (N+1)
ans = 0
for _ in range(N-1):
    x, y = map(int, input().split())
    graph[x] += [y]
    graph[y] += [x]
dfs(S, 0)
print(2*(ans-1) if ans else 0)
