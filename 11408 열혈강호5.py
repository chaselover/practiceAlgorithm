import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
board = [[0] * (m + 1) for _ in range(n + 1)]
graph = [[] for _ in range(n + m + 2)]

for i in range(1, n + 1):
    data = list(map(int, sys.stdin.readline().split()))
    for j in range(data[0]):
        board[i][data[2 * j + 1]] = data[2 * j + 2]
        graph[i].append(data[2 * j + 1] + n)

for i in range(1, n + 1):
    graph[0].append(i)

for j in range(n + 1, n + m + 1):
    graph[j].append(n + m + 1)

ans = 0
weight = 0
while True:
    res = [float('inf')] * (n + m + 2)
    res[0] = 0

    prev = [-1] * (n + m + 2)
    visit = [0] * (n + m + 2)
    queue = deque([0])

    while queue:
        cur = queue.popleft()
        visit[cur] = 0
        
        for nxt in graph[cur]:
            if 0 < cur < nxt < n + m + 1:
                cost = board[cur][nxt - n]
            elif 0 < nxt < cur < n + m + 1:
                cost = -board[nxt][cur - n]
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

    ans += 1
    nxt = n + m + 1
    while nxt:
        cur = prev[nxt]
        
        if 0 < cur < nxt < n + m + 1:
            weight += board[cur][nxt - n]
        elif 0 < nxt < cur < n + m + 1:
            weight -= board[nxt][cur - n]
        
        graph[cur].remove(nxt)
        graph[nxt].append(cur)
        nxt = cur

print(ans)
print(weight)

# 2
import sys
input = sys.stdin.readline
INF = 9876543210

def MCMF(source, sink):
    answer = [0, 0] # 최소 비용, 최대 유량
    while True:
        path, dist = [-1]*v, [INF]*v
        inQueue, queue = [0]*v, [source] # 다음에 방문할 정점들
        dist[source], inQueue[source] = 0, 1
        while queue:
            present = queue[0] # 현재 정점
            del queue[0]
            inQueue[present] = False
            for _next in adj[present]:
                # 최소 비용이고, 최대 유량일 경우
                if dist[_next] > dist[present] + cost[present][_next] and capacity[present][_next] - flow[present][_next] > 0:
                    dist[_next], path[_next] = dist[present] + cost[present][_next], present
                    if not inQueue[_next]:
                        queue.append(_next)
                        inQueue[_next] = 1
        if path[sink] == -1: # 가능한 모든 경로를 찾았을 경우
            break
        # 현재 경로에서의 최소 유량 찾음
        flowRate = INF
        present = sink
        while present != source:
            previous = path[present]
            flowRate = min(flowRate, capacity[previous][present] - flow[previous][present])
            present = path[present]
        # 유량 흘림
        present = sink
        while present != source:
            previous = path[present]
            answer[0] += flowRate*cost[previous][present] # 총 비용이 각 간선 비용만큼 증가
            flow[previous][present] += flowRate
            flow[present][previous] -= flowRate # 음의 유량
            present = path[present]
        answer[1] += flowRate
    return answer

MAX_N, MAX_M = 400, 400 # 최대 직원의 수, 최대 일의 수
n, m = map(int, input().split()) # 직원의 수, 일의 수
v = MAX_N + MAX_M + 2 # 정점의 수 (최대 직원 수 + 최대 일의 수 + source + sink)
capacity = [[0]*v for _ in range(v)] # 용량
flow = [[0]*v for _ in range(v)] # 유량
cost = [[0]*v for _ in range(v)] # 비용
adj = [[] for _ in range(v)] # 연결된 정점 (source + 직원 + 일 + sink)
for _n in range(1, n+1): # 직원과 일 매칭
    info = list(map(int, input().split()))
    for i in range(1, len(info), 2):
        _m = MAX_N+info[i]
        adj[_n].append(_m)
        adj[_m].append(_n)
        capacity[_n][_m] = 1
        cost[_n][_m] = info[i+1] # 순방향 간선의 비용
        cost[_m][_n] = -info[i+1] # 역방향 간선의 비용
