import sys
input = sys.stdin.readline


def dfs(depth, weight):
    if depth == N:
        return 1
    ret = 0
    for i in range(N):
        next_weight = weight - K + a[i]
        if not check[i] and next_weight >= 500:
            check[i] = True
            ret += dfs(depth + 1, next_weight)
            check[i] = False
    return ret

N, K = map(int, input().split())
a = list(map(int, input().split()))
check = {i: False for i in range(N)}

print(dfs(0, 500))