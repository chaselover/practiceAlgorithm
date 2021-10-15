import sys
input = sys.stdin.readline

num_set = {}
N = int(input())
A = list(map(int, input().split()))
for num in A:
    num_set[num] = True
M = int(input())
Q = list(map(int, input().split()))
for num in Q:
    if num in num_set:
        print(1)
    else:
        print(0)