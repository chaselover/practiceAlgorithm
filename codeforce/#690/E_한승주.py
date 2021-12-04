import sys
input = sys.stdin.readline
from math import factorial

MOD = int(1e9) + 7
for test in range(int(input())):
    n, k = map(int, input().split())
    a = [0] + sorted(map(int, input().split()))
    cnt, now, total = 1, a[n], 0
    each = []
    for i in range(n - 1, -1 , -1):
        if now == a[i]:
            cnt += 1
        else:
            each.append(cnt)
            total += cnt
            now = a[i]
            cnt = 1
            if total > k:
                break
    last = sum(each[:-1])
    total, pick = each[-1], k - last
    answer = factorial(total) % MOD // (factorial(pick) % MOD * factorial(total - pick) % MOD) % MOD
    print(answer)