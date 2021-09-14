import sys
input = sys.stdin.readline

def dfs(v,arr):
    if len(arr)==K:
        for num in arr:
            print(num)
        exit()
    for i in range(v+1,N+1):
        if not visited[i]:
            for num in arr:
                if num not in graph[i]:
                    break
            else:
                visited[i] = True
                dfs(i,arr+[i])



K, N, F = map(int, input().split())
graph = {i: [] for i in range(1,N+1)}
for _ in range(F):
    a, b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]

for i in range(1,N+1):
    visited = {i: False for i in range(1,N+1)}
    visited[i] = True
    dfs(i,[i])

print(-1)