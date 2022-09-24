import sys

N = int(sys.stdin.readline())
num = []

for _ in range(N):
    n = list(map(int,sys.stdin.readline().split()))
    num.append(n)



for i in range(1,N):
    for j in range(len(num[i])):
        if j==0:
            num[i][j] = num[i-1][j]+num[i][j]
        elif j==len(num[i])-1:
            num[i][j] = num[i-1][len(num[j])-2]+num[i][j]
        else:
            num[i][j] = max(num[i-1][j],num[i-1][j-1])+num[i][j]



print(max(num[N-1]))

# 