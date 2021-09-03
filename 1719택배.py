import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dists = [[float('inf') for _ in range(n)] for _ in range(n)]
pre_node = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    dists[a-1][b-1] = min(dists[a-1][b-1],c)
    dists[b-1][a-1] = min(dists[b-1][a-1],c)
    pre_node[a-1][b-1] = b
    pre_node[b-1][a-1] = a


for k in range(n):
    for i in range(n):
        for j in range(n):
            if dists[i][j] > dists[i][k] + dists[k][j]:
                dists[i][j] = dists[i][k] + dists[k][j]
                pre_node[i][j] = pre_node[i][k]

for i in range(n):
    pre_node[i][i] = '-'
for row in pre_node:
    print(*row)