import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))

start, end = 0, N-1
min = float('inf')

while start < end:
    _sum = arr[start] + arr[end]
    if abs(min) > abs(_sum):
        min = _sum
    if _sum < 0:
        start +=1
    else:
        end -=1

print(min)


