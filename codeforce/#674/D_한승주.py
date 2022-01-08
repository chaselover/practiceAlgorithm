import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
segments = {0}
cnt, tmp = 0, 0
for i in range(n):
    tmp += a[i]
    if tmp in segments:
        cnt += 1
        segments = {0}
        tmp = a[i]
    segments.add(tmp)
print(cnt)
