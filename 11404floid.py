import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
maps = [[float('inf') for _ in range(n)] for _ in range(n)]
for _ in range(m):
    a,b,c = map(int,input().split())
    maps[a-1][b-1]=min(maps[a-1][b-1],c)

for i in range(n):
    maps[i][i]=0

for k in range(n):
    for i in range(n):
        for j in range(n):
            if maps[i][j] > maps[i][k]+maps[k][j]:
                maps[i][j] = maps[i][k]+maps[k][j]

for map in maps:
    print(*map)