n = int(input())

matrix=[[1]*10 for _ in range(n)]

for i in range(1,n):
    sum=0
    for j in range(10):
        for k in range(j+1):
            matrix[i][j] += matrix[i-1][k]
            sum += matrix[i-1][k]

if n==1:
    print(10)
else:
    print(sum%10007)