from collections import deque

def bfs(node):
    q = deque()
    q.append(node)
    check[node] = 0
    while q:
        node = q.popleft()
        for n in graph[node]:
            if check[n] == -1:
                q.append(n)
                check[n] = check[node]+1

N, K = map(int, input().split())
graph = [[] for _ in range(N+1)]
check = [-1]*(N+1)
for _ in range(K):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
ok = 1
for i in range(1, N+1):
    check = [-1]*(N+1)
    bfs(i)
    if (max(check) > 6) or (-1 in check[1:]):
        ok = 0
        break
print("Small World!" if ok else "Big World!")