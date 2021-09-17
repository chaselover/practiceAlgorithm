import sys
input = sys.stdin.readline
from collections import deque


def bfs():
    cnt = 0
    while fireballs:
        fireball_moved = {}
        for _ in range(len(fireballs)):
            x, y, m, s, d = fireballs.popleft()
            nx, ny = (x+(direction[d][0])*s)%N, (y+(direction[d][1])*s)%N
            if (nx,ny) not in fireball_moved:
                fireball_moved[(nx,ny)] = [m, s, [d], 1]
            else:
                fireball_moved[(nx,ny)][0] += m
                fireball_moved[(nx,ny)][1] += s
                fireball_moved[(nx,ny)][2] += [d]
                fireball_moved[(nx,ny)][3] += 1
        for fireball in fireball_moved:
            if fireball_moved[fireball][3]==1:
                x, y = fireball
                fireballs.append((x, y, fireball_moved[fireball][0], fireball_moved[fireball][1], fireball_moved[fireball][2].pop()))
            else:
                x, y = fireball
                m = fireball_moved[fireball][0]//5
                if not m:
                    continue
                s = fireball_moved[fireball][1]//fireball_moved[fireball][3]
                flag = 0
                for d in fireball_moved[fireball][2]:
                    if d&1:
                        flag += 1
                if flag==len(fireball_moved[fireball][2]) or not flag:
                    for i in range(0,7,2):
                        fireballs.append((x,y,m,s,i))
                else:
                    for i in range(1,8,2):
                        fireballs.append((x,y,m,s,i))
        cnt += 1
        if cnt==K:
            return       


N, M, K = map(int, input().split())
direction = ((-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1))
fireballs = deque()
for _ in range(M):
    fireballs.append(tuple(map(int, input().split())))

bfs()
answer = 0
while fireballs:
    x, y, m, s, d = fireballs.pop()
    answer += m
print(answer)