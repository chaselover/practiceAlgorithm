import sys
input = sys.stdin.readline


N, M = map(int, input().split())
frog_favor_topic = {i: [0] + list(map(int, input().split())) for i in range(1,N+1)}
favor_leaf = {i: list(map(int,input().split())) for i in range(1, N+1)}
graph = {i:[] for i in range(1, N+1)}
visited_leaf = {i: 0 for i in range(1,N+1)}
choosed_flog = {i: False for i in range(1,N+1)}
for _ in range(M):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))