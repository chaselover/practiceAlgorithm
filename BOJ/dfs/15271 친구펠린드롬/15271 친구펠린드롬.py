import sys
input = sys.stdin.readline
n, m = map(int, input().split())
path = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    if (a + b) % 2:
        path[a].append(b)
        path[b].append(a)

match = [-1]*(n+1)
def dfs(n):
    if n == -1:
        return 2
    for j in path[n]:
        if avail[j]:
            avail[j] = False
            if dfs(match[j]):
                match[j] = n
                return 2
    return 0

ans = 0
for i in range(1, n+1, 2):
    avail = [True] * (n + 1)
    ans += dfs(i)

if ans != n:
    ans += 1
print(ans)



# 2
from sys import setrecursionlimit as SRL
SRL(15000)
from collections import deque
def BFS(ssize, tsize, adj, pairu, pairv, dist):
    Q = deque()
    for u in range(1, ssize+1):
        if pairu[u] == 0: dist[u] = 0; Q.append(u)
        else: dist[u] = float('inf')
    dist[0] = float('inf')
    while len(Q) > 0:
        u = Q.popleft()
        if dist[u] >= dist[0]: continue
        for v in adj[u]:
            if dist[pairv[v]] == float('inf'):
                dist[pairv[v]] = dist[u] + 1
                Q.append(pairv[v])
    return dist[0] != float('inf')

def DFS(ssize, tsize, adj, pairu, pairv, dist, u):
    if u == 0: return True
    for v in adj[u]:
        if dist[pairv[v]] == dist[u] + 1 and DFS(ssize, tsize, adj, pairu, pairv, dist, pairv[v]):
            pairv[v] = u; pairu[u] = v; return True
    dist[u] = float('inf'); return False

def HopcroftKarp(ssize, tsize, adj):
    pairu = [0]*(ssize+1); pairv = [0]*(tsize+1); dist = [-1]*(ssize+1)
    match = 0
    while BFS(ssize, tsize, adj, pairu, pairv, dist):
        for u in range(1, ssize+1):
            if pairu[u] == 0: match+= DFS(ssize, tsize, adj, pairu, pairv, dist, u)
    return match

from sys import stdin
input = stdin.readline
n, m = map(int,input().split())
adj = [[] for i in range(n+1)]
for i in range(m):
    a, b = map(int,input().split())
    if a%2 == b%2: continue
    if a%2: a,b = b,a
    adj[a].append(b)
match = HopcroftKarp(n, n, adj)
print(min(2*match+1, n))