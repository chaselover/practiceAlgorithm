import sys
input = sys.stdin.readline
from collections import defaultdict,deque

N = int(input())
graph = defaultdict(list)

for _ in range(N-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

queue = deque([1])
ans = {}
check = [False for _ in range(N+1)]

while queue:
    parent = queue.popleft()
    for i in graph[parent]:
        if not check[i]:
            ans[i] = parent
            queue.append(i)
            check[i] = True

for i in range(2,N+1):
    print(ans[i])