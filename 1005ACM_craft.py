import sys
input = sys.stdin.readline
from collections import deque

def topological_sorting():
    queue = deque()
    for i in range(1,N+1):
        if not level[i]:
            queue.append(i)
            dp_times[i] = times[i-1]
    while queue:
        cur_node = queue.popleft()
        if cur_node == W:
            return
        for next_node in graph[cur_node]:
            dp_times[next_node] = max(dp_times[cur_node]+times[next_node-1],dp_times[next_node])
            level[next_node] -= 1
            if not level[next_node]:
                queue.append(next_node)

# 위상정렬
T = int(input())
for test in range(T):
    N,K = map(int,input().split())
    times = list(map(int,input().split()))
    graph = {i:[] for i in range(1,N+1)}
    level = {i:0 for i in range(1,N+1)}
    dp_times = {i:0 for i in range(1,N+1)}
    for _ in range(K):
        X,Y = map(int,input().split())
        graph[X] += [Y]
        level[Y] += 1
    W = int(input())

    topological_sorting()

    print(dp_times[W])