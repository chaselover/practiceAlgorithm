import sys
sys.stdin = open('input.txt')


# 각 행에 몇칸짜리 자리가 있는지 count 해 cells 에 저장합니다.
def count_row(n, target, puzzle):
    sum_seat = 0
    for row in range(n):
        cnt = 0
        cells = []
        for column in range(n):
            if puzzle[row][column]:
                cnt += 1
            else:
                if cnt:
                    cells.append(cnt)
                cnt = 0
        cells.append(cnt)
        sum_seat += cells.count(target)  # 원하는 자리가 있다면 세줍니다.
    return sum_seat


# 글자가 들어갈 자리를 찾을 함수입니다.
def find_seat(size, length):
    n = size
    l = length
    answer = 0

    puzzle = [list(map(int, input().split())) for _ in range(n)]
    answer += count_row(n, l, puzzle)

    # 배열의 열과 행을 뒤집에 한번 더 실시합니다.
    new_puzzle = [k for k in zip(*puzzle)]
    answer += count_row(n, l, new_puzzle)

    return answer


for test in range(1, int(input())+1):
    N, K = map(int, input().split())
    print(f'#{test} {find_seat(N, K)}')
