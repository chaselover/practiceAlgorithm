import sys
from collections import deque
sys.setrecursionlimit(10**9)

# DFS를 통해 사이클 찾기

def dfs(x, cnt):
    # 이미 방문한 노드인데 거리차가 3 이상일 경우 사이클
    if check[x]:
        if cnt - dist[x] >= 3:
            return x
        else: return -1
    check[x] = 1
    dist[x] = cnt
    for y in adj_list[x]:
        cycleStartNode = dfs(y, cnt + 1)
        if cycleStartNode != -1:
            check[x] = 2
            if x == cycleStartNode: return -1
            else: return cycleStartNode
    return -1

if __name__ == '__main__':
    N = int(input())
    adj_list = [[] * (N + 1) for _ in range(N + 1)]
    # check[i] = 0 : 방문하지 않은 노드
    # check[i] = 1 : 방문한 노드
    # check[i] = 2 : 사이클에 속하는 노드
    check = [0] * (N + 1)
    dist = [0] * (N + 1)

    for _ in range(N):
        u, v = map(int, sys.stdin.readline().split())
        adj_list[u].append(v)
        adj_list[v].append(u)
    # 사이클 찾기
    dfs(1, 0)
    # BFS를 통해 사이클까지의 거리 계산하기
    q = deque()
    for i in range(1, N + 1):
        if check[i] == 2:
            q.append(i)
            dist[i] = 0
        else:
            dist[i] = -1
    while q:
        x = q.popleft()
        for y in adj_list[x]:
            if dist[y] == -1:
                q.append(y)
                dist[y] = dist[x] + 1
    print(' '.join(map(str, dist[1:])))