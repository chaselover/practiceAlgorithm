import sys
sys.stdin = open('input.txt')


def move_block():
    check = 0
    new_struck = 0
    for i in range(N):
        for j in range(N):
            if not i == 99 and matrix[i][j] == 1:
                if not matrix[i+1][j]:
                    matrix[i][j], matrix[i+1][j] = matrix[i+1][j], matrix[i][j]
                    check = 1
                elif matrix[i+1][j] == 1:
                    matrix[i][j] = 0
                    check = 1
                else:
                    matrix[i][j],matrix[i+1][j] = 0, 0
                    new_struck += 1
                    check = 1
            elif not i == 0 and matrix[i][j] == 2:
                if not matrix[i-1][j]:
                    matrix[i][j], matrix[i - 1][j] = matrix[i - 1][j], matrix[i][j]
                    check = 1
                elif matrix[i-1][j] == 2:
                    matrix[i][j] = 0
                    check = 1
                else:
                    matrix[i][j],matrix[i-1][j] = 0, 0
                    new_struck += 1
                    check = 1
    return check, new_struck


for test in range(1,11):
    N = int(input())
    # 파란색은 N 쪽으로 빨간색은 S 쪽으로 교착상태의 갯수?
    matrix = [list(map(int, input().split())) for _ in range(N)]
    answer = 0
    flag = 1
    while flag:
        flag, check_point = move_block()
        answer += check_point
    print(f'#{test} {answer}')
