import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def dfs(x, y):
    # 이미 다른 조사에서 완료된 지점이면 패스
    if dp_dist[x][y]: 
        return dp_dist[x][y]
    # 조사 안됐으면 1부터 시작.
    dp_dist[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            # 거리가 작으면 들어간다. 약간 다익스트라를 쓰는 느낌.
            if forest[x][y] < forest[nx][ny]:
                dp_dist[x][y] = max(dp_dist[x][y], dfs(nx, ny) + 1)
    return dp_dist[x][y]


n = int(input())
forest = [list(map(int, input().split())) for i in range(n)]
dp_dist = [[0] * n for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

# 모든 점에서 조사.
max_move = 0
for i in range(n):
    for j in range(n):
        max_move = max(max_move, dfs(i, j))
print(max_move)