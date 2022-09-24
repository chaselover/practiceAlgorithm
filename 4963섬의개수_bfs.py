import sys
input = sys.stdin.readline
from collections import deque

dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, -1, 1, -1, -1, 1, 1]

# bfs이용 근처에 1인 육지들을 찾아다니며 전부 0으로 만들어버린다.
def bfs(i, j):
    matrix[i][j] = 0
    queue = deque()
    queue.append([i,j])
    while queue:
        a, b = queue.popleft()
        for k in range(8):
            x = a + dx[k]
            y = b + dy[k]
            if 0 <= x < h and 0 <= y < w and matrix[x][y] == 1:
                matrix[x][y] = 0
                queue.append([x, y])

#
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    matrix = [list(map(int, input().split())) for _ in range(h)]
    cnt = 0
    # 땅이면 팔방탐색하고 섬카운트 하나 늘려.
    for i in range(h):
        for j in range(w):
            if matrix[i][j] == 1:
                bfs(i, j)
                cnt += 1
    print(cnt)