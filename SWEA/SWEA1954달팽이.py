import sys
sys.stdin = open('input.txt')


def make_snail(n):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    complete_snail = [[0 for _ in range(n)] for _ in range(n)]

    # 0,0 에서 초기화
    cnt = 1
    direction = 0
    x, y = 0, 0
    complete_snail[x][y] = cnt

    # cnt 가 모든 칸에 기록될때까지
    while cnt != N**2:

        nx = x + dx[direction]
        ny = y + dy[direction]

        if 0 <= nx < N and 0 <= ny < N and not complete_snail[nx][ny]:
            cnt += 1
            complete_snail[nx][ny] = cnt
            x, y = nx, ny
        else:       # 진입 못하면 방향 시계방향 전환
            direction = (direction+1) % 4

    return complete_snail


for test in range(1, int(input())+1):
    N = int(input())
    snail = make_snail(N)
    print(f'#{test}')
    for i in range(N):
        print(*snail[i])
