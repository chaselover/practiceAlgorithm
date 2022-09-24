import sys
sys.stdin = open('input.txt')


def find_max(arr):
    max_sum = 0
    # 행 조사
    for row in range(100):
        sum_row = sum(arr[row])
        if max_sum < sum_row:
            max_sum = sum_row
    # 열 조사
    for column in range(100):
        sum_column = sum([k for k in zip(*arr)][column])
        if max_sum < sum_column:
            max_sum = sum_column

    # 대각선 조사
    sum_diagonal1 = 0
    sum_diagonal2 = 0
    for i in range(100):
        sum_diagonal1 += arr[i][i]
        sum_diagonal2 += arr[i][99-i]
    if max_sum < sum_diagonal1:
        max_sum = sum_diagonal1
    if max_sum < sum_diagonal2:
        max_sum = sum_diagonal2

    return max_sum


for _ in range(10):
    test = int(input())
    matrix = [list(map(int, input().split())) for _ in range(100)]
    print(f'#{test} {find_max(matrix)}')
