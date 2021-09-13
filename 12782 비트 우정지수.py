import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N, M = map(lambda x: int(x,2), input().split())
    xor = N^M
    n = len(bin(xor)[2:])
    one = 0
    zero = 0
    answer  = 0
    for i in range(n):
        if xor & 1<<i:
            if M & 1<<i:
                one += 1
            else:
                zero += 1
    if zero > one:
        one, zero = zero, one
    answer += zero
    answer += one - zero
    print(answer)