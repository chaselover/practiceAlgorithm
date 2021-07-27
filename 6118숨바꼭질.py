import sys
input = sys.stdin.readline
from collections import deque

def BFS(start):
    queue = deque()
    queue.append(start)
    dp_dists[start] = 0
    while queue:
        cur_node = queue.popleft()
        for next_node in graph[cur_node]:
            if dp_dists[next_node]==-1:
                dp_dists[next_node] = dp_dists[cur_node] + 1
                queue.append(next_node)

# 헛간 N개
# 모든 헛간은 M개의 양방향 길.
# 1번 헛간에서 거리(가장 멀리있는)노드.

N,M = map(int,input().split())
graph = {i:[] for i in range(1,N+1)}
dp_dists = {i:-1 for i in range(1,N+1)}
for _ in range(M):
    a,b = map(int,input().split())
    graph[a] += [b]
    graph[b] += [a]

# 1부터 bfs방문한곳은 안들르고 dp하나씩 늘려가며.
BFS(1)

max_dists = 0
for dist in dp_dists:
    if max_dists and max_dists==dp_dists[dist]:
        cnt+=1
    if dp_dists[dist] > max_dists:
        max_dists = dp_dists[dist]
        max_node = dist
        cnt=1


print(max_node,max_dists,cnt)