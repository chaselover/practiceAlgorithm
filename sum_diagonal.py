
def findPath_dfs(v, visted):
    global visited
    visited.append(v)
    for adj in graph[v]:
        if not adj in visited:
            visited = findPath_dfs(adj,visited)
        return visited



for test in range(1,int(input())+1):
    graph = {}
    N,M = map(int,input().split())
    max_path = 1
    visited = []
    for _ in range(M):
        x,y = map(int,input().split())
        graph[x] = graph.get(x,[]) + [y]
        graph[y] = graph.get(y,[]) + [x]
    
    for i in range(1,N+1):
        if M==0:
            break
        else:
            findPath_dfs(i,visited)
            if max_path < len(visited):
                max_path = len(visited)

    print(f"#{test} {graph}")
    