from sys import setrecursionlimit, stdin
setrecursionlimit(1000000)
input = stdin.readline # 입력 시간 안줄여주면 시간초과 난다
n = int(input().rstrip())
tree = [[] for _ in range(n+1)] # 2차원 인접 리스트
for _ in range(n-1):
    n1, n2 = [int(x) for x in input().rstrip().split()]
    tree[n1].append(n2)
    tree[n2].append(n1) # 여기서 한쪽 노드만 인접하게 설정해줘서 계속 오답났다.

# DFS
# 1. 단말 노드이면 연결된 노드는 얼리어답터
# 2. 연결된 노드가 모두 얼리어답터 아니면 무조건 얼리어답터
early = set()
visited = set()
def dfs(n):
    global tree, early, visited
    visited.add(n)
    if len(tree[n]) <= 1: # 단말노드이다
        return True 
    for i in tree[n]:
        if not i in visited: # 양방향 그래프이므로 무한루프에 빠지지 않게끔
            if dfs(i):
                early.add(n)
            elif not i in early: # 연결된 노드가 얼리어답터 아니면
                early.add(n)
    return False # 단말노드 아니다

# 단말노드에서 시작하지 않게끔
for i, start in enumerate(tree):
    if len(start) > 1:
        dfs(i)
        break
# 모두 단말노드인 경우
if n==2:
    print(1)
else:
    print(len(early))




# tree dp
import sys
input = sys.stdin.readline
from collections import deque
N = int(input())
graph = [[] for _ in range(N+1)]
for i_ in range(N-1):
    a,b= map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)


dp = [[0]*2 for _ in range(N+1)]
visited = [0]*(N+1)
dp[1][0] += 1
visited[1] = 1
depth = [0] * (N+1)
stack = []
stack.append(1)
while stack:
    cnt = 0
    top = stack[-1]
    for elem in graph[top]:
        if visited[elem] == 0:
            visited[elem] = 1
            dp[elem][0] = 1
            depth[elem] = depth[top]+ 1
            stack.append(elem)
            cnt += 1
    if cnt == 0:
        stack.pop()
        for elem in graph[top]:
            if depth[elem] < depth[top]:
                dp[elem][0] += min(dp[top][0],dp[top][1])
                dp[elem][1] += dp[top][0]
