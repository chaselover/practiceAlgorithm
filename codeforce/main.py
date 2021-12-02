import sys
input = sys.stdin.readline

for test in range(1, int(input()) + 1):
    N, B, S, P, D = map(int, input().split())
    # B는 기준 0글번호, 1글제목, 2 조회수
    # D가 0이면 오름차순, 1이면 내림차순
    table = [input().rstrip()[1:-1].split(', ') for _ in range(N)]
    if B == 0:
        table.sort()
    elif B == 1:
        table.sort(key=lambda x: (x[1], int(x[0])))
    else:
        table.sort(key=lambda x: (int(x[2]), int(x[0])))
    
    if D == 1:
        table = table[::-1]
    table = table[S * P - P: P * S]
    print(f'#{test}', end=' ')
    for i in range(S):
        print(table[i][0], end=' ')
    print()