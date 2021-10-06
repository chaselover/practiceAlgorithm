import sys
input = sys.stdin.readline

n, k = map(int, input().split())
matrix = [[0] * n for __ in range(n)]
for __ in range(k):
    a, b = map(lambda x : int(x) - 1, input().split())
    matrix[a][b] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if matrix[i][k] and matrix[k][j]:
                matrix[i][j] = 1
for __ in range(int(input())):
    a, b = map(lambda x : int(x) - 1, input().split())
    if matrix[a][b]:
        print(-1)
    elif matrix[b][a]:
        print(1)
    else:
        print(0)