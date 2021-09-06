import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def dfs(v):
    visited[v] = True
    dp[v][1] = citizen[v-1]
    for u in graph[v]:
        if not visited[u]:
            dfs(u)

            dp[v][0] += max(dp[u][0],dp[u][1])
            dp[v][1] += dp[u][0]


N = int(input())
citizen = list(map(int, input().split()))
graph = {i: [] for i in range(1,N+1)}
visited = {i: False for i in range(1,N+1)}
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dp = [[0,0] for _ in range(N+1)]
dfs(1)
print(max(dp[1][0],dp[1][1]))