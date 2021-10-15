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


for test in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    parents = {i: i for i in range(1, N + 1)}
    for i in range(M):
        a, b = map(int, input().split())
        if find(a) != find(b):
            union(a, b)
    group = set()
    for i in range(1, N + 1):
        if parents[i] not in group:
            x = find(i)
            if x not in group:
                group.add(x)
    print(f'#{test} {len(group)}')