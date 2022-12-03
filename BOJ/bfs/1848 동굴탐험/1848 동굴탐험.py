import sys
import heapq
input = sys.stdin.readline

def dijkstra(bit):
	q = []
	for l in lnk:
		node, _in, _ = l
		if node & (1 << bit):
			heapq.heappush(q, (_in, node))
			dis[node] = _in
	
	while q:
		d, u = heapq.heappop(q)
		if dis[u] < d:
			continue
		for v, w in graph[u]:
			if dis[v] > d + w:
				dis[v] = d + w
				heapq.heappush(q, (dis[v], v))

def dijkstra2(bit):
	q = []
	for l in lnk:
		node, _in, _ = l
		if not (node & (1 << bit)):
			heapq.heappush(q, (_in, node))
			dis[node] = _in
	
	while q:
		d, u = heapq.heappop(q)
		if dis[u] < d:
			continue
		for v, w in graph[u]:
			if dis[v] > d + w:
				dis[v] = d + w
				heapq.heappush(q, (dis[v], v))
		
if __name__ == '__main__':
	n, m = map(int, input().split())
	graph = [[] for _ in range(n+1)]
	lnk = []
	for _ in range(m):
		a, b, c, d = map(int, input().split())

		if a != 1 and b != 1:
			graph[a].append((b, c))
			graph[b].append((a, d))
		
		if a == 1 and b != 1:
			lnk.append((b, c, d)) # (node, in, out)
		if a != 1 and b == 1:
			lnk.append((a, d, c))
		
	ans = float('inf')
	for i in range(13):
		dis = [float('inf') for _ in range(n+1)]
		dijkstra(i)
		for l in lnk:
			node, _, _out = l
			if not (node & (1 << i)):
				ans = min(ans, _out + dis[node])
		
		dis = [float('inf') for _ in range(n+1)]
		dijkstra2(i)
		for l in lnk:
			node, _, _out = l
			if node & (1 << i):
				ans = min(ans, _out + dis[node])
	
	print(ans)