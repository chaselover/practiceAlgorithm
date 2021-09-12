import sys
input = sys.stdin.readline
from bisect import bisect_left

n = int(input())
arr = list(map(int, input().split()))
answer = [arr[0]]
for num in arr[1:]:
    if answer[-1] < num:
        answer.append(num)
    else:
        answer[bisect_left(answer,num)] = num
print(len(answer))