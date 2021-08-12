import sys
input = sys.stdin.rewadline

def DFS(v,cnt):
    for next_node in graph[v]:
        if not visited[next_node]:
            visited[next_node] = True
            cnt = DFS(next_node,cnt+1)
    return cnt

for test in range(1, int(input())+1):
    N, M = map(int, input().split())
    graph = {i:[] for i in range(1, N+1)}
    visited = {i:False for i in range(1, N+1)}
    for _ in range(M):
        a, b = map(int,input().split())
        graph[a] += [b]
        graph[b] += [a]
    
    answer = DFS(1,0)
    print(answer)

    # 사실 연결그래프라 최소갯수는 n-1 최대갯수는 n(n-1)이다.