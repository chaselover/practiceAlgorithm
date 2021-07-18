
N = int(input())
num = list(map(int,input().split()))
cnt = 0

for i in range(N):
    for j in range(2,i):
        if num[i]%j==0:
            break
    cnt+=1

print(cnt)