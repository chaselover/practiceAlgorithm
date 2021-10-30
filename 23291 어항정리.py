import sys
input = sys.stdin.readline
from collections import deque


# 달팽이를 만든다. 시작좌표는 
def make_snail():
    row, col = n, n
    if n**2 - N >= n:
        col -= 1
    matrix = [[0] * col for _ in range(row)]
    q = deque()
    q.append((row - 1, col - 1, 0))
    blank_cnt = row * col - N
    start = N - 1
    while q:
        x, y, d = q.popleft()
        matrix[x][y] = arr[start]
        if blank_cnt:
            matrix[x][y] = -1
        for i in range(d, d + 4):
            i %= 4
            nx, ny = x + delta[i][0], y + delta[i][1]
            if 0 <= nx < row and 0 <= ny < col and not matrix[nx][ny]:
                q.append((nx, ny, i))
                if blank_cnt:
                    blank_cnt -= 1
                else:
                    start -= 1
                break
    return matrix


# 최솟값들에 대해 1더해준다.
def engage_minimum():
    min_v = min(arr)
    for i in range(N):
        if arr[i] == min_v:
            arr[i] += 1


def spread(matrix):
    row = len(matrix)
    col = len(matrix[0])
    new_matrix = [[0] * col for _ in range(row)]
    if matrix[-1][-1] == -1:
        row -= 1
        a, b = row - 1, row
        if matrix[a][0] != -1 and matrix[b][0] != -1:
            if matrix[a][0] < matrix[b][0]:
                a, b = b, a
            move = (matrix[a][0] - matrix[b][0]) // 5
            new_matrix[a][0] -= move
            new_matrix[b][0] += move
        for y in range(col):
            if matrix[row][y] == -1:
                break
            for dy in (1, -1):
                ny = y + dy
                if 0 <= ny < col and matrix[row][ny] != -1:
                    if matrix[row][y] - matrix[row][ny] < 5:
                        continue
                    move = (matrix[row][y] - matrix[row][ny]) // 5
                    new_matrix[row][ny] += move
                    new_matrix[row][y] -= move 
    for x in range(row):
        for y in range(col):
            for dx, dy in delta:
                nx, ny = x + dx, y + dy
                if 0 <= nx < row and 0 <= ny < col:
                    if matrix[x][y] - matrix[nx][ny] < 5:
                        continue
                    move = (matrix[x][y] - matrix[nx][ny]) // 5
                    new_matrix[nx][ny] += move
                    new_matrix[x][y] -= move
    if matrix[-1][-1] == -1:
        row += 1
    for i in range(row):
        for j in range(col):
            matrix[i][j] += new_matrix[i][j]
    return matrix


# 달팽이인데 오른족 아래 빈칸 상태면 왼쪽 위부터 행을 순서대로 읽는다.
# 완전한 정사각형이면 왼쪽 아래부터 위로 열을 순대로 읽는다.
def make_arr(matrix):
    row = len(matrix)
    col = len(matrix[0])
    ret = []
    if matrix[-1][-1] == -1:
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == -1:
                    continue
                ret.append(matrix[i][j])
    else:
        for i in range(col):
            for j in range(row - 1, -1, -1):
                ret.append(matrix[j][i])
    return ret


# 행 4개에 분배하기. 배열 4등분 해서 뒤집은 3번째, 2번째, 뒤집은 1번째, 4번째 순.
def make_four_row(arr):
    new_matrix = []
    new_matrix.append(arr[pivot * 2:pivot * 3][::-1])
    new_matrix.append(arr[pivot:pivot * 2])
    new_matrix.append(arr[:pivot][::-1])
    new_matrix.append(arr[pivot * 3:])
    return new_matrix


N, K = map(int, input().split())
arr = list(map(int, input().split()))
pivot = N // 4
for i in range(2, 11):
    if i**2 >= N:
        n = i
        break

delta = ((0, -1), (-1, 0), (0, 1), (1, 0))

