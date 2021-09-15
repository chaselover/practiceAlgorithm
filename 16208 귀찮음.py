import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
total = sum(arr)
answer  = 0
for num in arr:
    answer += num * (total - num)
    total -= num
print(answer)