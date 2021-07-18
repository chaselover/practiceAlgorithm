import itertools as it

T = int(input())
for test in range(T):
    N = int(input())
    s = []
    print("#{}\n1".format(test+1))
    for i in range(N-1):
        s.append(i)

        for j in range(i+2):
            com = list(it.combinations(s,j))
            num = len(com)
            print(num, end = " ")
        print("")