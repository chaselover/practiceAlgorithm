import sys

N = int(sys.stdin.readline())



num = [int(sys.stdin.readline()) for _ in range(N)]
plus = []
minus = []
zeroOne = []

for i in range(N):
    if num[i]>1:
        plus.append(num[i])
    elif num[i]<0:
        minus.append(num[i])
    else:
        zeroOne.append(num[i])

Sum = 0


