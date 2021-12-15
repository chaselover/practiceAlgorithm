import sys
input = sys.stdin.readline

for test in range(int(input())):
    n = int(input())
    arr = list(input().split())
    answer = ''
    answer += arr[0]
    flag = 0
    for i in range(1, n - 2):
        if answer[-1] != arr[i][0]:
            answer += arr[i]
            flag = 1
        else:
            answer += arr[i][1]
    if flag:
        print(answer)
    else:
        print(answer + 'b')
