import sys
sys.stdin = open('input.txt')


def color_areas(color_cnt):
    # 색을 칠할 칠판입니다.
    matrix = [[[] for _ in range(10)] for _ in range(10)]
    for _ in range(color_cnt):
        r1, c1, r2, c2, color = map(int, input().split())
        # 내 색깔이 칸에 안칠해져있다면 칠합니다.
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                if not color in matrix[i][j]:
                    matrix[i][j].append(color)
    # 원하는 색이 칠해져있다면 세줍니다.
    answer = 0
    for i in range(10):
        for j in range(10):
            if len(matrix[i][j]) == 2:
                answer += 1
    return answer


for test in range(1, int(input())+1):
    N = int(input())
    print(f'#{test} {color_areas(N)}')
