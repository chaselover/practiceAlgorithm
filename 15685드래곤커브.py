import sys
input = sys.stdin.readline


dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

n = int(input())
matrix = [[0 for _ in range(101)] for _ in range(101)]

for i in range(n):
    x, y, d, g = map(int, input().split())
    # 최초 노드 x,y, 전체노드, 추가되는 노드방향성(증감성) 초기화.
    matrix[x][y] = 1
    next_direction = [d]
    cur_direction = [d]
    # 세대수만큼 반복.
    for generation in range(g + 1):
        # 각 노드의 방향성에 따른 증감을 반영하며 드래곤 커브 실시.
        for direction in cur_direction:
            nx = x + dx[direction]
            ny = y + dy[direction]
            matrix[nx][ny] = 1
            x,y = nx,ny
        # 세대가 지날수록 각 노드들은 방향성이 1만큼 증가. 0~3순환
        # 다음 세대에 진행할 노드방향성.
        cur_direction = [(cur_direction + 1) % 4 for cur_direction in next_direction]
        # 세대 순환은 가장 마지막에 도착한 노드부터 출발.
        cur_direction.reverse()
        # 다음 세대 추가 완료.
        next_direction = next_direction + cur_direction

# 정사각형 탐색.
cnt = 0
for i in range(100):
    for j in range(100):
        if matrix[i][j] and matrix[i][j + 1] and matrix[i + 1][j] and matrix[i + 1][j + 1]:
            cnt += 1
print(cnt)