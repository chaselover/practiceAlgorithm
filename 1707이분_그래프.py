import sys
input = sys.stdin.readline
from collections import defaultdict
from collections import deque


def BFS(v):
    queue.append(v)
    check[v] = 1
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if check[i] ==0:
                if check[v]==1:
                    check[i]= -1
                else:
                    check[i] = 1
                queue.append(i)



for test in range(int(input())):
    V,E = map(int,input().split())
    graph = defaultdict(list)
    queue = deque()
    check = [0]*(V+1)
    ans = 0

    for _ in range(E):
        a,b = map(int,input().split())
        graph[a] +=[b]
        graph[b] +=[a]

    for i in range(1,V+1):
        if check[i] ==0:
            BFS(i)
    
    for i in range(1,V+1):
        for adj in graph[i]:
            if check[i]==check[adj]:
                ans = 1

    if ans==0:
        print("YES")
    else:
        print("NO")