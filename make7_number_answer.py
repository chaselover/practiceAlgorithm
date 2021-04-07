def dfs(lst, start, count, string):
    global result
    if count == 7:
        result.add(string)
        return
 
    for i in range(4):
        ny, nx = start[0] + dy[i], start[1] + dx[i]
        if 0 <= ny < 4 and 0 <= nx < 4:
            dfs(lst, [ny, nx], count + 1, string + lst[ny][nx])
 
 
 
 
T = int(input())
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
for test_case in range(1, T + 1):
    lst = [list(map(str, input().split())) for _ in range(4)]
    result = set()
    for i in range(4):
        for j in range(4):
            dfs(lst, [i, j], 1, lst[i][j])
    print('#{} {}'.format(test_case, len(result)))