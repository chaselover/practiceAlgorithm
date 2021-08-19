import sys

input = sys.stdin.readline
n, m = map(int, input().split())
a = list(map(int, input().split()))
arr = sorted((v, i + 1) for i, v in enumerate(a))
ans = ''
for _ in range(m):
    i, j, k = map(int, input().split())
    cnt = 0
    for v, idx in arr:
        if i <= idx <= j:
            cnt += 1

        if cnt == k:
            ans += str(v) + '\n'
            break

print(ans)