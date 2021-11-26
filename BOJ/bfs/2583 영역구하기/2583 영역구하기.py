m, n, k = map(int, input().split())
s = [[0] * n for i in range(m)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
cnt = []
for i in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for j in range(y1, y2):
        for k in range(x1, x2):
            s[j][k] = 1
for i in range(m):
    for j in range(n):
        if s[i][j] == 0:
            count = 1
            s[i][j] = 1
            queue = [[i, j]]
            while queue:
                x, y = queue[0][0], queue[0][1]
                del queue[0]
                for k in range(4):
                    x1 = x + dx[k]
                    y1 = y + dy[k]
                    if 0 <= x1 < m and 0 <= y1 < n and s[x1][y1] == 0:
                        s[x1][y1] = 1
                        count += 1
                        queue.append([x1, y1])
            cnt.append(count)
print(len(cnt))
cnt.sort()
for i in cnt:
    print(i, end=' ')