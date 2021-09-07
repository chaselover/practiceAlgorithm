import sys
input = sys.stdin.readline
from heapq import heappop,heappush

def find(x):
    if parent[x]==x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a = find(a)
    b = find(b)

    if level[a] >= level[b]:
        parent[b] = a
        if level[a]==level[b]:
            level[a] += 1
    else:
        parent[a] = b

n, m = map(int, input().split())
parent = {i:i for i in range(1,n+1)}
level = {i: 0 for i in range(1,n+1)}
# 2~n번컴퓨터까지 MST를 만들어라?
for _ in range(m):
    x, y = map(int, input().split())
    if find(x) != find(y):
        union(x,y)

cost_matrix = [list(map(int, input().split())) for _ in range(n)]
costs = []
for i in range(1,n-1):
    for j in range(i+1,n):
        heappush(costs,(cost_matrix[i][j],i+1,j+1))

min_cost = 0
cnt = 0
coms = []
while costs:
    c, a, b = heappop(costs)
    if find(a) != find(b):
        union(a,b)
        min_cost += c
        cnt += 1
        coms.append([a,b])
print(min_cost, cnt)
for com in coms:
    print(*com)



# 다른풀이
import sys
import heapq
def input():
    return sys.stdin.readline().rstrip()
def find_parent(ind):
    if make_set[ind] == ind:
        return ind
    make_set[ind] = find_parent(make_set[ind])
    return make_set[ind]

def union(x,y):
    X = find_parent(x)
    Y = find_parent(y)
    if X == Y:
        return False
    else:
        if ranks[X] < ranks[Y]:
            X,Y = Y,X
        make_set[Y] = X
        if ranks[X] == ranks[Y]:
            ranks[X] += 1
        return True

N,M = map(int,input().split())

make_set = [i for i in range(N+1)]
ranks = [1 for _ in range(N+1)]
connect_cnt = 0
for _ in range(M):
    x,y = map(int,input().split())
    if union(x,y):
        connect_cnt += 1

node_list = []

for x in range(N):
    temp = list(map(int,input().split()))

    for y in range(N):
        if x == 0 or y ==0 or x==y or x>y:
            continue
        else:
            node_list.append((temp[y],x+1,y+1))

if connect_cnt == N-2:
    print(0,0)
else:
    heapq.heapify(node_list)
    result = 0
    answer = []
    while node_list:
        pay,x,y = heapq.heappop(node_list)

        if union(x,y):
            result += pay
            connect_cnt += 1
            answer.append((x,y))
        if connect_cnt == N-2:
            break
    print(result,len(answer))
    for row in answer:
        print(*row)


# 다른풀이
input = __import__('sys').stdin.readline
import heapq
n,m = map(int,input().split())
e = []
for i in range(m): 
    e.append(tuple(map(lambda x:int(x)-1,input().split())))
adj = [list(map(int,input().split())) for i in range(n)]
for a,b in e:
    adj[a][b] = 0
    adj[b][a] = 0

cost = [float('inf')]*n
cost[1] = 0
visit = [False]*n
visit[0]  =True
cost[0] = 0
H = [(0,1,0)]
e = []
while H:
    c,u,p = heapq.heappop(H)
    if (not visit[u]) and c==cost[u]:
        visit[u] = True
        if c: 
            e.append((u+1,p+1))
        for v in range(n):
            if (not visit[v]) and adj[u][v]<cost[v]:
                heapq.heappush(H,(adj[u][v],v,u))
                cost[v] = adj[u][v]
print(sum(cost), len(e))
for i in e: print(*i)