import sys
input = sys.stdin.readline

N, M = map(int, input().split())
cakes = list(map(int, input().split()))
cakes.sort(key=lambda x: (x%10,x))
cake_cnt = 0
for cake in cakes:
    cnt = cake//10
    if not cake%10:
        if cnt-1 <= M:
            cake_cnt += cnt
            M -= cnt -1
        else:
            cake_cnt += M
            M -= M
    else:
        if cnt <= M:
            cake_cnt += cnt
            M -= cnt
        else:
            cake_cnt += M
            M -= M
print(cake_cnt)
