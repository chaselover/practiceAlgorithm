import sys
input = sys.stdin.readline
from collections import defaultdict,deque

def BFS(v):
    queue=deque()
    queue.append(v)
    while queue:
        N = len(queue)
        for _ in range(N):
            cur_node = queue.popleft()
            if cur_node==k:
                return N
            for next_node in parents[cur_node]:
                queue.append(next_node)

while 1:
    n,k = map(int,input().split())
    if not n and not k:
        break
    arr = list(map(int,input().split()))
    parents = defaultdict(list)
    if k==arr[0]:
        print(0)
    else:
        idx=0
        for i in range(1,n):
            parents[arr[idx]].append(arr[i])
            if arr[i]==k:
                parent_k=arr[idx]
            if i <n-1 and arr[i]+1 < arr[i+1]:
                idx+=1
        level_cnt= BFS(arr[0])
        print(level_cnt-len(parents[parent_k]))
