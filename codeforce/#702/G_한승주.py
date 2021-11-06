import sys
input = sys.stdin.readline

for test in range(int(input())):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    prefix_sum = []
    total = 0
    for num in arr:
        total += num
        prefix_sum.append(total)
    x = list(map(int, input().split()))
    answer = []
    for target in x:
        pos = 0
        if total > 0 and target > total:
            a = target // total
            target -= total * a
            pos += n * a
        if target:
            for idx, num in enumerate(prefix_sum):
                if target == num:
                    answer.append(pos + idx)
                    break
            else:
                answer.append(-1)
        else:
            answer.append(pos - 1)
    print(*answer)