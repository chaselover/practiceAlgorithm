import sys
input = sys.stdin.readline
from collections import deque

def bfs(start,target):
    queue = deque()
    queue.append([start,0,[start]])
    visited = [False]*400001
    visited[start] = True
    while queue:
        cur,cur_time,cur_path = queue.popleft()
        if cur==target:
            return cur_time ,cur_path
        for next_node in (cur-1,cur+1,cur*2):
            if 0<=next_node<=200000 and not visited[next_node]:
                visited[next_node] = True
                queue.append([next_node,cur_time+1,cur_path+[next_node]])

N, K = map(int, input().split())
if K <= N:
    print(N-K)
    print(*[i for i in range(N,K-1,-1)])
    exit()
time, path = bfs(N,K)
print(time)
print(*path)