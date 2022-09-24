n,m=map(int,input().split())

comb = 1
for i in range(n-m+1,n+1):
    comb *= i
for i in range(1,m+1):
    comb = comb // i
print(comb)