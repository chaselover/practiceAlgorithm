import sys
input = sys.stdin.readline

from heapq import heappush,heappop

queue = []
for _ in range(int(input())):
    x = int(input())
    if not x:
        try:
            print(heappop(queue)[1])
        except:
            print(0)
    else:
        heappush(queue,(-x,x))