import sys
input = sys.stdin.readline

N = int(input())
deaguen = [input().rstrip() for _ in range(N)]
check = {car: False for car in deaguen}
youngsik = [input().rstrip() for _ in range(N)]

idx = 0
cnt = 0
for last in youngsik:
    while check[deaguen[idx]]:
        idx += 1
    if last == deaguen[idx]:
        idx += 1
    else:
        cnt += 1
    check[last] = True
print(cnt)