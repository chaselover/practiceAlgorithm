import sys
input = sys.stdin.readline

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
edge = [[1] * n for _ in range(n)]
result = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j or j == k or i == k:
                continue
            # 합으로 표현되면 취하지 않는다.(그게 경로라는뜻)
            if matrix[i][j] == matrix[i][k] + matrix[k][j]:
                edge[i][j] = 0
            # 큰게 하나라도 있으면 불가능한 그래프.
            elif matrix[i][j] > matrix[i][k] + matrix[k][j]:
                result = -1

if result != -1:
    for i in range(n):
        for j in range(i, n):
            if edge[i][j]:
                result += matrix[i][j]
print(result)