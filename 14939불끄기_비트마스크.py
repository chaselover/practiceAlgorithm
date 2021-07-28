table = []
for i in range(10):
    temp = list(input())
    for j in range(10):
        if temp[j] == 'O':
            temp[j] = True #True: 불 켜져있음
            continue
        temp[j] = False #False: 불 꺼져있음
    table.append(temp)

dx = [-1, 1, 0, 0, 0]
dy = [0, 0, 0, -1, 1]
ans = 101
for f in range(1<<10):
    a = []
    for i in range(10):
        a.append(table[i][:])
    cnt = 0

    for i in range(10):
        if f & (1<<i): #i번째 스위치를 누른 경우
            cnt += 1
            for k in range(5):
                nx = i + dx[k]
                ny = 0 + dy[k]
                if 0 <= nx <= 9 and 0 <= ny <= 9:
                    a[ny][nx] = not a[ny][nx]

    for i in range(1, 10): #y좌표
        for j in range(10): #x좌표
            if not a[i-1][j]: #바로 윗 전등이 켜져있다면 스위치를 눌러줘야됨
                continue
            for k in range(5):
                nx = j + dx[k]
                ny = i + dy[k]
                if 0 <= nx <= 9 and 0 <= ny <= 9:
                    a[ny][nx] = not a[ny][nx]
            cnt += 1


    can = True
    for i in range(10):
        if a[9][i] == True:
            can = False

    if can:
        ans = min(cnt, ans)

print(ans if ans != 101 else -1)