import collections as col

T = int(input())
def find_mfn():
    students = list(map(int,input().split()))
    cnt = col.Counter(students)
    mfn = cnt.most_common()
    maxf = mfn[0][1]

    maxes = []

    for i in range(len(students)):
        if mfn[i][1] == maxf:
            maxes.append(mfn[i][0])
        else:
            break

    answer = max(maxes)


for testcase in range(T):
    print("#{} {}".format(testcase+1,answer))