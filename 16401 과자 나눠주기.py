import sys
input = sys.stdin.readline

M, N = map(int, input().split())
L = list(map(int, input().split()))
start, end = 1, max(L)
answer = 0
while start <= end:
    target_l = (start + end) // 2
    if sum([each_l // target_l for each_l in L]) >= M:
        answer = target_l
        start = target_l + 1
    else:
        end = target_l - 1
print(answer)