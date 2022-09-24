import sys
input = sys.stdin.readline
from heapq import heappop,heappush

n = int(input())
basket = []
for i in range(n):
    command = input().split()
    A = command[0]
    if A=='1':
        tasty = command[1]
        basket.append(tasty)
    else:
        tasty = command[1]
        push_pull = command[2]
        if push_pull >0:
            for i in range(push_pull):
                basket.append(tasty)
        else:
            for i in range(-push_pull):
                basket.pop()