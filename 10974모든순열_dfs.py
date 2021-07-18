from sys import stdin


def dfs(depth):
    if depth == n:
        answer.append([num for num in permutation_deep])
    else:
        for i in range(n):
            if i + 1 in permutation_deep:
                continue
            permutation_deep[depth] = i + 1
            dfs(depth + 1)
            permutation_deep[depth] = 0

answer = []
n = int(stdin.readline())
permutation_deep = [0] * n
dfs(0)

for case in answer:
    print(*case)