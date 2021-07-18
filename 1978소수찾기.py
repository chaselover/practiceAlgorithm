
A,B = map(int,input().split())

for i in range(A,B+1):
    if i == 1:
        continue
    elif i == 2:
        print(i)
        continue
    else:
        for j in range(2,i):
            if i%j==0:
                break
            if j==i-1:
                print(i)
