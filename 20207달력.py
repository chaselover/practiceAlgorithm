import sys
input = sys.stdin.readline

N = int(input())
sch = [0]*(366)
for _ in range(N):
    a, b = map(int, input().split())
    for i in range(a,b+1):
        sch[i] += 1

area = 0
max_h = 0
for i in range(1,366):
    if not sch[i-1] and sch[i]:
        left = i
    if max_h < sch[i]:
        max_h = sch[i]
    if not sch[i] and sch[i-1]:
        right = i
        area += (right-left)* max_h
        max_h = 0
        left = 0
        right = 0
area += (366-left)* max_h

print(area)