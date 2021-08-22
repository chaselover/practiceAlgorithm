# https://www.acmicpc.net/problem/14428
# Segment Tree

from sys import stdin

n = int(stdin.readline().strip())
seq = [0] + list(map(int, stdin.readline().split()))


def helper(first, second):
    return min(sorted([first, second]), key=lambda x: seq[x])


# Initialize Segment Tree
tree = [0 for _ in range(n)] + [i for i in range(1, n + 1)]
for i in range(n - 1, -1, -1):
    # idx_l = tree[2 * i]
    # idx_r = tree[2 * i ^ 1]
    # if seq[idx_l] <= seq[idx_r]:
    #     tree[i] = idx_l
    # else:
    #     tree[i] = idx_r
    tree[i] = helper(tree[2 * i], tree[2 * i ^ 1])


def query(left, right):
    left += n - 1
    right += n - 1
    res = tree[left]
    while left < right:
        if left % 2 == 1:
            res = helper(res, tree[left])
            left += 1
        if right % 2 == 0:
            res = helper(res, tree[right])
            right -= 1
        left //= 2
        right //= 2

    if left == right:
        res = helper(res, tree[right])

    return res


def update(pos, new):
    seq[pos] = new
    pos += n - 1
    while pos > 1:
        tree[pos // 2] = helper(tree[pos], tree[pos ^ 1])
        pos //= 2


m = int(stdin.readline().strip())
for _ in range(m):
    a, b, c = map(int, stdin.readline().split())
    if a == 1:
        update(b, c)
        # print(seq)
        # print(tree)

    else:
        print(query(b, c))