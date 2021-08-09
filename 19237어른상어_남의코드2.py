import sys

input = sys.stdin.readline
dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]

n, m, k = map(int, input().split())

maps, shark = [], [[] for _ in range(m)]
for i in range(n):
    maps.append(list(map(int, input().split())))
    for j in range(n):
        if maps[i][j]:
            shark[maps[i][j]-1].extend([i, j])
            maps[i][j] = [maps[i][j], k]

cur_dir = list(map(int, input().split()))
for i in range(m):
    shark[i].append(cur_dir[i])

priority_dir = [[] for _ in range(m)]
idx = -1
for i in range(4*m):
    if i % 4 == 0:
        idx += 1
    priority_dir[idx].append(list(map(int, input().split())))

ans = 0
while True:
    ans += 1
    if ans == 1001:
        print(-1)
        break

    check = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(m):
        # 상어가 살아있을 떄
        if shark[i] != 0:
            x, y, cur_dir, flag = shark[i][0], shark[i][1], shark[i][2], 0
            for j in range(4):
                next_dir = priority_dir[i][cur_dir-1][j]
                nx, ny = x + dx[next_dir], y + dy[next_dir]
                if 0 <= nx < n and 0 <= ny < n:
                    # 이동 가능하면 이동
                    if maps[nx][ny] == 0:
                        flag = 1
                        break
            # 이동 불가능하면 기록한 상어 번호가 나랑 같은 놈한테로 이동.
            if flag == 0:
                for j in range(4):
                    next_dir = priority_dir[i][cur_dir-1][j]
                    nx, ny = x + dx[next_dir], y + dy[next_dir]
                    if 0 <= nx < n and 0 <= ny < n:
                        if maps[nx][ny][0] == i+1:
                            break
            # 그 자리에 있는 상어가 나보다 작은넘이면 죽인다.
            if check[nx][ny]:
                if check[nx][ny] < i+1:
                    shark[i] = 0
                else:
                    shark[check[nx][ny]-1] = 0
            else:
                check[nx][ny] = i+1
                shark[i] = [nx, ny, next_dir]

    # 한바퀴 돌면서 냄새 -1시켜주고 0이면 자리 비워줌.
    for i in range(n):
        for j in range(n):
            if maps[i][j]:
                maps[i][j][1] -= 1
                if maps[i][j][1] == 0:
                    maps[i][j] = 0
    # 상어가 이동한 위치에 최신화 시켜줌.
    for i in range(m):
        if shark[i]:
            x, y = shark[i][0], shark[i][1]
            maps[x][y] = [i+1, k]
    # 상어가 죽은 마리수가 m-1마리면 종료
    if shark.count(0) == m-1:
        print(ans)
        break