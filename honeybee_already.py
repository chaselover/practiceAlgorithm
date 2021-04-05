
def sumCheck():
    if sum(queue)<=C:
        a = map(lambda x : x**2,queue)
        answers.append(sum(a))
    else:
        sorted_queue = sorted(queue)
        check[0]*M
        



    return answers





for test_case in range(1,int(input())+1):
    N,M,C = map(int,input().split())
    honey = []
    sum = 0
    queue = []
    answers = []
    for _ in range(N):
        row = list(map(int, input().split()))
        honey.append(row)
    for i in range(N):
        for j in range(N-M+1):
            queue.append(honey[i][j])
            if len(queue) > M:
                queue.pop(0)
            if len(queue) ==M:
                sumCheck()

    print("#{} {}".format(test_case,max(answers)))
