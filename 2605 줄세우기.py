import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))
answer = []
for i in range(1,N+1):
    answer.insert(arr[i-1],i)
print(*answer[::-1])