import sys
input = sys.stdin.readline

a_idx = {}
N, M = map(int, input().split())
A = sorted([int(input()) for _ in range(N)])
for i in range(N):
    if A[i] not in a_idx:
        a_idx[A[i]] = i
D = [int(input()) for _ in range(M)]
for num in D:
    if num in a_idx:
        print(a_idx[num])
    else:
        print(-1)