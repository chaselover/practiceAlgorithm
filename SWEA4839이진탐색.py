import sys
sys.stdin = open('input.txt')


# 좌우로 부터 조여 몇번 조여야 원하는 n값에 도달하는지 체크합니다.
def binary_search(P, n):
    left = 1
    right = P
    cnt = 0
    while left <= right:
        mid = (left + right)//2
        cnt += 1
        if mid < n:
            left = mid
        elif mid > n:
            right = mid
        else:
            break
    return cnt


def find_winner():
    P, A, B = map(int, input().split())
    if P == 1 or A == B:
        return 0
    a_cnt = binary_search(P, A)
    b_cnt = binary_search(P, B)
    # 체크한 횟수를 비교해 결과를 반환합니다.
    if a_cnt > b_cnt:
        return 'B'
    elif b_cnt > a_cnt:
        return 'A'
    else:
        return 0


for test in range(1, int(input())+1):
    print(f'#{test} {find_winner()}')


