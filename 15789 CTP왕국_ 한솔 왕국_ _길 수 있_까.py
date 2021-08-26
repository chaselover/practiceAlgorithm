import sys
input = sys.stdin.readline
from collections import deque
from heapq import heappop,heappush

def bfs(i):
    queue = deque()
    queue.append(i)
    check[i] = i
    cnt = 1
    while queue:
        cur = queue.popleft()
        for next in graph[cur]:
            if not check[next]:
                queue.append(next)
                check[next] = i
                cnt += 1
    return cnt

N, M = map(int, input().split())
graph = {i: [] for i in range(1,N+1)}
for _ in range(M):
    a, b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]
check = {i:0 for i in range(1,N+1)}
count_set = []
C, H, K = map(int, input().split())
for i in range(1,N+1):
    if not check[i]:
        c = bfs(i)
        heappush(count_set,(-c,i))
        if check[C] == i:
            init_power = c

power = init_power
while count_set and K > 0:
    cur_union_cnt, king = heappop(count_set)
    if check[king] != check[C] and check[king] != check[H]:
        power -= cur_union_cnt
        K -= 1
print(power)