import sys
from collections import defaultdict
input = sys.stdin.readline

N,M = map(int, input().split())
check = [False]*N
graph = defaultdict(list)
cnt = 0

for _ in range(M):
    a,b = map(int,input().split())
    graph[a] += [b]
    graph[b] += [a]

# 방문, graph[v]안의 노드들 돌아가면서 검사 노드하나들어가서 
# False면 True방문하고 DFS로 파고들고 h하나 늘리고. 
# 끝까지 갔는데 못찾으면 check하나씩 False로 되돌리면서 나오기
# 이런식으로 모든 경로 깊이 탐색.

def DFS(v,h):
    if h==4:
        print(1)
        exit()
    for i in graph[v]:
        if check[i]==False:
            check[i] = True
            DFS(i, h+1)
            check[i]=False

# 최초 몇번노드로 들어갈 것인지?0~N-1
for i in range(N):
    check[i] = True
    DFS(i,0)
    check[i]= False
    
print(0)