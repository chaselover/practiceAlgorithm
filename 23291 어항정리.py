import sys
input = sys.stdin.readline
from collections import deque


def make_snail():
    matrix = [[0] * length for _ in range(length)]
    start_x, start_y = length - 1, (N % length) - 1
    if start_y == -1:
        start_y = length - 1
    for i in range(start_y, length):
        matrix[start_x][i] = -1
    q = deque()
    q.append((start_x, start_y, 0))
    start = N - 1
    while q:
        x, y, d = q.popleft()
        matrix[x][y] = arr[start]
        for i in range(d, d + 4):
            i %= 4
            nx, ny = x + delta[i][0], y + delta[i][1]
            if 0 <= nx < length and 0 <= ny < length and not matrix[nx][ny]:
                q.append((nx, ny, i))
                start -= 1
                break
    return matrix


def engage_minimum():
    min_v = min(arr)
    for i in range(N):
        if arr[i] == min_v:
            arr[i] += 1


def spread(matrix):
    row = len(matrix)
    col = len(matrix[0])
    flag = 0
    new_matrix = [[0] * col for _ in range(row)]
    if matrix[row - 1][col - 1] == -1:
        flag = 1
        row -= 1
    for x in range(row):
        for y in range(col):
            for dx, dy in delta:
                nx, ny = x + dx, y + dy
                if 0 <= nx < row and 0 <= ny < col and matrix[x][y] > matrix[nx][ny]:
                    move = (matrix[x][y] - matrix[nx][ny]) // 5
                    new_matrix[nx][ny] += move
                    new_matrix[x][y] -= move

    if flag:
        n, k = row - 1, row
        if matrix[n][0] < matrix[k][0]:
            n, k = k, n
        move = (matrix[n][0] - matrix[k][0]) // 5
        new_matrix[n][0] -= move
        new_matrix[k][0] += move
        row += 1

    for i in range(row):
        for j in range(col):
            matrix[i][j] += new_matrix[i][j]
    return matrix


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


def make_four_row(arr):
    new_matrix = []
    pivot = N // 4
    new_matrix.append(arr[pivot * 2:pivot * 3][::-1])
    new_matrix.append(arr[pivot:pivot * 2])
    new_matrix.append(arr[:pivot][::-1])
    new_matrix.append(arr[pivot * 3:])
    return new_matrix


N, K = map(int, input().split())
arr = list(map(int, input().split()))
for i in range(2, 11):
    if i**2 >= N:
        length = i
        break

delta = ((0, -1), (-1, 0), (0, 1), (1, 0))

answer = 0
while max(arr) - min(arr) > K:
    # 1. 최솟값들에 대해 1씩 넣어준다.
    engage_minimum()
    # 2. 왼쪽을 중앙으로 시작해서 달팽이.   
    # N보다 큰 제곱수의 2차원 배열을 만든 후 남는 칸수만큼 오른쪽에서 offset을 준 뒤 달팽이 하며 감아 들어가면 됨.
    snail = make_snail()
    # 3. 달팽이에서 인접칸 검사 (a - b) // 5만큼 분배. 동시 분배.
    matrix = spread(snail)
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
 