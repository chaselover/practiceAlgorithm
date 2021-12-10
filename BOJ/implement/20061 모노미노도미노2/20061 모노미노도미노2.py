import sys
input = sys.stdin.readline

def move_block(t, x, y):
    if t == 1:
        for row in range(6):
            if green_area[row][y]:
                green_area[row - 1][y] = 1
                break
        else:
            green_area[5][y] = 1
        for col in range(6):
            if blue_area[x][col]:
                blue_area[x][col - 1] = 1
                break
        else:
            blue_area[x][5] = 1
    elif t == 2:
        for row in range(6):
            if green_area[row][y] or green_area[row][y + 1]:
                green_area[row - 1][y], green_area[row - 1][y + 1] = 1, 1
                break
        else:
            green_area[5][y], green_area[5][y + 1] = 1, 1
        for col in range(6):
            if blue_area[x][col]:
                blue_area[x][col - 1], blue_area[x][col - 2] = 1, 1
                break
        else:
            blue_area[x][5], blue_area[x][4] = 1, 1
    else:
        for row in range(6):
            if green_area[row][y]:
                green_area[row - 1][y], green_area[row - 2][y] = 1, 1
                break
        else:
            green_area[5][y], green_area[4][y] = 1, 1
        for col in range(6):
            if blue_area[x][col] or blue_area[x + 1][col]:
                blue_area[x][col - 1], blue_area[x + 1][col - 1] = 1, 1
                break
        else:
            blue_area[x][5], blue_area[x + 1][5] = 1, 1


def check_areas():
    global answer
    # 녹색영역 검사
    remove_line = []
    for i in range(5, -1, -1):
        if sum(green_area[i]) == 4:
            answer += 1
            for j in range(4):
                green_area[i][j] = 0
            remove_line.append(i)

    remove_line.reverse()
    for line in remove_line:
        for i in range(line, 0, -1):
            for j in range(4):
                green_area[i][j] = green_area[i - 1][j]

    for i in range(4):
        green_area[0][i] = 0
    # 파란영역 검사
    remove_line = []
    for i in range(5, -1, -1):
        tmp = 0
        for j in range(4):
            if blue_area[j][i]:
                tmp += 1
        if tmp == 4:
            answer += 1
            for j in range(4):
                blue_area[j][i] = 0
            remove_line.append(i)
    remove_line.reverse()
    for line in remove_line:
        for i in range(line, 0, -1):
            for j in range(4):
                blue_area[j][i] = blue_area[j][i - 1]
    for i in range(4):
        blue_area[i][0] = 0


def check_zeroarea():
    global green_area
    green_zeros = 0
    blue_zeros = 0
    for i in range(2):
        for j in range(4):
            if green_area[i][j] == 1:
                green_zeros += 1
                break
        for j in range(4):
            if blue_area[j][i] == 1:
                blue_zeros += 1
                break
    for _ in range(green_zeros):
        green_area.pop()
        green_area = [[0, 0, 0, 0]] + green_area
    for _ in range(blue_zeros):
        for i in range(4):
            for j in range(5, 0, -1):
                blue_area[i][j] = blue_area[i][j - 1]
            blue_area[i][0] = 0


N = int(input())
blocks = [tuple(map(int, input().split())) for _ in range(N)]
# 1, 2 - 가로, 3 - 세로

blue_area = [[0] * 6 for _ in range(4)]
green_area = [[0] * 4 for _ in range(6)]

answer = 0
# 블록 놓기
for t, x, y in blocks:
    move_block(t, x, y)
    check_areas()
    check_zeroarea()

cnt = 0
for i in range(4):
    for j in range(6):
        if blue_area[i][j]:
            cnt += 1
for i in range(6):
    for j in range(4):
        if green_area[i][j]:
            cnt += 1
print(answer)
print(cnt)
