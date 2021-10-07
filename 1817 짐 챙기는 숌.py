import sys
input = sys.stdin.readline

N, M = map(int, input().split())
weights = list(map(int, input().split()))
box, cnt = M, 1
for weight in weights:
    if box - weight >= 0:
        box -= weight
    else:
        cnt += 1
        box = M - weight
if not N: cnt = 0
print(cnt)