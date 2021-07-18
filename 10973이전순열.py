import sys
input = sys.stdin.readline

N = int(input())
pers = list(map(int,input().split()))
ans = []

for i in range(N-1,0,-1):
    if pers[i] < pers[i-1]:
        for j in range(N-1,i-1,-1):
            if pers[i-1] >pers[j]:
                pers[i-1],pers[j] = pers[j],pers[i-1]
                ans = pers[:i] + sorted(pers[i:],reverse=True)
                print(*ans)
                break
        if ans:
            break

if not ans:
    print(-1)
