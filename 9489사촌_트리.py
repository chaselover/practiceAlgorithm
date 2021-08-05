import sys
input = sys.stdin.readline
from collections import defaultdict


while 1:
    n,k = map(int,input().split())
    if not n and not k:
        break
    arr = list(map(int,input().split()))
    parents = defaultdict(int)
    idx=0
    for i in range(1,n):
        parents[arr[i]] = arr[idx]
        if i <n-1 and arr[i]+1 < arr[i+1]:
            idx+=1
    if parents[parents[k]]:
        cnt=0
        for node in arr:
            if (parents[parents[k]] == parents[parents[node]]) and (parents[k] != parents[node]):
                cnt+=1
        print(cnt)
    else:
        print(0)
