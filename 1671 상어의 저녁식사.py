import sys
input = sys.stdin.readline


def dfs(start):
    if visit[start] == 1:
        return 0
    visit[start] = 1
    for i in range(1, n + 1):
        if can_eat[start][i]:
            if d[i] == 0 or dfs(d[i]):
                d[i] = start
                return 1
    return 0


n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
can_eat = [[False] * (n + 1) for _ in range(n + 1)]
d = [0 for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            continue
        if s[i][0] == s[j][0] and s[i][1] == s[j][1] and s[i][2] == s[j][2] and i > j:
            continue
        if s[i][0] >= s[j][0] and s[i][1] >= s[j][1] and s[i][2] >= s[j][2]:
            can_eat[i][j] = True
result = 0
for _ in range(2):
    for i in range(1, n + 1):
        visit = [0 for _ in range(n + 1)]
        dfs(i)
print(d[1:].count(0))