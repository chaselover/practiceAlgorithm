INF = 1_000_000
N = int(input())
T = [INF] * (N+N)


def update(i, v):
    i = i + N
    p = i // 2
    T[i] = v
    while p and T[i] < T[p]:
        T[p] = T[i]
        i, p = p, p // 2


def get(i, j):
    r = 1_000_000
    i, j = i + N, j + N
    while i <= j:
        if i&1:
            r = min(T[i], r)
            i += 1
        if not j&1:
            r = min(T[j], r)
            j -= 1
        i, j = i//2, j//2
    return r


B = [0] * (N+1)
C = [0] * (N+1)

A = list(map(int, input().split()))
i = 0
for b in map(int, input().split()):
    i += 1
    B[b] = i
i = 0
for c in map(int, input().split()):
    i += 1
    C[c] = i
c = N
for x in A:
    c -= get(1-1, B[x]-1) < C[x]
    update(B[x]-1, C[x]-1)
print(c)