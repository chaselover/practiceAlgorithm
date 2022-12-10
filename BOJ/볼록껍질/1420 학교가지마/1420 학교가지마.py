import sys
read = sys.stdin.readline
from collections import deque

n, m = map(int, read().split())
board = [read().strip() for _ in range(n)]
dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
frm = [[None for _ in range(m)] for _ in range(n)]
to = [[None for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        if board[i][j] == 'H':
            end = (i, j)
        if board[i][j] == 'K':
            start = (i, j)

if abs(end[0] - start[0]) + abs(end[1] - start[1]) == 1:
    print(-1)
    exit()

def bfs():
    q = deque([(*start, 0)])
    visit = {(*start, 0): None}
    while q:
        cur = q.popleft()
        i, j, k = cur
        if cur[0:2] == end:
            assert k == 0
            while (i, j) != start:
                pi, pj, pk = visit[(i, j, k)]
                if frm[pi][pj] == (i, j):
                    frm[pi][pj] = None
                    if to[i][j] == (pi, pj):
                        to[i][j] = None
                else:
                    to[pi][pj] = (i, j)
                    frm[i][j] = (pi, pj)
                i, j, k = pi, pj, pk
            return True

        if k == 0:
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if not (0 <= ni < n and 0 <= nj < m):
                    continue
                if (ni, nj) == start:
                    continue
                if board[ni][nj] == '#':
                    continue
                if frm[ni][nj] == (i, j):
                    continue
                if to[i][j] == (ni, nj):
                    continue
                if to[ni][nj] and to[ni][nj] != (i, j):
                    if (ni, nj, 1) not in visit:
                        q.append((ni, nj, 1))
                        visit[(ni, nj, 1)] = cur
                else:
                    if (ni, nj, 0) not in visit:
                        q.append((ni, nj, 0))
                        visit[(ni, nj, 0)] = cur
        elif k == 1:
            ni, nj = frm[i][j]
            if (ni, nj, 0) not in visit:
                q.append((ni, nj, 0))
                visit[(ni, nj, 0)] = cur
    return False


count = 0
while bfs():
    count += 1
print(count)


# 2
class queue:
    def __init__(self): self.items = []
    def isEmpty(self): return self.items == []
    def enqueue(self, item): self.items.insert(0,item)
    def dequeue(self): return self.items.pop()

class FlowGraph:
    def __init__(self, n: int) -> None:
        self.n=n
        self.c=[{} for _ in range(n)] # Capacity of each edge
        self.f=[{} for _ in range(n)] # Flow of each edge
        self.adj=[[] for _ in range(n)] # Adjacency list of the graph

    def add_edge(self, u, v, w) -> None: # Add an edge to the graph
        if w == 0 and v in self.adj[u]: return
        self.c[u][v]=w
        self.f[u][v]=0
        self.adj[u].append(v)
        self.__add_edge(v, u, 0)
    
    def __add_edge(self, u, v, w) -> None: # Add an edge to the graph
        if w == 0 and v in self.adj[u]: return
        self.c[u][v]=w
        self.f[u][v]=0
        self.adj[u].append(v)

    def mf(self, s: int, e: int) -> int:
        t=0 # Total Flow
        while True:
            prev=[-1]*self.n
            q=queue()
            q.enqueue(s)
            while not q.isEmpty() and prev[e]==-1:
                u=q.dequeue()
                for v in self.adj[u]:
                    if self.c[u][v]-self.f[u][v]>0 and prev[v]==-1:
                        q.enqueue(v)
                        prev[v]=u
                        if v==e: break
            if prev[e]==-1: break
            flow=float('inf')
            i=e
            while i!=s: 
                flow=min(flow, self.c[prev[i]][i]-self.f[prev[i]][i])
                i=prev[i]
            i=e
            while i!=s: 
                self.f[prev[i]][i]+=flow
                self.f[i][prev[i]]-=flow
                i=prev[i]
            t+=flow
        return t

import sys
input = sys.stdin.readline
n,m=map(int,input().split())
g=FlowGraph(n*m*2+2)
def valid(x,y): return 0<=x<n and 0<=y<m
def inf(): return float('inf')
s=n*m*2
e=n*m*2+1
k,h=[0,0],[0,0]
for i in range(n):
    l=list(input().rstrip())
    for j in range(m):
        if l[j]=='#':
            continue
        if l[j]=='.':
            g.add_edge(m*i+j,n*m+m*i+j,1)
        elif l[j]=='K':
            g.add_edge(m*i+j,n*m+m*i+j,inf())
            g.add_edge(s,m*i+j,inf())
            k=[i,j]
        elif l[j]=='H':
            g.add_edge(m*i+j,n*m+m*i+j,inf())
            g.add_edge(n*m+m*i+j,e,inf())
            h=[i,j]
        if valid(i-1,j):
            g.add_edge(n*m+m*i+j,m*(i-1)+j,inf())
        if valid(i+1,j):
            g.add_edge(n*m+m*i+j,m*(i+1)+j,inf())
        if valid(i,j-1):
            g.add_edge(n*m+m*i+j,m*i+(j-1),inf())
        if valid(i,j+1):
            g.add_edge(n*m+m*i+j,m*i+(j+1),inf())
if (k[0]-h[0]==1 or k[0]-h[0]==-1) and k[1]==h[1]:
    print(-1);sys.exit(0)
if (k[1]-h[1]==1 or k[1]-h[1]==-1) and k[0]==h[0]:
    print(-1);sys.exit(0)
r=g.mf(s,e)
print(r)