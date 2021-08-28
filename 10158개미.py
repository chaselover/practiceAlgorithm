import sys
input = sys.stdin.readline

w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

init_x = p + t
init_y = q + t
if not (init_x//w)&1:
    x = (-2*w*((init_x//w)//2) + init_x)
else:
    x = 2*w - (-2*w*((init_x//w)//2) + init_x)
if not (init_y//h)&1:
    y = (-2*h*((init_y//h)//2) + init_y)
else:
    y = 2*h - (-2*h*((init_y//h)//2) + init_y)
print(x,y)