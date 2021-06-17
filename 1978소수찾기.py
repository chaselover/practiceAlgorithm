
N = int(input())
num = list(map(int,input().split()))
cnt = 0

for i in range(N):
    if num[i] == 1:
        continue
    elif num[i] == 2:
        cnt+=1
        continue
    else:
        for j in range(2,num[i]):
            if num[i]%j==0:
                break
            if j==num[i]-1:
                cnt+=1

print(cnt)