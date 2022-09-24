N = int(input())


for i in range(1,N+1):
    cnt = 0
    number = i
    if i>100:
        if i//100 ==3 or i//100 ==6 or i//100 ==9:
            cnt +=1
        i = i - i//100 *100
    if i>10:
        if i//10 ==3 or i//10 ==6 or i//10 ==9:
            cnt +=1
        i = i - i//10 *10
    if i == 3 or i ==6 or i ==9:
        cnt +=1
    if cnt !=0:
        for _ in range(cnt):
            print("-", end ="")
        print(end = " ")
    else:
        print(number, end=" ")