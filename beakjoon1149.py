import sys

N = int(sys.stdin.readline())
c = []

for _ in range(N):
    color = list(map(int,sys.stdin.readline().split()))
    c.append(color)


# 각 색을 선택시마다 최소값을 누적시키면서 진행.(결국 i-1이랑만 안겹치면됨)
for i in range(1,N):
    c[i][0] = min(c[i-1][1],c[i-1][2])+c[i][0]
    c[i][1] = min(c[i-1][0],c[i-1][2])+c[i][1]
    c[i][2] = min(c[i-1][0],c[i-1][1])+c[i][2]

print(min(c[N-1][0],c[N-1][1],c[N-1][2]))