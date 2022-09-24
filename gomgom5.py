import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from collections import defaultdict


def dfs(cur_node):
    if not graph[cur_node]:
        return True
    for next_node in graph[cur_node]:
        if next_node in gomgom:
            continue
        if dfs(next_node):
            return True


N, M = map(int, input().split())
graph = defaultdict(set)
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].add(v)
S = int(input())
gomgom = set(map(int, input().split()))
if 1 in gomgom:
    print("Yes")
else:
    print("yes" if dfs(1) else "Yes")