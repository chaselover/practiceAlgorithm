import sys
input = sys.stdin.readline
from math import ceil

N = int(input())
A = list(map(int,input().split()))
B,C = map(int,input().split())
cnt=0
for i in range(N):
    if A[i]-B>0:
        cnt+=ceil((A[i]-B)/C)
    cnt+=1

print(cnt)