import sys
sys.stdin.readline


def make_snail(n):
    global t_x,t_y
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    complete_snail = [[0 for _ in range(n)] for _ in range(n)]
    
    # 0,0 에서 초기화
    cnt = n**2
    direction = 0
    x, y = 0, 0
    complete_snail[x][y] = cnt
    cnt -= 1
    # cnt 가 모든 칸에 기록될때까지
    while cnt > 0:

        nx = x + dx[direction]
        ny = y + dy[direction]

        if 0 <= nx < n and 0 <= ny < n and not complete_snail[nx][ny]:
            complete_snail[nx][ny] = cnt
            if cnt==target:
                t_x,t_y = nx,ny
            x, y = nx, ny
            cnt -= 1
        else:       # 진입 못하면 방향 시계방향 전환
            direction = (direction+1) % 4
    return complete_snail


N = int(input())
target = int(input())
t_x,t_y = 0,0
snail = make_snail(N)
for row in snail:
    print(*row)
print(t_x+1,t_y+1)
