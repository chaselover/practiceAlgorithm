T = int(input())



for test_case in range(1, T + 1):
    edge = list(input())
    Numerator = 1
    Demorator = 1

    for i in range(len(edge)):
        if edge[i] == "L":
            Demorator += Numerator
        else:
            Numerator += Demorator

    print("#{} {} {}".format(test_case, Numerator, Demorator))