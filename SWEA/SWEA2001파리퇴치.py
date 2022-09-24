import sys
sys.stdin = open('input.txt')


# 파리채로 쳐 죽입니다.
def count_kill_flies(x,y, fly_killer_size, matrix):
    kill = 0
    for i in range(x, x+fly_killer_size):
        kill += sum(matrix[i][y:y+fly_killer_size])
    return kill


def kill_flies(matrix_size, fly_killer_size):
    matrix = [list(map(int, input().split())) for _ in range(matrix_size)]

    # 파리채로 칠 범위를 지정합니다.(왼쪽 위 idx)
    kill_sum = []
    for i in range(matrix_size-fly_killer_size+1):
        for j in range(matrix_size-fly_killer_size+1):
            init_x, init_y = i, j
            kill_sum.append(count_kill_flies(init_x, init_y, fly_killer_size, matrix))
    return max(kill_sum)


for test in range(1, int(input())+1):
    N, M = map(int, input().split())
    print(f'#{test} {kill_flies(N, M)}')
