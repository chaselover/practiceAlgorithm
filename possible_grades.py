
for test_case in range(1,int(input())+1):
    N = int(input())
    student = []
    for _ in range(N):
        s,d = map(int,input().split())
        student.append([s,d])
    student = sorted(student,key = lambda a : a[0])
    student = sorted(student,key = lambda a : a[1])
    check = [0]*N
    cnt = 0
    while sum(check) != N:
        last = 0
        for i in range(N):
            if student[i][0] >= last and check[i] ==0:
                last = student[i][1]
                check[i] = 1
        cnt+=1
    print("#{} {}".format(test_case, cnt))
        
        

