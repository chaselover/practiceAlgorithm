# import sys
# input = sys.stdin.readline
# from collections import deque


# # 왜? BFS로 안풀림?
# def BFS(start):
#     q = deque()
#     q.append(start)
#     visited[start] = 0
#     while q:
#         cur_node = q.popleft()
#         for next_node in graph[cur_node]:
#             if not visited[next_node]:
#                 visited[next_node]=visited[cur_node]+1
#                 q.append(next_node)

# N = int(input())
# graph = {i: [] for i in range(1,N+1)}
# level = {i: 0 for i in range(1,N+1)}
# visited = {i: 0 for i in range(1,N+1)}
# for _ in range(N-1):
#     a, b = map(int, input().split())
#     graph[a] += [b]
#     graph[b] += [a]
#     level[a] += 1
#     level[b] += 1

# BFS(1)

# leaf_dist_cost = 0
# for node in range(2,N+1):
#     if level[node]==1:
#         leaf_dist_cost += visited[node]

# print("YES" if leaf_dist_cost&1 else "NO")



'''
[리프노드-루트노드까지의 거리]의 총 합이 홀수냐 짝수냐를 묻는 문제...인가?
'''
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graphs = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graphs[a].append(b)
    graphs[b].append(a)

q = deque()
# 노드번호, 거리
q.append([1,0])
visited = [0] * (N+1)
visited[1] = 1

answer = 0
while q:
    cur, dist = q.popleft()
    # 리프 여부 체크
    flag = True
    for next in graphs[cur]:
        if not visited[next]:
            q.append([next, dist+1])
            visited[next] = 1
            flag = False
    if flag:
        answer += dist

if answer%2:
    print('Yes')
else:
    print('No')