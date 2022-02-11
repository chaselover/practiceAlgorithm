import sys
input = sys.stdin.readline

for test in range(int(input())):
    n = int(input())
    x = list(map(int, input().split()))
    pivot = x[0]
    y = [0] * n
    for i in range(1, n):
        l = len(bin(pivot)[2:])
        for j in range(l):
            k = (1 << j)
            if pivot & k and not x[i] & k:
                y[i] += k
        pivot = x[i] ^ y[i]
    print(*y)