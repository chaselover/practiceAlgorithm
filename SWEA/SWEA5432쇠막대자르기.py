import sys
sys.stdin = open('input.txt')


for test in range(1,int(input())+1):
    arr = list(input())
    board = 0
    answer = 0
    for i in range(len(arr)):
        if arr[i] == '(':
            if arr[i+1] == ')':
                answer += board
            else:
                board += 1

        if arr[i] == ')':
            if arr[i-1] == ')':
                board -= 1
                answer += 1
    print(f'#{test} {answer}')
