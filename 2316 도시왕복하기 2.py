import sys
input=sys.stdin.readline
n,p=map(int,input().split())
adj=[[] for _ in range(2*n)]
for i in range(n):
  adj[2*i+1].append(2*i)
for _ in range(p):
  i,j=map(int,input().split())
  adj[2*i-2].append(2*j-1)
  adj[2*j-2].append(2*i-1)
def dfs(i):
  global found,cnt
  if i==3:
    for k in range(len(path)-1):
      u,v=path[k],path[k+1]
      adj[u].remove(v)
      adj[v].append(u)
    found=1
    cnt+=1
    return
  for j in adj[i]:
    if found:
      break
    if not visit[j]:
      visit[j]=1
      path.append(j)
      dfs(j)
      path.pop()
cnt=0
while 1:
  found=0
  visit=[1]+[0]*(2*n-1)
  path=[0]
  dfs(0)
  if not found:
    break
print(cnt)



# 3
import sys


def dfs(cur):
    if cur == 2:
        return 1
    
    for nxt in range(2, 2 * n + 1):
        if graph[cur][nxt] and not visit[nxt]:            
            visit[nxt] = 1
            if dfs(nxt):
                graph[cur][nxt] -= 1
                graph[nxt][cur] += 1
                return 1
    
    return 0


n, m = map(int, sys.stdin.readline().split())
graph = [[0] * (2 * n + 1) for _ in range(2 * n + 1)]

for i in range(1, n + 1):
    graph[i][i + n] = 1

for _ in range(m):
    start, end = map(int, sys.stdin.readline().split())
    graph[start + n][end] += 1
    graph[end + n][start] += 1

ans = 0
flow = 1
while flow:
    visit = [0] * (2 * n + 1)
    flow = dfs(1 + n)
    ans += flow

print(ans)


# 4
from collections import deque
import sys
input = sys.stdin.readline
n, p = map(int, input().split())
C = [[0] * (2 * n) for _ in range(2 * n)]
F = [[0] * (2 * n) for _ in range(2 * n)]
graph = [[] for _ in range(2*n)]

for i in range(p):
    a, b = map(int, input().split())
    a = (a - 1) * 2 + 1
    b = (b - 1) * 2
    C[a][b] = 1
    graph[a].append(b)
    graph[b].append(a)
    C[b+1][a-1] = 1
    graph[b+1].append(a-1)
    graph[a-1].append(b+1)
for i in range(n):
    a, b = i * 2, i * 2 + 1
    C[a][b] = 1
    graph[a].append(b)
    graph[b].append(a)

def dfs(u, limit):
    if limit <= 0:
        return 0
    if u == E:
        return limit
    val = 0
    for v in graph[u]:
        res = C[u][v] - F[u][v]
        if level[v] == level[u] + 1 and res > 0:
            flow = dfs(v, min(limit - val, res))
            F[u][v] += flow
            F[v][u] -= flow
            val += flow
    if val == 0:
        level[u] -= 1
    return val

S, E = 1, 2
total = 0
while True:
    Q = deque([S])
    level = [-1] * len(graph)
    level[S] = 0
    while Q:
        u = Q.popleft()
        for v in graph[u]:
            if level[v] == -1 and C[u][v] > F[u][v]:
                level[v] = level[u] + 1
                Q.append(v)
    if level[E] == -1:
        break
    total += dfs(S, sum(C[S][v] for v in graph[S]))
print(total)


# Dinic algorithm but with very sparse graphs
# adj = list of adjacent nodes, must be made bidirectional
# C = capacity dict
# s = index of source
# t = index of sink

from collections import deque, defaultdict
def Dinic(G, C, s, t):
    def send(u, limit):
        if limit <= 0: return 0
        if u == t: return limit
        val = 0
        for v in G[u]:
            res = C[(u,v)]-flow[(u,v)]
            if level[v] == level[u]+1 and res>0:
                a = send(v, min(limit-val, res))
                flow[(u,v)]+= a; flow[(v,u)]-= a; val+= a
        if val == 0: level[u]-= 1
        return val
    Q, tot, n, flow = deque(), 0, len(G), defaultdict(int)
    while 1:
        Q.append(s); level = [-1]*n; level[s] = 0
        while len(Q) > 0:
            u = Q.popleft()
            for v in G[u]:
                if level[v] == -1 and C[(u,v)] > flow[(u,v)]: level[v] = level[u]+1; Q.append(v)
        if level[t] == -1: return tot#, flow
        tot+= send(s, sum(C[(s,v)] for v in G[s]))

def addedge(i, j, cap):
    G[i].append(j); G[j].append(i); C[(i,j)]+= cap