answer = 0
while max(arr) - min(arr) > K:
    # 1. 최솟값들에 대해 1씩 넣어준다.
    engage_minimum()
    # 2. 왼쪽을 중앙으로 시작해서 달팽이.   
    # N보다 큰 제곱수의 2차원 배열을 만든 후 남는 칸수만큼 오른쪽에서 offset을 준 뒤 달팽이 하며 감아 들어가면 됨.
    matrix = make_snail()
    # 3. 달팽이에서 인접칸 검사 (a - b) // 5만큼 분배. 동시 분배.
    matrix = spread(matrix)
    # 4. 펼치는건 왼쪽 아래부터 위로
    arr = make_arr(matrix)
    # 첫 N // 4는 뒤집어서 2행, 다음 N// 4는 그대로 1행, 그다음 N // 4는 뒤집어서 0행 마지막 N // 4는 그대로 3행.
    matrix = make_four_row(arr)
    # 6. 물고기 분배 한번 더.
    matrix = spread(matrix)
    # 7. 1열부터 펼치면 3행부터 거꾸로 올라가며 펼치면 됨.
    arr = make_arr(matrix)
    answer += 1
print(answer)
 

#  jh님 코드
def rot_cw(grid):
    h = len(grid); w = len(grid[0])
    G = [[0]*h for i in range(w)]
    for i in range(h):
        for j in range(w):
            G[j][h-i-1] = grid[i][j]
    return G

def rot_180(grid):
    return [row[::-1] for row in grid[::-1]]

def move_fish(multi):
    h = len(multi)
    w = len(multi[0])
    movable = []
    for i in range(h):
        for j in range(w):
            if multi[i][j] == -1: continue
            for ni,nj in (i-1,j),(i+1,j),(i,j-1),(i,j+1):
                if not (0<=ni<h and 0<=nj<w): continue
                if multi[ni][nj] == -1: continue
                d = (multi[i][j] - multi[ni][nj]) // 5
                if d > 0: movable.append((i,j,ni,nj,d))
    for i,j,ni,nj,d in movable:
        multi[i][j]-= d
        multi[ni][nj]+= d

MIS = lambda: map(int,input().split())

n, k = MIS()
box = list(MIS())
op = 0

