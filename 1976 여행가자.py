import sys
input = sys.stdin.readline


def union(x, y):
    x = find(x)
    y = find(y)

    if x > y:
        x, y = y, x
    parents[y] = x


def find(x):
    if parents[x] == x:
        return x
    parents[x] = find(parents[x])
    return parents[x]


N = int(input())
M = int(input())
edges = [list(map(int, input().split())) for _ in range(N)]
plan = list(map(lambda x: int(x) - 1, input().split()))
parents = {i: i for i in range(N)}
for i in range(N):
    for j in range(N):
        if edges[i][j] and find(i) != find(j):
            union(i, j)

pivot = find(plan[0])
for city in plan[1:]:
    if find(city) != pivot:
        print('NO')
        break
else:
    print('YES')