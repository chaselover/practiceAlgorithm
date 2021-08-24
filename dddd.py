import sys
sys.stdin = open('input.txt')


# 열 인덱스로 순열을 만들면 세로로 같은 줄에서 두 개 이상의 숫자를 고를 수 없다는 조건을 만족할 수 있다.
# swea 제한시간 초과 남
# 백트래킹 조건을 추가 - 합이 최소값을 넘으면 더이상 찾지 않도록 설정

def get_per_sum(i, sum_nums):
    global min_sum


    

    # 백트래킹 조건: 현재 합이 최소합을 넘으면 -> 볼 필요 없음.
    if sum_nums > min_sum:
        return

    if i == n:  # 순열 완성  P = [1, 0, 2]

        # sums.append(sum)
        min_sum = min(sum_nums, min_sum)
        return

    else:
        for j in range(i, n):  # 자신부터 오른쪽 원소와 교환
            P[i], P[j] = P[j], P[i]
            get_per_sum(i + 1, sum_nums + arr[i][P[i]])
            P[i], P[j] = P[j], P[i]


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    P = [i for i in range(n)]  # 열 인덱스 순열을 만들 리스트 P = [0, 1, 2]
    # sums = []  # 합을 모을 리스트
    min_sum = float('inf')  # 무한대
    get_per_sum(0, 0)

    print(f'#{tc} {min_sum}')