for _n in range(1, n+1): # source와 직원 매칭
    adj[0].append(_n)
    adj[_n].append(0)
    capacity[0][_n] = 1
for _m in range(MAX_N+1, MAX_N+m+1): # 일과 sink 매칭
    adj[_m].append(v-1)
    adj[v-1].append(_m)
    capacity[_m][v-1] = 1
min_cost, max_flow = MCMF(0, v-1)
print(max_flow)
print(min_cost)

# 3
# 1 아니면 0 임으로 따로 허용량 표시 안해도 되긴 할 듯 -> 속도 향상 될수도

import sys
input = sys.stdin.readline

n,m = list(map(int,input().strip().split()))
# 0 n n+m n+m+1
start = 0
destination = n+m+1
graph = dict([(i,{}) for i in range(n+m+2)])

for i in range(n):
    read = list(map(int,input().strip().split()))[1:]
    for j in range(len(read)//2):
        index = j*2
        graph[i+1][read[index]+n] = read[index+1]
        
for i in range(1,n+1):
    graph[0][i] = 0
    
for i in range(n+1,destination):
    graph[i][destination] = 0
    
def search():
    queue = {}
    new_queue = {start:start}
    distance[start] = 0
    while len(new_queue):
        queue = new_queue
        new_queue = {}
        for k in list(queue.keys()):
            node = queue.pop(k)
            use_graph = graph[node]
            for g in use_graph:
                new_d = distance[node] + use_graph[g]
                if distance[g] > new_d:
                    distance[g] =  new_d
                    parent[g] = node
                    new_queue[g] = g
                
    
sum_v = 0
while True:
    parent = [None for _ in range(m+n+2)]
    distance = [99999 for _ in range(m+n+2)]
    search()
    end = destination
    if parent[destination] == None:
        break
    while True:
        pa = parent[end]
        if pa == None:
            break
        w = graph[pa][end]
        sum_v+=w
        del graph[pa][end]
        graph[end][pa] = -w
        end = pa
        
        
print(len(graph[destination]))
print(sum_v)


# 5 비효율
import sys
from collections import deque
input = sys.stdin.readline
INF = 1e9
n, m = map(int, input().split())
maxv = n+m+2
S = maxv-2
E = maxv-1
c = [[0 for _ in range(maxv)] for _ in range(maxv)]
d = [[0 for _ in range(maxv)] for _ in range(maxv)]
f = [[0 for _ in range(maxv)] for _ in range(maxv)]
adj = [[] for _ in range(maxv)]
for i in range(m):
    c[i+n][E] = 1
    adj[i+n].append(E)
    adj[E].append(i+n)
for i in range(n):
    c[S][i] = 1
    adj[S].append(i)
    adj[i].append(S)
    tmp = list(map(int, input().split()))
    idx = 1
    while idx < tmp[0]*2:
        j, val = tmp[idx], tmp[idx+1]
        d[i][n+j-1], d[n+j-1][i] = val, -val
        c[i][n+j-1] = 1
        adj[i].append(n+j-1)
        adj[n+j-1].append(i)
        idx += 2
res = 0
cnt = 0
while True:
    prev = [-1 for _ in range(maxv)]
    dist = [INF for _ in range(maxv)]
    atQ = [False for _ in range(maxv)]
    q = deque()
    dist[S] = 0
    atQ[S] = True
    q.append(S)
    while q:
        cur = q.popleft()
        atQ[cur] = False
        for nxt in adj[cur]:
            if c[cur][nxt] - f[cur][nxt] > 0 and dist[nxt] > dist[cur] + d[cur][nxt]:
                dist[nxt] = dist[cur]+d[cur][nxt]
                prev[nxt] = cur
                if not atQ[nxt]:
                    q.append(nxt)
                    atQ[nxt] = True
    if prev[E] == -1:
        break
    flow = INF
    i = E
    while i != S:
        flow = min(flow, c[prev[i]][i]-f[prev[i]][i])
        i = prev[i]
    i = E
    while i != S:
        res += flow*d[prev[i]][i]
        f[prev[i]][i] += flow
        f[i][prev[i]] -= flow
        i = prev[i]
    cnt += 1
print(cnt)
print(res)
