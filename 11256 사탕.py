import sys
input = sys.stdin.readline

for _ in range(int(input())):
    J, N = map(int, input().split())
    cases = []
    for i in range(N):
        R, C = map(int, input().split())
        cases.append(R*C)
    cases.sort(reverse=True)
    cnt = 0
    for case in cases:
        J -= case
        cnt += 1
        if J <= 0:
            print(cnt)
            break
