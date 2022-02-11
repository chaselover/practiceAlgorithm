from collections import deque


def bfs(start,n,info,graph):
    queue = deque()
    queue.append([start,1,0,1])
    max_sheep = 1
    next_time = []
    while queue:
        cur_node, sheep, wolf,visited = queue.popleft()
        if sheep > max_sheep:
            max_sheep = sheep
        for i in range(n):
            if visited & (1<<i):
                for next_node in graph[i]:
                    if not visited & (1<<next_node):
                        if sheep > wolf + info[next_node]:
                            if info[next_node]:
                                queue.append([next_node, sheep, wolf+1,visited|(1<<next_node)])
                            else:
                                queue.append([next_node, sheep+1, wolf,visited|(1<<next_node)])
                        else:
                            next_time.append(next_node)
    return max_sheep

def solution(info, edges):
    n = len(info)
    graph = {i: [] for i in range(n)}
    for parent, child in edges:
        graph[parent].append(child)
    return bfs(0,n,info,graph)





print(solution([0,0,1,1,1,0,1,0,1,0,1,1],[[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))