import sys
input = sys.stdin.readline

N,M = map(int,input().split())
graph = [[float('inf') for _ in range(N)] for _ in range(N)]

for i in range(M):
    a,b = map(int,input().split())
    graph[a-1][b-1] = 2
    graph[b-1][a-1] = 2

for i in range(N):
    graph[i][i] = 0

for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][j] >graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

max_time = float('inf')

for i in range(N-1):
    for j in range(i,N):
        chicken1 = i
        chicken2 = j
        sum_time = 0
        for building in range(N):
            sum_time += min(graph[building][chicken1],graph[building][chicken2])
        if max_time > sum_time:
            max_time = sum_time
            max_chicken1 = chicken1
            max_chicken2 = chicken2

print(max_chicken1+1, max_chicken2+1, max_time)