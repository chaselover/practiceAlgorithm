import sys
input = sys.stdin.readline

for test in range(int(input())):
    a, b = map(lambda x: int(x, 2), input().split())
    print(bin(a + b)[2:])
