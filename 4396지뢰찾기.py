import sys
input = sys.stdin.readline


n = int(input())

mines = [list(input().rstrip()) for _ in range(n)]
maps = [list(input().rstrip()) for _ in range(n)]

di = [0,0,-1,1,1,1,-1,-1]
dj = [1,-1,0,0,1,-1,1,-1]

flag = False
for i in range(n):
    for j in range(n):
        if maps[i][j]=='x':
            if mines[i][j]=='*':
                flag = True
                continue
            cnt = 0
            for k in range(8):
                if 0<= i+di[k] < n and 0 <= j+dj[k] < n and mines[i+di[k]][j+dj[k]]=='*':
                    cnt += 1
            maps[i][j] = str(cnt)

if flag:
    for i in range(n):
        for j in range(n):
            if mines[i][j]=='*':
                maps[i][j] = '*'

for row in maps:
    print(''.join(row))