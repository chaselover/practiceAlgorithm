import sys
input = sys.stdin.readline
from collections import deque


N,K = map(int,input().split())
queue = deque()
time = [0] * (100001)

def BFS():
    queue.append(N)
    while queue:
        v= queue.popleft()
        if v == K:
            return time[v]
        for next_step in (v-1, v+1, v*2): 
            if 0 <= next_step < 100001 and not time[next_step]: 
                time[next_step] = time[v] + 1 
                queue.append(next_step)

if N <= K:
    print(BFS())
else:
    print(N-K)