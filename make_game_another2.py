def dfs(x, y, memo, d):
    global ans
    if ans == 'YES': return
 
    tgt = arr[x][y]
    if tgt == '@':
        ans = 'YES'
        return
 
    wrap = (x, y, memo, d)
    if wrap in visited: return
    visited[wrap] = True
    if tgt in direction:
        if tgt == '<': d = 0
        elif tgt == '>': d = 1
        elif tgt == '^': d = 2
        elif tgt == 'v': d = 3
 
        elif tgt == '_': d = 1 if memo == 0 else 0
        elif tgt == '|': d = 3 if memo == 0 else 2
 
    elif tgt.isdigit(): memo = int(tgt)
    elif tgt == '+': memo = (memo + 1) % 16
    elif tgt == '-': memo = (memo - 1) % 16
 
    if tgt == '?':
        if arr[(x + 1) % R][y] == '@' or arr[(x - 1) % R][y] == '@' \
                or arr[x][(y + 1) % C] == '@' or arr[x][(y - 1) % C] == '@':
            ans = 'YES'
            return
 
        for i in range(4):
            dx, dy = delta[i]
            tx, ty = (x + dx) % R, (y + dy) % C
            dfs(tx, ty, memo, i)
 
    else:
        dx, dy = delta[d]
        dfs((x + dx) % R, (y + dy) % C, memo, d)
 
 
direction = '<>^v_|'
delta = ((0, -1), (0, 1), (-1, 0), (1, 0))
TCs = int(input())
for T in range(1, TCs+1):
    R, C = map(int, input().split())
    arr = []
 
    atExists = False
    for i in range(R):
        arr.append(list(input()))
        if '@' in arr[i]: atExists = True
 
    for i in range(R):
        for j in range(C):
            if arr[i][j] == '@':
                if arr[(i - 1) % R][j] != 'v' and arr[(i - 1) % R][j] in direction \
                        and arr[(i + 1) % R][j] != '^' and arr[(i + 1) % R][j] in direction \
                        and arr[i][(j - 1) % C] != '>' and arr[i][(j - 1) % C] in direction \
                        and arr[i][(j + 1) % C] != '<' and arr[i][(j + 1) % C] in direction:
                    atExists = False
                    break
 
    ans = 'NO'
    print(f'#{T}', end=' ')
    if atExists:
        visited = {}
        dfs(0, 0, 0, 1)
 
    print(ans)