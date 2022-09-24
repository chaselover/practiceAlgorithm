from collections import deque
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
for tc in range(1,int(input()) + 1):
    R, C = map(int, input().split())
    data = [input() for _ in range(R)]
    visit = [[[[True] * 16 for j in range(4)]  for i in range(C)] for _ in range(R)]
    ans = False
    memory = 0
    Q = deque()
    Q.append((0, 0, 0))
    visit[0][0][0][memory] = False
    while Q:
        x, y, direction = Q.popleft()
        chk = False
        if '0' <= data[x][y] <= '9':
            memory = int(data[x][y])
        elif data[x][y] == '+':
            memory = (memory + 1) % 16
        elif data[x][y] == '-':
            memory = (memory - 1) % 16
        elif data[x][y] == '<':
            direction = 2
        elif data[x][y] == '>':
            direction = 0
        elif data[x][y] == '^':
            direction = 3
        elif data[x][y] == 'v':
            direction = 1
        elif data[x][y] == '_':
            if memory == 0:
                direction = 0
            else:
                direction = 2
        elif data[x][y] == '|':
            if memory == 0:
                direction = 1
            else:
                direction = 3
        elif data[x][y] == '?':
            chk = True
        elif data[x][y] == '@':
            ans = True
            Q.clear()
        if chk:
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                nx %= R
                ny %= C
                if visit[nx][ny][i][memory]:
                    visit[nx][ny][i][memory] = False
                    Q.append((nx, ny, i))
        else:
            nx, ny = x + dx[direction], y + dy[direction]
            nx %= R
            ny %= C
            if visit[nx][ny][direction][memory]:
                visit[nx][ny][direction][memory] = False
                Q.append((nx, ny, direction))
    if ans:
        print('#{} YES'.format(tc))
    else:
        print('#{} NO'.format(tc))