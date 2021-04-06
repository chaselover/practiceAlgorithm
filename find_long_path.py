
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
        graph[x] = graph.get(x,[]) + [y]#딕셔너리에 x키가 있으면 x키의 값을 반환하고
        graph[y] = graph.get(y,[]) + [x]#없으면 디폴트값[]를 내놓는다 +[y]
                                        #리스트 합을 통해 graph[x]에 재저장.
    for i in range(1,N+1):
        if M==0:
            break
        else:
            findPath_dfs(i,visited)
            if max_path < len(visited):
                max_path = len(visited)

    print(f"#{test} {max_path}")
    