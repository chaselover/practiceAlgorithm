import sys
sys.stdin = open('input.txt')


test = int(input())
for test in range(1, test+1):
    n = int(input())
    pascals = [[] for _ in range(n)]         #* *삼각형을 그릴 틀*
    pascals[0].append(1)                     #* *첫열은 그냥 삽입*
    for i in range(1, n):                    #* *2열부터 그릴 것임.*
        stack = pascals[i-1][:]              #* *1열(i-1열을 복사)*
        pascals[i].append(1)                 #* *첫인자 삽입*
        for j in range(1, i):                #* *다음인자부터는 i-1열의 인자를 하나하나 pop 해주며 다음에 나올 인자와의 합을 i열에 삽입해줌.*
            pascals[i].append(stack.pop()+stack[-1])
        pascals[i].append(1)             #* *마지막 인자 삽입.*
                                             #* *어차피 좌우대칭이므로 기존 파스칼 삼각형의 규칙인*                                    #* *i-1열의 0,1번째 인자의 합이 i열 1인자가 될 필요 없음
    print(f'#{test}')                        #* *stack 을 이용 i-1열의 i,i-1번째 인자가 i열의 1번 인자가 되는 방식.*
    for pas in pascals:
        print(*pas)
