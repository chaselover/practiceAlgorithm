N = int(input())
Si = []
Ti = []
check = [False] * N

for _ in range(N):
    i,j = map(int,input().split())
    Si.append(i)
    Ti.append(j)


cnt = 0

while sum(check) != N:
    finish = 0
    for i in range(N):
        if Si[i] >= finish and check[i] == False:
            finish = Ti[i]
            check[i] = True
    cnt+=1

print(cnt)