import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))

q=[]
for x in a:
    if not q or x > q[-1]:
        q.append(x)
    else:
        q[bisect_left(q,x)] = x

print(len(q))
