import sys
input = sys.stdin.readline
from collections import deque

N,K = map(int,input().split())
queue=deque()
time = [-1]*100001

def BFS(N,K):
    queue.append(N)
    time[N] = 0
    while queue:
        N = queue.popleft()
        if N==K:
            print(time[K])
            exit()
        for next_node in (2*N,N+1,N-1):
            if 0<=next_node<100001 and time[next_node]==-1:
                if next_node == 2*N:
                    # 위상이 같을때는 queue앞에 넣어주어도 됨.(위상 = level)
                    queue.appendleft(next_node)
                    time[next_node] = time[N]
                else:
                    queue.append(next_node)
                    time[next_node] = time[N]+1 
if N<K:
    BFS(N,K)
else:
    print(N-K)