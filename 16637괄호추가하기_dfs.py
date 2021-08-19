from math import inf
from sys import stdin


def dfs(idx, sub_total):
    global answer

    if idx == len(op):
        answer = max(answer, int(sub_total))
        return

    # (3 + 8) * 7 - 9 * 2 부터 시작.
    first = str(eval(sub_total + op[idx] + nums[idx + 1]))
    dfs(idx + 1, first)

    if idx + 1 < len(op):
        # 3 + (8 * 7) - 9 * 2 부터 시작
        second = str(eval(nums[idx + 1] + op[idx + 1] + nums[idx + 2]))
        second = str(eval(sub_total + op[idx] + second))
        # op를 2개 소모했으므로 idx + 2
        dfs(idx + 2, second)


if __name__ == '__main__':
    n = int(stdin.readline())
    expression = stdin.readline().rstrip()
    nums, op = [], []
    answer = -inf

    for e in expression:
        nums.append(e) if e.isdigit() else op.append(e)

    dfs(0, nums[0])
    print(answer)


