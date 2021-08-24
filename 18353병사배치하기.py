import sys
input = sys.stdin.readline
from bisect import bisect_left

N = int(input())
arr = list(map(int, input().split()))
q = []
q.append(-arr[0])
for i in range(1,N):
    if -arr[i] > q[-1]:
        q.append(-arr[i])
    else:
        q[bisect_left(q,-arr[i])] = -arr[i]
print(N-len(q))
