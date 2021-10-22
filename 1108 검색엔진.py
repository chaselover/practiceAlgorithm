import sys
sys.setrecursionlimit(10 ** 9)


def dfs1(n):
    visited[n] = True
    for v in forward[n]:
        if not visited[v]:
            dfs1(v)
    stack.append(n)


def dfs2(n):
    visited[n] = idx
    for i in range(len(backward[n]) - 1, -1, -1):
        v = backward[n][i]
        if visited[v] == -1:
            forward[v].remove(n)
            dfs2(v)
        elif visited[v] == idx:
            forward[v].remove(n)
    tmp.append(n)


def dfs(n):
    for v in forward[n]:
        if dp[v] == 1:
            dp[n] += dfs(v)
        else:
            dp[n] += dp[v]
    return dp[n]


N = int(sys.stdin.readline())
forward = [[] for _ in range(N)]
backward = [[] for _ in range(N)]
data = [sys.stdin.readline().split() for _ in range(N)]
alpha = dict()
idx = N
for i in range(N):
    alpha[data[i][0]] = i
for i in range(N):
    for j in range(2, len(data[i])):
        if data[i][j] not in alpha:
            alpha[data[i][j]] = idx
            idx += 1
            forward.append([])
            backward.append([])
        forward[i].append(alpha[data[i][j]])
        backward[alpha[data[i][j]]].append(i)
N = idx
visited = [False] * N
stack = []
for i in range(N):
    if not visited[i]:
        dfs1(i)
visited = [-1] * N
idx = 0
ans = []
target = alpha[sys.stdin.readline().rstrip()]
while stack:
    cur = stack.pop()
    if visited[cur] == -1:
        tmp = []
        dfs2(cur)
        ans.append(tmp)
        idx += 1
dp = [1] * N
print(dfs(target))