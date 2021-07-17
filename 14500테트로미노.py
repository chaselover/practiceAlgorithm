import sys
input = sys.stdin.readline

# 사방
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

# 빠큐모양 고려해야될 4개.
mfinger = [[[0, 1], [0, 2], [-1, 1]], [[0, 1], [0, 2], [1, 1]], 
[[1, 0], [2, 0], [1, 1]], [[1, 0], [1, -1], [2, 0]]]


n, m = map(int, input().split())
s = []
# check박스
visit = [[0] * m for _ in range(n)]

# DFS 들어가고 나오고 max값만 비교.
# 먼가 이거 상하향은 고려안해도 될것 같은 느낌인데..
# (2방향으로 DFS 하고 L자 삐져나오는 모양이랑 미음자 따로 계산해주는 게 날듯. 3가지 케이스니까.)
def dfs(x, y, cnt, num):
    global result
    if cnt == 4:
        result = max(result, num)
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and visit[nx][ny] == 0:
            visit[nx][ny] = 1
            dfs(nx, ny, cnt + 1, num + s[nx][ny])
            visit[nx][ny] = 0

# 빠큐값만 따로계산해서 max치 비교(빠큐는 DFS로 탐색되는 모양이 아니기 때문.)
def middlefinger(x, y):
    global result
    for i in mfinger:
        try:
            num = s[x][y] + s[x + i[0][0]][y + i[0][1]] + s[x + i[1][0]][y + i[1][1]] + s[x + i[2][0]][y + i[2][1]]
        except:
            num = 0
        result = max(result, num)

# matrix 입력
for i in range(n):
    s.append(list(map(int, input().split())))

# 탐색 전 result 초기화
result = 0
# 모든 점에 대해 dfs및 빠큐탐색 진행.
for i in range(n):
    for j in range(m):
        visit[i][j] = 1
        dfs(i, j, 1, s[i][j])
        visit[i][j] = 0
        middlefinger(i, j)
print(result)