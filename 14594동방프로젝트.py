import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
rooms = [1] * (N+1)
break_wall=[]

for _ in range(M):
    x, y = map(int, input().split())
    break_wall.append([x,y])

for left,right in break_wall:
    for i in range(left,right):
        rooms[i] = 0

print(sum(rooms)-1)