while max(box) - min(box) > k:
    op+= 1
    # supplement to minimum
    mfish = min(box)
    for i in range(n):
        if box[i] == mfish: box[i]+= 1
    # cw
    multi = [[box[0]], [box[1]]]
    single = box[2:]
    while 1:
        height = len(multi)
        if height > len(single): break
        multi = rot_cw(multi) + [single[:height]]
        single = single[height:]
    # move fish
    for i in range(len(multi)-1):
        multi[i].extend([-1] * len(single))
    multi[-1].extend(single)
    move_fish(multi)
    # linearize
    box = []
    for j in range(len(multi[0])):
        row = [multi[i][j] for i in range(len(multi)-1, -1, -1)]
        box.extend([x for x in row if x != -1])
    # rot 180
    multi = [box]
    for STEP in range(2):
        w = len(multi[0])
        left = rot_180([row[:w//2] for row in multi])
        right = [row[w//2:] for row in multi]
        multi = left + right
    move_fish(multi)
    # linearize
    box = []
    for j in range(len(multi[0])):
        row = [multi[i][j] for i in range(len(multi)-1, -1, -1)]
        box.extend([x for x in row if x != -1])
print(op)

# gk님 코드
import sys
def input():
    return sys.stdin.readline().rstrip()

def check(arr):
    if max(arr) - min(arr) <=K:
        return False
    return True
def push():
    min_value = min(arr[-1])
    for i in range(N):
        if arr[-1][i] == min_value:
            arr[-1][i] += 1
def roll(arr):
    row,col = 1,1
    new_N = N
    time = 0
    while True:
        new_temp = [[-1 for _ in range(new_N-col)] for _ in range(row+1)]

        for y in range(col,new_N):
            new_temp[-1][y-col] = arr[-1][y]

        for y in range(col):
            for x in range(len(arr)):
                new_temp[y][len(arr)-x-1] = arr[x][y]
        new_N = new_N-col
        if time%2:
            row += 1
            col += 1
        time += 1
        arr = [row[:] for row in new_temp]
        row_N = len(new_temp)
        if row_N*(col+1) >N:
            break
    return arr
def outOfbound(x,y,row,col):
    if 0<=x<row and 0<=y<col:
        return False
    return True
def blow():
    row = len(new_arr)
    col = len(new_arr[0])
    temp = [[0 for _ in range(col)] for _ in range(row)]
    for x in range(row):
        for y in range(col):
            if new_arr[x][y] == -1:continue
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if outOfbound(nx,ny,row,col):continue
                if new_arr[nx][ny] == -1:continue
                if new_arr[x][y] - new_arr[nx][ny] >=5:
                    gap = (new_arr[x][y] - new_arr[nx][ny])//5
                    temp[x][y] -= gap
                    temp[nx][ny] += gap
    for x in range(row):
        for y in range(col):
            new_arr[x][y] += temp[x][y]
def flatting(maze):
    temp_arr = [[]]
    row = len(maze)
    col = len(maze[0])
    for y in range(col):
        for x in range(row-1,-1,-1):
            if maze[x][y]==-1:continue
            temp_arr[-1].append(maze[x][y])
    return temp_arr
def spread():
    spread_arr = flatting(new_arr)
    temp = [[-1 for _ in range(N//4)] for _ in range(4)]

    for x in range(4):
        if x%2:
            start_x = N//4*x
            y = 0
            while y<N//4:
                temp[x][y] = spread_arr[-1][start_x+y]
                y += 1
        else:
            y = N//4-1
            if x == 2:
                start_x = 0
            else:
                start_x = N//4*2
            while y>=0:
                temp[x][y] = spread_arr[-1][start_x]
                start_x += 1
                y -= 1
    return temp
                
    
N,K = map(int,input().split())

arr = [list(map(int,input().split()))]
dx = [-1,0,1,0]
dy = [0,-1,0,1]
turn = 0
while check(arr[-1]):
    push()
    new_arr = roll(arr)
    blow()
    new_arr = spread()
    blow()
    arr = flatting(new_arr)
    turn += 1
print(turn)


# as님 코드
from sys import stdin

dx = [1,0]
dy = [0,1]
input = stdin.readline

n,k = map(int, input().split())
board = [[0]*n for _ in range(n)]
board[0] = list(map(int, input().split()))

def solv():
    answer = 0
    while True:
        add_fish()
        stack_rotate()
        modify_fish_count()
        set_board()

        fold_board()
        modify_fish_count()
        set_board()
        answer += 1
        if max(board[0])-min(board[0]) <= k:
            print(answer)
            return
def add_fish():
    global board
    target = min(board[0])
    for idx in range(n):
        if board[0][idx] == target:
            board[0][idx] += 1

    board[1][1] = board[0][0]
    board[0][0] = 0

def stack_rotate():
    while True:
        step = 0
        length = 0
        max_x = search_max_x()

        flag=False
        for y in range(n):
            if not flag:
                if board[0][y] == 0:
                    step += 1
                else:
                    flag = True
                    if board[1][y] != 0:
                        length = 1
            else:
                if board[1][y] != 0:
                    length += 1
                else:
                    break
        if step > 0:
            renew_board(step,max_x)

        if board[0][length+max_x-1] == 0:
            return
        for x in range(max_x):
            for y in range(length):
                board[length-y][length+x],board[x][y] = board[x][y],0

def renew_board(step,max_x):
    global board
    for y in range(step, n):
        for x in range(max_x):
            board[x][y-step],board[x][y] = board[x][y],0
def set_board():
    global board
    new_row = []
    max_x = search_max_x()

    for y in range(n):
        if board[0][y] == 0:
            break
        for x in range(max_x):
            if board[x][y] == 0:
                break
            new_row.append(board[x][y])

    for x in range(max_x):
        board[x] = [0]*n
    board[0] = new_row

def fold_board():
    length = n//2
    for y in range(length):
        board[1][n-y-1], board[0][y] = board[0][y], 0

    renew_board(length,2)

    length = n//4
    for x in range(2):
        for y in range(length):
            board[3-x][n//2-y-1],board[x][y]=board[x][y],0

    renew_board(length, 4)

def modify_fish_count():
    global board

    tmp = [[0]*n for _ in range(n)]
    for x in range(n):
        if board[x][0] == 0:
            break
        for y in range(n):
            if board[x][y] == 0:
                break
            for dir in range(2):
                nx = x + dx[dir]
                ny = y + dy[dir]

                if point_validator(nx,ny):
                    d = abs(board[x][y]-board[nx][ny])//5
                    if board[x][y] > board[nx][ny]:
                        tmp[x][y] -= d
                        tmp[nx][ny] += d
                    elif board[x][y] < board[nx][ny]:
                        tmp[nx][ny] -= d
                        tmp[x][y] += d

    for x in range(n):
        for y in range(n):
            board[x][y] += tmp[x][y]
def point_validator(x,y):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    elif board[x][y] == 0:
        return False
    return True
def search_max_x():
    for y in range(n):
        if board[0][y] == 0:
            continue
        for x in range(n):
            if board[x][y] == 0:
                return x
    return n
solv()
