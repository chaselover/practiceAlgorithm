import sys
input = sys.stdin.readline
from collections import deque


def bfs():
    while queue:
        a, b = queue.popleft()
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < n and 0 <= y < m and matrix[x][y] == 0:
                matrix[x][y] = matrix[a][b] + 1
                queue.append([x, y])


m, n = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
queue = deque()
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            queue.append([i, j])

bfs()

isTrue = False
max_value = -2
# j=0이 있으면 완성할 수 없는 상황. -1
# 가장 큰값이 -1
# 모두 익을 때까지 최소 날짜는 matrix의 max값-1(input부터 1이기 때문에)
for i in matrix:
    for j in i:
        if j == 0:
            isTrue = True
        max_value = max(max_value, j)
if isTrue == True:
    print(-1)
elif max_value == -1:
    print(0)
else:
    print(max_value - 1)