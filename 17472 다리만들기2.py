import sys
input = sys.stdin.readline
from collections import deque
from heapq import heappop, heappush


def find(x):
    if parents[x] == x:
        return x
    parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    x = find(x)
    y = find(y)

    if x > y:
        x, y = y, x
    parents[y] = x


def grouping_continent(x, y):
    q = deque()
    q.append((x, y))
    maps[x][y] = group_num
    while q:
        x, y = q.popleft()
        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and maps[nx][ny] == 1:
                maps[nx][ny] = group_num
                q.append((nx, ny))


def get_dists(row, col):
    for i in range(row):
        left = -1
        for j in range(1, col):
            if maps[i][j - 1] and not maps[i][j]:
                left = j - 1
                left_continent = maps[i][j - 1]
            elif not maps[i][j - 1] and maps[i][j] and not left == -1:
                right_continent = maps[i][j]
                if left_continent != right_continent and not j - 1 - left == 1:
                    if left_continent > right_continent:
                        left_continent, right_continent = right_continent, left_continent
                    if (left_continent, right_continent) not in dists:
                        dists[(left_continent, right_continent)] = j - left - 1
                    else:
                        dists[(left_continent, right_continent)] = min(dists[(left_continent, right_continent)],
                                                                       j - left - 1)


N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
delta = ((0, 1), (1, 0), (0, -1), (-1, 0))
# grouping
group_num = 2
for i in range(N):
    for j in range(M):
        if maps[i][j] == 1:
            grouping_continent(i, j)
            group_num += 1

n = group_num - 2
parents = {i: i for i in range(2, group_num)}
# 거라계산 후 간선정보 갱신
dists = {}
get_dists(N, M)
maps = [row[::-1] for row in zip(*maps)]
get_dists(M, N)

edges = []
for a, b in dists:
    heappush(edges, (dists[(a, b)], a, b))

# kruskal
answer = 0
cnt = 0
while edges:
    dist, a, b = heappop(edges)
    if find(a) != find(b):
        union(a, b)
        answer += dist
        cnt += 1
    if cnt == n - 1:
        break

if cnt != n - 1:
    answer = -1
print(answer)