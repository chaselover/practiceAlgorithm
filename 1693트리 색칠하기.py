import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def dfs(idx):
    for i in s[idx]:
        if not visit[i]:
            visit[i] = True
            dfs(i)
            for j in range(1, 17):
                m_num = 100000000
                for k in range(1, 17):
                    if j != k:
                        if m_num > dp[i][k]:
                            m_num = dp[i][k]
                dp[idx][j] += m_num
    for i in range(1, 17):
        dp[idx][i] += i
    return


n = int(input())
s = [[] for i in range(n + 1)]
dp = [[0] * 17 for i in range(n + 1)]
visit = [False for i in range(n + 1)]

for i in range(n - 1):
    a, b = map(int, input().split())
    s[a].append(b)
    s[b].append(a)
visit[1] = True
dfs(1)
print(min(dp[1][1:]))



# 진한님 풀이.
from sys import setrecursionlimit as SRL, stdin
input = stdin.readline
#range = xrange

n = int(input())
MAXC = 18
adj = [[] for i in range(n+1)]
tadj = [[] for i in range(n+1)]
for i in range(n-1):
    a, b = map(int,input().split())
    adj[a].append(b)
    adj[b].append(a)
    
from collections import deque
Q = deque(); Q.append(1)
visit = [False]*(n+1); visit[1] = True
order = []
while len(Q):
    p = Q.popleft()
    for q in adj[p]:
        if visit[q]: continue
        visit[q] = True
        tadj[p].append(q)
        Q.append(q)
    order.append(p)

opt = [[float('inf')]*MAXC for i in range(n+1)]
for p in reversed(order):
    if not tadj[p]:
        for c in range(1, MAXC): opt[p][c] = c
        continue
    for c in range(1, MAXC):
        res = c
        for q in tadj[p]:
            res+= min(opt[q][j] for j in range(1, MAXC) if j != c)
        opt[p][c] = res
print(min(opt[1]))



# 다른분 풀이
import collections as c
import math
d=c.defaultdict(set)
n=int(input())
o=int(math.log2(n)+1)
for i in range(n-1):
	x,y=map(int,input().split())
	d[x].add(y)
	d[y].add(x)
s=c.deque([(1,0)])
e={}
def m(l):
	a=b=0
	p=q=9**9
	for i,v in enumerate(l):
		if v<p:a,p,b,q=i,v,a,p
		elif v<q:b,q=i,v
	return a,p,b,q
while s:
	r,p=s[-1]
	k=d[r]-{p}
	l=set()
	if r not in e:e[r]=list(range(1,o+1))
	for i in k:
		if i not in e:
			s.append((i,r))
			break
		else:
			a,p,b,q=m(e[i])
			for j in range(o):
				e[r][j]+=p if a!=j else q
			l.add(i)
			del e[i]
	else:
		s.pop()
	d[r]=k-l
print(min(e[1]))