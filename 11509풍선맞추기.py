import sys
input = sys.stdin.readline

N = int(input())
H = list(map(int,input().split()))
arrows = []
for i in range(N):
    if H[i]+1 in arrows:
        arrows[arrows.index(H[i]+1)] -=1
    else:
        arrows.append(H[i])

print(len(arrows))