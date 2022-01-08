import sys
input = sys.stdin.readline

def move_block(points):
    min_x, min_y = 6, 6
    for x, y in points:
        # 초록은 y좌표에 대한 x를 5행부터 0행까지 검사
        for row in range(6):
            if not green_area[row][y]:
                min_x = min(min_x, row)
                break
        # 파랑은 x좌표에 대한 y를 5부터 0까지 검사
        for col in range(6):
            if not blue_area[x][col]:
                min_y = min(min_y, col)
                break
    for x, y in points:
        green_area[min_x][y] = 1
        blue_area[x][min_y] = 1



def check_areas():
    flag = 0
    # 녹색영역 검사
    for i in range(5, -1, -1):
        if sum(green_area[i]) == 4:
            
        tmp = 0
        for j in range(4):
            if blue_area[j][i]:
                tmp += 1
        if tmp == 4:
            
    # 파란영역 검사
    if flag:
        relocation()
    pass


def relocation():
    pass


def check_zeroarea():
    flag = 0
    if flag:
        make_stable()
    pass


def make_stable():
    pass


N = int(input())
blocks = [tuple(map(int, input().split())) for _ in range(N)]
# 1, 2 - 가로, 3 - 세로

blue_area = [[0] * 6 for _ in range(4)]
green_area = [[0] * 4 for _ in range(6)]

answer = 0
# 블록 놓기
for t, x, y in blocks:
    sites = []
    sites.append((x, y))
    if t == 2:
        sites.append((x, y + 1))
    else:
        sites.append((x + 1, y))
    move_block(sites)
    check_areas()
    check_zeroarea()
print(answer)