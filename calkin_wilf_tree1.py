T = int(input())



for test_case in range(1, T + 1):
    P = list(input())
    Q = list(input())

    for i in range(len(P)):
        if len(Q) == len(P)+1 and Q[-1] == "a":
            if P[i] == Q[i]:
                answer = 1
                continue
            else:
                answer = 0
        else:
            answer = 0
            break
    if answer == 1:
        print("#{} N".format(test_case))
    else:
        print("#{} Y".format(test_case))


    