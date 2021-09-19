import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
arr = list(map(int, input().split()))

max_size = 0
for i in range(1,M):
    max_size = max(max_size, arr[i] - arr[i-1])

print(max((max_size+1)//2,arr[0] - 0, N - arr[-1]))