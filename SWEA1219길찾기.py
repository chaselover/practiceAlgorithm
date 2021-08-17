import sys
sys.stdin = open('input.txt')


def dfs(v):
    if v == 99:
        return True
    for u in graph[v]:
        if not visited[u]:
            visited[u] = True
            if dfs(u):
                return True


for _ in range(10):
    test, edge_n = map(int, input().split())
    graph = {i: [] for i in range(100)}
    edge_set = list(map(int, input().split()))
    visited = {i: False for i in range(100)}
    for i in range(0, edge_n*2, 2):
        graph[edge_set[i]] += [edge_set[i+1]]
    print(f'#{test}', end=' ')
    visited[0] = True
    print(1 if dfs(0) else 0)
