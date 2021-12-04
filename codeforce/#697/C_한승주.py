import sys
input = sys.stdin.readline


for test in range(int(input())):
    x = int(input())
    answer, flag = '', 0
    for num in range(9, 0, -1):
        if x >= num:
            x -= num
            answer += str(num)
        if not x:
            print(answer[::-1])
            break
    else:
        print(-1)