import sys
from math import log2, ceil

n = int(sys.stdin.readline())
num0 = list(map(int, sys.stdin.readline().split()))
score1 = [0] * (n + 1)
score2 = [0] * (n + 1)

num1 = list(map(int, sys.stdin.readline().split()))
num2 = list(map(int, sys.stdin.readline().split()))

for i in range(n):
    score1[num1[i]] = i + 1
    score2[num2[i]] = i + 1

height = ceil(log2(n))
tree = [float('inf')] * 2 ** (height + 1)


def minimum(a, b):
    res = float('inf')
    a += 2 ** height - 1
    b += 2 ** height - 1
    while a <= b:
        if a % 2:
            res = min(res, tree[a])
            a += 1
        if b % 2 == 0:
            res = min(res, tree[b])
            b -= 1
        a //= 2
        b //= 2

    return res


def update(k, c):
    idx = 2 ** height + k - 1
    tree[idx] = c
    while idx > 1:
        idx //= 2
        tree[idx] = min(tree[2 * idx], tree[2 * idx + 1])


ans = 1
update(score1[num0[0]], score2[num0[0]])

for i in range(1, n):
    tar = num0[i]
    if minimum(1, score1[tar] - 1) > score2[tar]:
        ans += 1
    update(score1[tar], score2[tar])

print(ans)