# 0 ~ n-1: vertex in
# n ~ 2n-1: vertex out
from sys import stdin
input = stdin.readline
n, p = map(int,input().split())
G = [[] for i in range(2*n)]
C = defaultdict(int)

for i in range(n): addedge(i, i+n, 1)
for i in range(p):
    a, b = sorted(map(int,input().split()))
    addedge(a+n-1, b-1, 1)
    addedge(b+n-1, a-1, 1)
print(Dinic(G, C, n, 1))


# 5
INF = float("inf")


class Dinic:
    def __init__(self, n):
        self.lvl = [0] * n
        self.ptr = [0] * n
        self.q = [0] * n
        self.adj = [[] for _ in range(n)]

    def add_edge(self, a, b, c, rcap=0):
        self.adj[a].append([b, len(self.adj[b]), c, 0])
        self.adj[b].append([a, len(self.adj[a]) - 1, rcap, 0])

    def dfs(self, v, t, f):
        if v == t or not f:
            return f

        for i in range(self.ptr[v], len(self.adj[v])):
            e = self.adj[v][i]
            if self.lvl[e[0]] == self.lvl[v] + 1:
                p = self.dfs(e[0], t, min(f, e[2] - e[3]))
                if p:
                    self.adj[v][i][3] += p
                    self.adj[e[0]][e[1]][3] -= p
                    return p
            self.ptr[v] += 1

        return 0

    def calc(self, s, t):
        flow, self.q[0] = 0, s
        for l in range(31):  # l = 30 maybe faster for random data
            while True:
                self.lvl, self.ptr = [0] * len(self.q), [0] * len(self.q)
                qi, qe, self.lvl[s] = 0, 1, 1
                while qi < qe and not self.lvl[t]:
                    v = self.q[qi]
                    qi += 1
                    for e in self.adj[v]:
                        if not self.lvl[e[0]] and (e[2] - e[3]) >> (30 - l):
                            self.q[qe] = e[0]
                            qe += 1
                            self.lvl[e[0]] = self.lvl[v] + 1

                p = self.dfs(s, t, INF)
                while p:
                    flow += p
                    p = self.dfs(s, t, INF)

                if not self.lvl[t]:
                    break

        return flow


N,P = map(int,input().split())
flow = Dinic(2 * N - 2)
for i in range(2,N):
    flow.add_edge(i, i + N - 2, 1)
for _ in range(P):
    a,b = map(int,input().split())
    aNew = a + (N - 2) * (a != 1 and a != 2)
    aNew -= 1
    bNew = b + (N - 2) * (b != 1 and b != 2)
    bNew -= 1
    flow.add_edge(aNew, b - 1, 1)
    flow.add_edge(bNew, a - 1, 1)
print(flow.calc(0, 1))


# 6
from collections import deque
from sys import stdin, stdout

N, P = map(int, stdin.readline().split())
adj = [set() for _ in range(1+N*2)]
fn = [[0] * (1+N*2) for _ in range(1+N*2)]
cn = [[0] * (1+N*2) for _ in range(1+N*2)]

for i in range(1, 1+N):
    adj[i+N].add(i)
    cn[i+N][i] += 1
    adj[i].add(i+N)
    cn[i][i+N] += 0
cn[2+N][2] += P


def flow(prev):
    route = [2]
    flow = 1
    while 1:
        now = route[-1]
        pre = prev[now]
        flow = min(flow, cn[pre][now] - fn[pre][now])
        route.append(pre)
        if pre == 1:
            break
    while route:
        now = route.pop()
        nxt = route[-1]
        fn[now][nxt] += flow
        fn[nxt][now] -= flow
        if now % N != nxt % N:
            if now > N:
                fn[now-N][nxt+N] += flow
                fn[nxt+N][now-N] -= flow
            else:
                fn[now+N][nxt-N] += flow
                fn[nxt-N][now+N] -= flow
        if nxt == 2:
            break
    return flow


def bfs():
    queue = deque()
    queue.append(1)
    prev = [-1]*(1+N*2)
    while queue:
        now = queue.popleft()
        for nxt in adj[now]:
            if cn[now][nxt] > fn[now][nxt] and prev[nxt] == -1:
                prev[nxt] = now
                queue.append(nxt)
                if nxt == 2:
                    ans = flow(prev)
                    return ans
    return 0


for _ in range(P):
    a, b = map(int, stdin.readline().split())
    cn[a][b+N] += 1
    adj[a].add(b+N)
    cn[b][a+N] += 1
    adj[b].add(a+N)

    cn[a+N][b] += 0
    adj[a+N].add(b)
    cn[b+N][a] += 0
    adj[b+N].add(a)


total = 0
while 1:
    temp = bfs()
    if temp == 0:
        break
    total += temp

stdout.write(f"{total}")