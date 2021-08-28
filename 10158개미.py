import sys
input = sys.stdin.readline

w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

init_x = p + t
init_y = q + t

while not 0 <= init_x <= w or not 0 <= init_y <= h:
    if init_x > w:
        init_x = 2*w - init_x
    elif init_x < 0:
        init_x *= -1
    elif init_y > h:
        init_y = 2*h - init_y
    elif init_y < 0:
        init_y *= -1

print(init_x,init_y)