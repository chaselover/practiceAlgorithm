import sys
input = sys.stdin.readline

a, b, c = map(int, input().split(' '))

def conq(length):
    if length == 1:
        return a %c
    if length % 2 == 0:
        left = conq(length // 2)
        return left * left %c
    else:
        left = conq(length // 2)
        return left * left * a %c


print(conq(b))

