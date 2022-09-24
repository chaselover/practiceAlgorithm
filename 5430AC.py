import sys
input = sys.stdin.readline
from collections import deque

# R 뒤집기, D 버리기함수

# 비어있을때 D쓰면 에러.

T = int(input())

for test in range(T):
    p = input().rstrip()
    n = int(input())
    xi = input().rstrip().rstrip(']').lstrip('[').split(',')
    Xi = deque()
    if not n:
        xi.pop()
    flag=0
    switch = 0
    for x in xi:
        Xi.append(x)
    for command in p:
        if command == 'R':
            if flag:
                flag=0
            else:
                flag=1
        else:
            if Xi:
                if flag:
                    Xi.pop()
                else:
                    Xi.popleft()
            else:
                print('error')
                switch = 1
                break
    if switch:
        continue
    else:
        if flag:
            ans = ''
            while Xi:
                ans+=(Xi.pop())+','
            ans = ans[:-1]
            print(f"[{ans}]")
        else:
            ans = ",".join(Xi)
            print(f"[{ans}]")