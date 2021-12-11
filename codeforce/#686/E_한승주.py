import sys
input = sys.stdin.readline
from collections import defaultdict
 
def dfs(cur_node, path):
    global answer
    for next_node in graph[cur_node]:
        if next_node not in path:
            answer += 1
            dfs(next_node, path | {next_node})
            

for test in range(int(input())):
    n = int(input())
    graph = defaultdict(list)
    answer = 0
    for _ in range(n):
        u, v = map(int, input().split())
        graph[u] += [v]
        graph[v] += [u]
    for start in range(1, n + 1):
        dfs(start, {start})
    print(answer//2)