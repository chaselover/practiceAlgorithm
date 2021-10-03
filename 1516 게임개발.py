import sys
input = sys.stdin.readline
from collections import deque


def topological_sort():
    visited = {i: False for i in range(1, N + 1)}
    q = deque()
    for node in levels:
        if not levels[node]:
            q.append(node)
            visited[node] = True
    while q:
        cur_node = q.popleft()
        for next_node in next_nodes[cur_node]:
            levels[next_node] -= 1
            if not visited[next_node] and not levels[next_node]:
                visited[next_node] = True
                q.append(next_node)
                max_cost = 0
                for node in pre_nodes[next_node]:
                    if max_cost < costs[node]:
                        max_cost = costs[node]
                costs[next_node] += max_cost

N = int(input())
costs = [0]
next_nodes = {i: [] for i in range(1, N + 1)}
pre_nodes = {}
levels = {i: 0 for i in range(1, N + 1)}
for node in range(1, N + 1):
    command = list(map(int, input().split()))
    costs.append(command[0])
    for pre_node in command[1:-1]:
        next_nodes[pre_node].append(node)
    pre_nodes[node] = command[1:-1]
    levels[node] = len(command) - 2

topological_sort()
for each in costs[1:]:
    print(each)