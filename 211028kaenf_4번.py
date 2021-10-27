from collections import defaultdict

def dfs(cur_node, graph, visited):
    global answer
    visited[cur_node] = True
    answer += '(' + cur_node
    for next_node in graph[cur_node]:
        if visited[next_node]:
            answer = 'E3'
            for key in visited:
                visited[key] = True
            return
        dfs(next_node, graph, visited)
        answer += ')'
    return answer

    
def sExpression(nodes):
    global answer
    graph = defaultdict(list)
    visited = {}
    for idx, char in enumerate(nodes):
        if char == ',':
            start, end = nodes[idx - 1], nodes[idx + 1]
            visited[start], visited[end] = False, False
            if start in graph and end in graph[start]:
                return 'E2'
            if end in graph and start in graph[end]:
                return 'E2'
            graph[start].append(end)
            if len(graph[start]) > 2:
                return 'E1'
    for value in graph.values():
        value.sort()
   
    for start in visited:
        visited = {node: False for node in visited}
        answer = ''
        dfs(start, graph, visited)
        answer += ')'
        if len(answer) == 3 * len(visited):
            return answer
        if answer[0] == 'E':
            return 'E3'
    return 'E4'


if __name__ == '__main__':
    nodes = input()

    result = sExpression(nodes)

    print(result)
