import sys
input = sys.stdin.readline

def floid_washal():
    dp_dists = [[float('inf') for _ in range(n+1)] for _ in range(n+1)]
    for cur_node in graph:
        for next_node,dist in graph[cur_node]:
            if dp_dists[cur_node][next_node] > dist:
                dp_dists[cur_node][next_node] = dist
                dp_dists[cur_node][cur_node] = 0

    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                dp_dists[i][j] = min(dp_dists[i][j],dp_dists[i][k]+dp_dists[k][j])
    
    for i in range(1,n+1):
        for j in range(1,n+1):
            if dp_dists[i][j] == float('inf'):
                print(0, end=' ')
            else:
                print(dp_dists[i][j], end=' ')
        print()

n = int(input())
m = int(input())
graph = {i:[] for i in range(1,n+1)}
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append([b,c])

floid_washal()