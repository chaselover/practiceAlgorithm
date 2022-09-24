import sys
input = sys.stdin.readline

N = int(input())
tree = [[float('inf') for _ in range(N+1)] for _ in range(N+1)]

for _ in range(N-1):
    a,b,c = map(int,input().split())
    tree[a][b] = c
    tree[b][a] = c

for i in range(1,N+1):
    tree[i][i] = 0

for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            if tree[i][j] > tree[i][k] + tree[k][j]:
                tree[i][j] = tree[i][k] + tree[k][j]

M = int(input())

for _ in range(M):
    a,b = map(int,input().split())
    print(tree[a][b])