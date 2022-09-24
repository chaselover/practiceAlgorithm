import sys
input = sys.stdin.readline
from bisect import bisect_right

T = int(input())
for test in range(T):
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    A.sort()
    sum = 0
    for i in B:
        sum += len(A)-bisect_right(A,i)
    print(sum)