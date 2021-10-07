# import sys

# lines = sys.stdin.readlines()
# e = []
# for line in lines:
#     line = line.rstrip()
#     if line: e.append(tuple(map(int,line.split())))

# n = len(e)+1
# adj = [[] for i in range(n+1)]
# for a,b,w in e:
#     adj[a].append((b,w))
#     adj[b].append((a,w))

# max_u, max_w = 0,0
# visit = [False]*(n+1)
# S = [(1,0)]
# visit[1]=True
# while S:
#     next_node,w = S.pop()
#     if w>max_w: max_u=next_node; max_w=w
#     for v,dw in adj[next_node]:
#         if not visit[v]:
#             S.append((v,w+dw))
#             visit[v]=True

# visit = [False]*(n+1)
# S = [(max_u,0)]
# visit[max_u]=True
# max_u, max_w = 0,0
# while S:
#     next_node,w = S.pop()
#     if w>max_w: max_u=next_node; max_w=w
#     for v,dw in adj[next_node]:
#         if not visit[v]:
#             S.append((v,w+dw))
#             visit[v]=True
# print(max_w)


# # 다익스트라
# import heapq
# import sys

# si = sys.stdin.readline
# INF = 987654321


# def get_max_value():
#     ret = 0
#     for node in node_list:
#         if ret < distance[node]:
#             ret = distance[node]
#     return ret


# def dijkstra(start):
#     q = []
#     distance[start] = 0
#     heapq.heappush(q, (0, start))
#     while q:
#         dist, now = heapq.heappop(q)

#         if distance[now] < dist:
#             continue

#         for j in graph[now]:
#             nxt = j[0]
#             cost = dist + j[1]
#             if distance[nxt] > cost:
#                 distance[nxt] = cost
#                 heapq.heappush(q, (cost, nxt))


# graph = [[] for _ in range(10001)]
# distance = [INF] * 10001
# node_list = set()

# while True:
#     try:
#         a, b, c = map(int, si().split(" "))
#         graph[a].append((b, c))
#         graph[b].append((a, c))
#         node_list.add(a)
#         node_list.add(b)
#     except:
#         break

# dijkstra(1)
# ret = 0
# start = 0
# for node in node_list:
#     if ret < distance[node]:
#         start = node
#         ret = distance[node]

# distance = [INF] * 10001
# dijkstra(start)
# print(get_max_value())



# # bfs
from collections import deque
import sys
tree = [[] for _ in range(10001)]

for line in sys.stdin:
    splitted = line.split()
    if len(splitted) != 3:
        break
    a, b, c = map(int, splitted)
    tree[a].append((b, c))
    tree[b].append((a, c))

def find_farthest(node):
    q = deque([(node, 0)])  # node and weight
    visited = [False for _ in range(10001)]
    visited[node] = True
    max_node, max_weight = node, 0
    while q:
        cur, cur_weight = q.popleft()
        if max_weight < cur_weight:
            max_node, max_weight = cur, cur_weight
        for nxt, weight in tree[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                nxt_weight = cur_weight + weight
                q.append((nxt, nxt_weight))
    return max_node, max_weight

anchor_node, _ = find_farthest(1)
_, farthest_distance = find_farthest(anchor_node)
print(farthest_distance)


# 간단한 bfs
import sys
input = sys.stdin.readline
from collections import deque

def bfs(start):
    q = deque()
    q.append((start, 0))
    visited = [False for __ in range(10001)]
    visited[start] = True
    max_dist = 0
    target_node = 0
    while q:
        cur_node, cur_dist = q.popleft()
        for next_node, next_dist in graph[cur_node]:
            if visited[next_node]: 
                continue
            visited[next_node] = True
            dist = next_dist + cur_dist
            if dist > max_dist:
                max_dist, target_node = dist, next_node
            q.append((next_node, dist))
    return (target_node, max_dist)


edges = []
while 1:
    try:
        a, b, c = map(int, input().split())
        edges.append((a, b, c))
    except: 
        break
n = len(edges)
graph = {i: [] for i in range(10001)}
for edge in edges:
    a, b, c = edge
    graph[a].append((b, c))
    graph[b].append((a, c))
print(bfs(bfs(1)[0])[1])