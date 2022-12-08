import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))
board = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

graph = [[] for _ in range(m + n + 2)]
for i in range(1, m + 1):
    graph[0].append([i, b[i - 1]])

    for j in range(m + 1, m + n + 1):
        graph[i].append([j, float('inf')])

for j in range(m + 1, m + n + 1):
    graph[j].append([m + n + 1, a[j - m - 1]])

weight = 0
while True:
    res = [float('inf')] * (m + n + 2)
    res[0] = 0

    prev = [-1] * (m + n + 2)
    visit = [0] * (m + n + 2)
    queue = deque([0])

    while queue:
        cur = queue.popleft()
        visit[cur] = 0
        
        for nxt, capacity in graph[cur]:
            if 0 < cur < nxt < m + n + 1:
                cost = board[cur - 1][nxt - m - 1]
            elif 0 < nxt < cur < m + n + 1:
                cost = -board[nxt - 1][cur - m - 1]
            else:
                cost = 0
            
            if res[nxt] > res[cur] + cost:
                res[nxt] = res[cur] + cost
                prev[nxt] = cur
                
                if not visit[nxt]:
                    queue.append(nxt)
                    visit[nxt] = 1
    
    if res[-1] == float('inf'):
        break

    flow = float('inf')
    nxt = m + n + 1
    while nxt:
        cur = prev[nxt]
        for i in range(len(graph[cur])):
            if graph[cur][i][0] == nxt:
                flow = min(flow, graph[cur][i][1])
                break
        nxt = cur
    
    nxt = m + n + 1
    while nxt:
        cur = prev[nxt]

        if 0 < cur < nxt < m + n + 1:
            weight += flow * board[cur - 1][nxt - m - 1]
        elif 0 < nxt < cur < m + n + 1:
            weight -= flow * board[nxt - 1][cur - m - 1]
        
        for i in range(len(graph[cur])):
            if graph[cur][i][0] == nxt:
                graph[cur][i][1] -= flow
                if graph[cur][i][1] == 0:
                    graph[cur].remove([nxt, 0])
                break
        
        for i in range(len(graph[nxt])):
            if graph[nxt][i][0] == cur:
                graph[nxt][i][1] += flow
                break
        else:
            graph[nxt].append([cur, flow])
        
        nxt = cur
    
print(weight)




# 2
from collections import deque

import sys

input = sys.stdin.readline

N, M = map(int, input().split()) #N이 사람 M이 서점

S = N + M

E = N + M + 1

total = N + M + 2

INF = 10000000

adj = [[] for _ in range(total)]

dist = [[0] * total for _ in range(total)]

capacity = [[0] * total for _ in range(total)]

flow = [[0] * total for _ in range(total)]

left = list(range(M))

right = list(range(M, N+M))

adj[S] = left

adj[E] = right

for u in range(M):

    adj[u] = right + [S]

for u in range(M, N + M):

    adj[u] = left + [E]

arr = list(map(int, input().split()))

for u, cap in enumerate(arr):

    u += M

    capacity[u][E] = cap

arr = list(map(int, input().split()))

for u, cap in enumerate(arr):

    capacity[S][u] = cap

for i in range(M):

    arr = list(map(int, input().split()))

    for j, d in enumerate(arr):

                   j += M

                   dist[i][j] = d

                   dist[j][i] = -d

                   capacity[i][j] = INF

def SPFA(S, E):

    d = [INF] * total

    d[S] = 0

    q = deque([S])

    inqueue = [False] * total

    prev = [-1] * total

    while q:

        u = q.popleft()

        inqueue[u] = False

        for v in adj[u]:

            if capacity[u][v] - flow[u][v] > 0 and d[u] + dist[u][v] < d[v]:
                
                d[v] = d[u] + dist[u][v]

                prev[v] = u

                if not inqueue[v]:

                    q.append(v)

                    inqueue[v] = True

    return prev

def MCMF(S, E, prev):

    ret = 0

    minFlow = INF

    v = E

    while v != S:

        u = prev[v]

        minFlow = min(minFlow, capacity[u][v] - flow[u][v])

        v = u

    v = E

    while v != S:

        u = prev[u]

        ret += dist[u][v] * minFlow

        flow[u][v] += minFlow

        flow[v][u] -= minFlow

        v = u

    return ret

ans = 0

while 1:

    prev = SPFA(S, E)

    if prev[E] == -1:

        break

    ans += MCMF(S, E, prev)

print(ans)

# 3
import sys

def solve(graph, capacity, flow, cost, s, t):
    ret = 0
    while True:
        parent = [-1 for _ in range(210)]
        distance = [10 ** 9 for _ in range(210)]
        in_queue = [False for _ in range(210)]
        queue = [s]
        distance[s] = 0
        in_queue[s] = True
        while queue:
            temp = []
            for curr in queue:
                in_queue[curr] = False
                for next in graph[curr]:
                    if capacity[curr][next] - flow[curr][next] > 0 and distance[next] > distance[curr] + cost[curr][next]:
                        distance[next] = distance[curr] + cost[curr][next]
                        parent[next] = curr
                        if in_queue[next] == False:
                            in_queue[next] = True
                            temp.append(next)
            queue = temp
        if parent[t] == -1:
            break
        val = 10 ** 9
        curr = t
        while curr != s:
            val = min(val, capacity[parent[curr]][curr] - flow[parent[curr]][curr])
            curr = parent[curr]
        curr = t
        while curr != s:
            ret += val * cost[parent[curr]][curr]
            flow[parent[curr]][curr] += val
            flow[curr][parent[curr]] -= val
            curr = parent[curr]
    return ret

def main():
    n, m = map(int, sys.stdin.readline().split())
    A = list(map(int, sys.stdin.readline().split()))
    B = list(map(int, sys.stdin.readline().split()))
    capacity = [[0 for _ in range(210)] for _ in range(210)]
    flow = [[0 for _ in range(210)] for _ in range(210)]
    cost = [[0 for _ in range(210)] for _ in range(210)]
    graph = [[] for _ in range(210)]
    for i in range(1, m + 1):
        temp = list(map(int, sys.stdin.readline().split()))
        for j in range(1, n + 1):
            cost[i + 100][j] = -temp[j - 1]
            cost[j][i + 100] = temp[j - 1]
            graph[i + 100].append(j)
            graph[j].append(i + 100)
            capacity[j][i + 100] = 10 ** 9
    for i in range(n):
        graph[i + 1].append(0)
        graph[0].append(i + 1)
        capacity[0][i + 1] = A[i]
    for i in range(m):
        graph[i + 101].append(201)
        graph[201].append(i + 101)
        capacity[i + 101][201] = B[i]
    ans = solve(graph, capacity, flow, cost, 0, 201)
    print(ans)
    return

if __name__ == "__main__":
    main()
