# 원교근공_LV3
"""
중복 경유없이 각 나라끼리 이동할 수 있는 경로가 반드시 하나만 존재하는 경우는 나라 간 연결이 tree의 형태를 이룰 때 입니다.
이에따라 location을 root로 하는 tree graph를 그립니다.
각 서브트리 루트까지의 최선의 결과는 상위 트리 결과를 연산할 때도 독립적으로 작용하기 때문에 
각 나라가 동맹에 속하는 경우와 속하지 않는 경우의 결과를 dynamic programming으로 구할 수 있습니다.
최종적으로 dp[location][1]에 location을 포함하는 최대의 연산 결과가 저장되며 같은 원리를 통해
각 subtree의 root를 포함하는 경우와 포함하지 않는 경우를 역추적해 최종 동맹 allies에 포함 되는 지 여부를 판단할 수 있습니다.
"""
from collections import defaultdict

def merge_power(u, army_powers):
    global visited, dp, graph
    visited[u] = True
    dp[u][1] = army_powers[u]
    dp[u][0] = 0
    for v in graph[u]:
        if not visited[v]:
            merge_power(v, army_powers)
            dp[u][1] += dp[v][0]
            dp[u][0] += max(dp[v][1], dp[v][0])


def make_allies(u, is_having):
    global graph, dp, visited, allies
    visited[u] = True
    if is_having and dp[u][1] > dp[u][0]:
        allies.append(u)
        is_having = False
    else:
        is_having = True
    for v in graph[u]:
        if not visited[v]:
            make_allies(v, is_having)


def solution(n, location, army_powers, edges):
    global visited, dp, graph, visited, allies
    graph = defaultdict(list)
    for a, b in edges:
        graph[a] += [b]
        graph[b] += [a]
    dp = {i: [0, 0] for i in range(n)}
    visited = {i: False for i in range(n)}
    merge_power(location, army_powers)
    max_power = dp[location][1]
    allies = [location]
    visited = {i: False for i in range(n)}
    visited[location] = True
    for v in graph[location]:
        make_allies(v, False)
    allies.sort()
    return max_power, allies


if __name__ == "__main__":
    print(solution(4, 0, [70, 80, 100, 2000], [[0, 1], [1, 2], [2, 3]]))