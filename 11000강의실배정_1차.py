import sys
input = sys.stdin.readline
from collections import deque

N= int(input())
times = []
for _ in range(N):
    times.append(list(map(int,input().split())))

class_room = 1
overlap = 0
last_time = deque()
for i in range(N):
    if last_time[0] > times[i][0]:
        overlap+=1
    if last_time < times[i][1]:
        last_time = times[i][1]
    if overlap > class_room:
        class_room+=1

