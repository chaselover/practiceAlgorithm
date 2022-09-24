import sys
input = sys.stdin.readline
from collections import deque

def bfs(x, adj):
	rtn = 0
	q = deque()
	q.append(x)
	visited[x] = True
	while q:
		v = q.popleft()
		for n in adj[v]:
			if not visited[n]:
				q.append(n)
				visited[n] = True
				rtn += 1
	return rtn

N, M, X = map(int, input().split())
higher = [[] for _ in range(N+1)]
lower = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(M):
	A, B = map(int, input().split())

	# A보다 큰 학생들
	higher[A].append(B)
	# B보다 작은 학생들
	lower[B].append(A)

print(1+bfs(X, lower), N-bfs(X, higher))