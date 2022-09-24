import sys
input = sys.stdin.readline

N = int(input())
s = list(map(int,input().split()))
flag = 0
for i in range(1,N):
    if s[-i] > s[-i-1]:
        for j in range(1,i):
            if s[-i-1] < s[-j]:
                s[-i-1],s[-j] = s[-j],s[-i-1]
                s = s[:-i] + sorted(s[-i:])
                flag = 1
                break
    if flag:
        print(*s)
        break

if not flag:
    print(-1)



12345
12354
12534
12543
15234
15243
15324
15342
15423
15432
